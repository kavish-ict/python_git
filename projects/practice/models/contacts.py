# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ContactView(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="Birthdate")
    customer_reference = fields.Char(string="Customer Reference")
