# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class EventTemplate(models.Model):
    """Event Template"""
    _name = "event.template"
    _description = __doc__

    name = fields.Char(
        string='Name',
    )
    temp_resp_id = fields.Many2one(
        'res.partner',
        string='Responsible',
    )
    activity_template_ids = fields.One2many(
        'activity.template',
        'event_template_id',
        string='Activity Template',
    )
    notes = fields.Html(
        string='Notes',
    )
