# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class Website(http.Controller):

    @http.route(['/advance'], type='http', auth="user", website=True)
    def advance(self, **data):
        """
        function to open the form page
        """
        return request.render("advance_actions.website_form", {})

    @http.route(['/advance/submit'], type='http', auth="user", website=True)
    def advance_submit(self, **data):
        """
        function to create record from website form
        """
        request.env['advance.action'].sudo().create([data])
        return request.render(
            "advance_actions.website_form_record", {})

    @http.route(['/advance/submit/records'], type='http', auth="user", website=True)
    def show_records(self):
        show = request.env['advance.action'].sudo().search([])
        return request.render(
            "advance_actions.advance_action_records", {'show_details': show})


