import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError

import datetime


class ResPartner(models.Model):
    """
    res.partner inherited
    """
    _inherit = 'res.partner'

    age = fields.Integer(compute="_compute_age_calculator", string="AGE")
    birth_date = fields.Date(string="Date of Birth", default=datetime.date.today())

    # today_date = fields.Date(default=date.today())

    # def name_get(self):
    #     """
    #     function to concatenate two fields
    #     """
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s -- %s' % (rec.name, rec.customer_ref_no)))
    #     return res
    #
    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=10, name_get_uid=None):
    #     """
    #     function to search record with phone number or email
    #     """
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
    #     return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    # @api.depends("date_of_birth")
    # def _compute_years(self):
    #     today = date.today()
    #     for rec in self:
    #         # dob = rec.date_of_birth
    #         if rec.date_of_birth:
    #             rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
    # @api.depends('date_of_birth')
    # def _compute_your_age(self):
    #     today_date = datetime.date.today()
    #     for rec in self:
    #         new_age = int((today_date - rec.date_of_birth).days) / 365
    #     rec.age = new_age

    # def age(birthdate):
    #     today = date.today()
    #     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    #     return age

    # @api.depends('birth_date')
    # def _compute_age_calculator(self):
    #     today_date = datetime.date.today()
    #     for rec in self:
    #         rec.age = int((today_date - rec.birth_date).days / 365)

    @api.depends('birth_date')
    def _compute_age_calculator(self):
        today_date = datetime.date.today()
        for rec in self:
            if rec.birth_date:
                rec.age = today_date.year - rec.birth_date.year - ((today_date.month,today_date.day) < (rec.birth_date.month,rec.birth_date.day))
            else:
                rec.age = 0


