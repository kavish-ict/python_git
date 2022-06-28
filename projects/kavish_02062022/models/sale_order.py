from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    batch_sale_tags = fields.Many2many('res.partner.category', string="Tags")

    def _search(self, args, offset=None, limit=None, order=None, count=False):
        # res = super(SaleOrder, self)._search([])
        # print("----------------------------", res)
        print("-------------args---------------", args)
        # return res
        new_env = self.env['batch.sale.workflow']._context.get('operation_type')
        print("-----------env-------", new_env)
        if new_env == 'confirm':
            print("-------confirm-----------")
            args = [('state', 'in', ['draft', 'sent']), ('user_id', '=', self._context.get('responsible_id'))]
            # return super(SaleOrder, self)._search([('state', 'in', ['draft', 'sent'])], offset=None,  limit=None,
            # order=None, count=False)
        elif new_env == 'cancel':
            print("-------cancel-----------")
            args = [('state', 'in', ['draft', 'sent', 'sale']), ('user_id', '=', self._context.get('responsible_id'))]
            # return super(SaleOrder, self)._search([('state', 'in', ['draft', 'sent', 'sale'])], offset=None,
            # limit=None, order=None, count=False)
        elif new_env == 'merge':
            print("-----------merge------------")
            args = [('state', 'in', ['draft', 'sent']), ('user_id', '=', self._context.get('responsible_id')),
                    ('partner_id', '=', self._context.get('partner_id'))]
            # return super(SaleOrder, self)._search([('state', 'in', ['draft', 'sent'])], offset=None,  limit=None,
            # order=None, count=False)
        return super(SaleOrder, self)._search(args)
