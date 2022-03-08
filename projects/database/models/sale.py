# -*- coding: utf-8 -*-
import required as required

from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    # _description = 'database.database'

    sales_description = fields.Char(readonly=True,string="name", default="kavish")


