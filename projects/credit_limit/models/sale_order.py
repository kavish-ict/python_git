from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Created this module."

    @api.onchange('partner_id')
    def test(self):
        res = self.env['product.template'].search([('detailed_type', '=', 'consu'),
                                                   ('sale_ok', '=', True)], limit=10)
        print("------------------", res)

    @api.model
    def create(self, vals):
        object_search = self.env['sale.order'].search([('state', '=', 'draft'),
                                                       ('partner_id', '=', vals.get('partner_id'))])
        block_search = self.env['sale.order'].search([('state', '=', 'sale'),
                                                      ('partner_id', '=', vals.get('partner_id'))])
        total_records = object_search + block_search
        print("------------total records--------------", total_records)
        print("------credit limit records---------------", object_search)
        print("--------block limit records-------------", block_search)
        total_credit_score = []
        total_block_score = []
        for rec in total_records:
            if rec.state == 'draft':
                print("-------------------draft-------------------")
                total_credit_score.append(rec.amount_total)
                print("------total credit score------", total_credit_score)
                total = sum(total_credit_score)
                if total > rec.partner_id.credit_limit_score:
                    raise ValidationError('Your Sale Order Credit Limit has been Exceeded.')
                else:
                    pass
            else:
                pass
            if rec.state == 'sale':
                print("-------------------sale-------------------")
                total_block_score.append(rec.amount_total)
                print("------total block score------", total_block_score)
                block_total = sum(total_block_score)
                if block_total > rec.partner_id.block_limit_score:

                    raise ValidationError("You cannot create Sale Order as the Block Limit has been Exceeded")
                else:
                    pass
            else:
                pass
        # for rec in block_search:
        #     total_block_score.append(rec.amount_total)
        #     block_total = sum(total_block_score)
        #     if block_total > rec.partner_id.block_limit_score:
        #         raise ValidationError("You cannot create Sale Order as the Block Limit has been Exceeded")
        #     else:
        #         pass
        return super(SaleOrder, self).create(vals)
