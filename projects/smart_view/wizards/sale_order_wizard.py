# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2one


class SaleOrderWizard(models.TransientModel):
    """
    created wizard
    """
    _name = 'sale.wizard'
    customer = fields.Char(string='Customer')
    customer_email = fields.Char(string='Email')
    sales_person = fields.Char(string='SalesPerson')
    sales_person_contact = fields.Char(string='SalesPerson Contact')
    paymentterms_id = fields.Many2one('account.payment.term', string='Payment Terms')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    # @api.model
    # def default_get(self, fields):
    #     """
    #     this function returns updated recordset
    #     """
    #     res = super(SaleOrderWizard, self).default_get(fields)
    #     rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
    #
    #     res.update({
    #         'customer': rec.partner_id.name,
    #         'customer_email': rec.partner_id.email,
    #         'sales_person': rec.user_id.name,
    #         'sales_person_contact': rec.user_id.phone,
    #         'paymentterms_id': rec.payment_term_id
    #     })
    #     return res

    def search_record(self):
        """
        function to print name of record 3 and 15
        """
        res_list = self.env['res.partner'].browse([3, 15]).read(['name'])
        for rec in res_list:
            print(rec)
