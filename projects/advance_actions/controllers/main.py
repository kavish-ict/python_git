# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    @http.route(['/contacts'], type='http', auth="user", website=True)
    def contacts(self, **data):
        contacts = request.env['res.partner'].sudo().search([])
        return request.render(
            "advance_actions.contacts_list", {})
