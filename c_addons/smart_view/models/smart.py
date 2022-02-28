# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SmartView(models.Model):
    _name = 'smart.view'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_id = fields.Char(string="Name",tracking=True)
    mobile_id = fields.Char(string="Mobile",tracking=True)
    quantity_id = fields.Integer(string="Quantity")



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