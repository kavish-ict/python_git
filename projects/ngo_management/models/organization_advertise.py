from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import *


class OrganizationAdvertise(models.Model):
    _name = "organization.advertise"
    _description = "organization advertise"

    o_organization = fields.Many2one('orphans.organization', string="Organization Home")
    avl_seats = fields.Integer(string="Available Seats")
    exp_dates = fields.Date(string="Expired Dates")
    facilities = fields.Html(string="Facilities")
    s1 = fields.Char(string="Address",related="o_organization.street1")
    s2 = fields.Char(related="o_organization.street2")
    city = fields.Char(related="o_organization.city")
    state = fields.Char(related="o_organization.state")
    zip = fields.Char(related="o_organization.zip")
    country = fields.Char(related="o_organization.country")
    image = fields.Binary()

    def s_button(self):
        print("works")

    # @api.depends('')