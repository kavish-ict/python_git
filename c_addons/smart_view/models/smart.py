# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class SmartView(models.Model):
    _name = 'smart.view'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_id = fields.Char(string="Name")
    new_names = fields.Many2one('college_management.college_management',string="Names List")
    mobile_id = fields.Integer(string="Mobile",tracking=True,related="new_names.mobileid")
    quantity_id = fields.Integer(string="Quantity")
    # ref = fields.Many2one('college_management.college_management',string="refernce")
    date_id = fields.Datetime(string='Date',default=fields.Datetime.now)



    # _sql_constraints = [
    #         ('name_uniq', 'unique (name_id)', "Name is already in use"),
    #     ]

    _sql_constraints = [
        ('name_uniq', 'CHECK(quantity_id>0)', "Less Quantity "),
    ]


    def check(self):
        k = {'name_id': 'kavish'}
        return self.create(k)
    def create_record(self):

        self.create({
            "name": "jake",
            "email_id":"jake@gmail.com",
            "url_id":"instagram.com",
            "my_field":"option1",
            "branch_id":"option3",
            "priority":"4"
        })
    # @api.constrains('name_id')
    # def test(self):
    #     for rec in self:
    #         if rec.name_id.isalpha() == False:
    #             raise ValidationError("invalid name")


    def test(self):
        vals = {"name_id":"james"}
        self.message_post(body="record updated")
        self.write(vals)




    # @api.constrains('mobile_id')
    # def test_id(self):
    #     for rec in self:
    #         if len(rec.mobile_id) > 10:
    #             raise ValidationError("number is greater than 10 digits")
    #         elif len(rec.mobile_id) < 10:
    #             raise ValidationError("number is less than 10 digits")



