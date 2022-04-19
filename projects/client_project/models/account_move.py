from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = "Created this module."

    def generate_bill(self):

        vendor_ids = self.invoice_line_ids.mapped("vendor_id.id")
        print("-------------------", vendor_ids)
        for record in vendor_ids:
            vendor_list = []
            for line in self.invoice_line_ids.filtered(lambda x: x.vendor_id.id == record):
                vendor_list.append((0, 0, {"product_id": line.product_id.id, "price_unit": line.vendor_price}))
            res = self.create({
                'move_type': 'in_invoice',
                'partner_id': record,
                'invoice_line_ids': vendor_list
            })
        # return self.env['ir.actions.act_window']._for_xml_id("account.action_move_in_invoice_type")
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Subscription Bill',
        #     'res_model': "account.move",
        #     "res_id": "account.action_move_in_invoice_type",
        #     'view_mode': "tree,form",
        #
        #     'domain': [('move_type', '=', 'in_invoice')]
        # }
        # return {
        #     'type': 'ir.actions.act_url',
        #     'target': 'self',
        #     'url': 'https://www.youtube.com'}
