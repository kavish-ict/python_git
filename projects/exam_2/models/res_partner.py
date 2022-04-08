"""inherited res partner''"""

import datetime
from odoo import models, fields, api


class ResPartner(models.Model):
    """
    class created for res partner
    """
    _inherit = 'res.partner'
    _description = "Created this module."

    age = fields.Integer(compute="_compute_years", string="Age")
    birth_date = fields.Date(string="Date of Birth", default=datetime.date.today())

    @api.depends("birth_date")
    def _compute_years(self):
        """
        function to get age based on birthdate
        """
        today = datetime.date.today()
        for rec in self:
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year - \
                          ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
