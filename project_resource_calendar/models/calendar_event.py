# Copyright 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    resource_type = fields.Selection([
        ('user', 'Human'),
        ('equipment', 'Equipment'),
        ('room', 'Room')],
        string='Resource Type',
        default='room',
    )
    room_id = fields.Many2one(
        string='Room',
        comodel_name='resource.calendar.room',
        ondelete='set null',
    )
    equipment_ids = fields.Many2many(
        string='Equipment',
        comodel_name='resource.calendar.instrument',
        ondelete='set null',
    )
    state = fields.Selection([
        ('draft', 'Unconfirmed'),
        ('open', 'Confirmed'),
        ('cancelled', 'Cancelled')],
        string='Status',
        readonly=True,
        track_visibility='onchange',
        default='draft')
    weekday = fields.Char(
        string='Weekday',
        compute='_get_weekday',
        store=True
    )
    event_task_id = fields.Many2one(
        string='Task',
        comodel_name='project.task',
        ondelete='set null',
    )
    is_task_event = fields.Boolean(
        string='Is Created From Task',
        default=False,
    )
    sector_id = fields.Many2one(
        'res.partner.sector',
        string='Faculty Sectors',
    )

    @api.one
    @api.depends('start_datetime')
    def _get_weekday(self):
        weekdays = {
            '0': _('Monday'),
            '1': _('Tuesday'),
            '2': _('Wednesday'),
            '3': _('Thursday'),
            '4': _('Friday'),
            '5': _('Saturday'),
            '6': _('Sunday'),
        }
        if self.start_datetime:
            start_datetime = str(datetime.strptime(self.start_datetime, '%Y-%m-%d %H:%M:%S').weekday())
            for day in weekdays:
                if day == start_datetime:
                    self.weekday = str(weekdays[day])
        else:
            return False

    @api.multi
    @api.constrains('room_id', 'start', 'stop', 'equipment_ids')
    def _check_room_id_double_book(self):
        for record in self:

            if record._event_in_past() or record.state == 'draft':
                continue

            room = record.room_id.filtered(
                lambda s: s.allow_double_book is False
            )
            equipment = record.equipment_ids.filtered(
                lambda s: s.allow_double_book is False
            )

            if not any(room) and not any(equipment):
                continue

            overlaps = self.env['calendar.event'].search([
                ('id', '!=', record.id),
                ('start', '<', record.stop),
                ('stop', '>', record.start),
            ])

            for resource in overlaps.mapped(lambda s: s.room_id):
                raise ValidationError(
                    _(
                        'The room cannot be double-booked '
                        'with any overlapping meetings or events.',
                    )
                )
            for resource in overlaps.mapped(lambda s: s.equipment_ids):
                raise ValidationError(
                    _(
                        'The resource cannot be double-booked '
                        'with any overlapping meetings or events.',
                    )
                )

    def print_calendar_report(self):
        return self.env.ref('project_resource_calendar.calendar_event_report').report_action(self)
