# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PartnerCategoryType(models.Model):
    _name = 'res.partner.category.type'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
    )
