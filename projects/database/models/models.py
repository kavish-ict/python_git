# -*- coding: utf-8 -*-
import required as required

from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record


class database(models.Model):
    _name = 'database.database'
    _description = 'database.database'

    name = fields.Char(readonly=True,string="name", default="kavish")
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()
    dob = fields.Date(required=True, help="Date of Birth")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100



