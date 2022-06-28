from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale order"

    def apply_promotional_discount(self):
        pro_discount = self.env['product.product'].search([('default_code', '=', 'DISC')])
        promo_disc = self.env['promotional.discount'].search(
            [('start_date', '<=', self.date_order), ('end_date', '>=', self.date_order),
             ('minimum_order_amount', '<=', self.amount_total)])
        print("-----------------------------discount", pro_discount)
        print("-----------------------------promotional", promo_disc)
        final_discount = []
        for rec in promo_disc:
            print("============================rec", rec)
            if rec.discount_type == 'fixed':
                # price = rec.fixed_discount
                final_discount.append(rec.fixed_discount)

                # new_line.append((0, 0, {
                #     'product_id': pro_discount.id,
                #     'price_unit': "-" + str(rec.fixed_discount)
                # }))
                print("==============================price", final_discount)
                print("---------------------fixed_discount", min(final_discount))
            # print("=============================new_line", new_line)
            elif rec.discount_type == 'percentage':
                for res in self.order_line:
                    price = (res.price_unit * (rec.discount / 100.0))
                    final_discount.append(price)
                    print("-----------------price", price)
                print("-------------------------percentage_discount", final_discount)
                print("-------------------------percentage_discount", min(final_discount))

        self.update({'order_line': [(0, 0, {
            'product_id': pro_discount.id,
            'price_unit': "-" + str(min(final_discount))})]
                     })


    # new_line.append((0, 0, {
    #     'product_id': pro_discount.id,
    #     'price_unit': "-" + str(rec.discount)
    # }))
    # print("=============================new_line", new_line)

    # self.write({
    #     'order_line': {'product_id': pro_discount.id,
    #                    'price_unit':}
    #     'amount_total': price
    # })

