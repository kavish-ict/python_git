# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class Website(http.Controller):

    @http.route(['/advance'], type='http', auth="user", website=True)
    def advance(self, **data):
        """
        function to open the form page
        """
        country = request.env['res.country'].sudo().search([])
        return request.render("advance_actions.website_form", {"countries": country})

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
        advance = request.env['advance.action'].sudo().search([])

        return request.render(
            "advance_actions.advance_action_records", {'show_details': advance})

    @http.route(['/advance/submit/records/<model("advance.action"):advance>'], type='http', auth="user", website=True)
    def advance_record(self, advance):
        """
        function created to view details of record
        """
        return request.render(
            "advance_actions.advance_action_form_page", {'advanceform': advance})


class AdvanceActionPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super( AdvanceActionPortal, self)._prepare_home_portal_values(counters)
        student_count = request.env["advance.action"].search_count([])
        values.update({
            'student_count': student_count
        })
        return values

    @http.route(['/advance/submit/records'], type='http', auth="user", website=True)
    def show_records(self):
        advance = request.env['advance.action'].sudo().search([])

        return request.render(
            "advance_actions.advance_action_records", {'show_details': advance})
