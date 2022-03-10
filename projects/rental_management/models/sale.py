"""
new module
"""
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    """
    sale order module inherited
    """
    _inherit = 'sale.order'
    _description = "inherit sale order object"

    new_mobile = fields.Char(string="Mobile No.")
    new_email = fields.Char(string="Email")

    @api.onchange('partner_id')
    def onchange_mobile_email(self):
        """
            while selecting name, mobile and email gets automatically updated
        """
        for rec in self:
            if rec.partner_id:
                rec.new_email = rec.partner_id.email
                rec.new_mobile = rec.partner_id.phone
        # for rec in self:
        #     if rec.partner_id.name:
        #         rec.new_mobile = "123456"
        #         rec.new_email = rec.partner_id.name + "@gmail.com"

    @api.constrains('payment_term_id')
    def check_condition(self):
        """
            checks that value of two are same or not, if not then throws user-error
        """
        for rec in self:
            print("-------------------------------------------", rec.partner_id.property_payment_term_id)
            if rec.payment_term_id != rec.partner_id.property_payment_term_id:
                raise UserError('wrong value')
