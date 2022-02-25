# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SmartView(models.Model):
    _name = 'smart.view'

    name_id = fields.Char(string="Name")
    mobile_id = fields.Char(string="Mobile")


    _sql_constraints = [
            ('name_uniq', 'unique (name_id)', "Name is already in use"),
        ]
    @api.constrains('name_id')
    def test(self):
        for rec in self:
            if rec.name_id.isalpha() == False:
                raise ValidationError("invalid name")

    # @api.constrains('mobile_id')
    # def test_id(self):
    #     for rec in self:
    #         if len(rec.mobile_id) > 10:
    #             raise ValidationError("number is greater than 10 digits")
    #         elif len(rec.mobile_id) < 10:
    #             raise ValidationError("number is less than 10 digits")