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

    # @http.route(['/advance/submit'], type='http', auth="user", website=True)
    # def advance_submit(self, **data):
    #     """
    #     function to create record from website form
    #     """
    #     request.env['advance.action'].sudo().create([data])
    #     return request.render(
    #         "advance_actions.website_form_record", {})

    @http.route(['/advance/submit/records'], type='http', auth="user", website=True)
    def show_records(self):
        advance = request.env['advance.action'].sudo().search([])

        return request.render(
            "advance_actions.advance_action_records", {'show_details': advance})

    @http.route(['/advance/submit/records/<model("advance.action"):advance>'],
                type='http', auth="user", website=True)
    def advance_record(self, advance=None, **post):
        """
        function created to view details of record
        """
        print('\n\ncontact---------------', advance, '\n\n')
        print('\n\npost---------------', post, '\n\n')
        # if post:
        #     advance_object = request.env['advance.action']
        #     data = {
        #         'name': post.get('name'),
        #         'phone': post.get('phone'),
        #         'email_id': post.get('email_id'),
        #     }
        #     if post.get('name_id'):
        #         advance_object.browse(int(post.get('name_id'))).update(data)
        #     else:
        #         advance_object.create(data)
        #     return request.redirect('/advance/submit/records')
        return request.render(
            "advance_actions.advance_action_form_page", {'advanceform': advance})

    @http.route(['/advance/submit', '/advance/submit/<model("advance.action"):record>'],
                type='http', auth="user", website=True)
    def show_records_details(self, record=None, **post):
        print("------------------------------------------", post)
        print("------------------------------------------", record)
        country = request.env['res.country'].sudo().search([])
        if post:
            advance_object = request.env['advance.action']
            data = {
                'name': post.get('name'),
                'phone': post.get('phone'),
                'email_id': post.get('email_id'),
            }
            if post.get('name_id'):
                advance_object.browse(int(post.get('name_id'))).update(data)
            else:
                advance_object.create(data)
            return request.redirect('/advance/submit/records')
        return request.render(
            "advance_actions.website_form", {'record': record,
                                             "countries": country})


class AdvanceActionPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(AdvanceActionPortal, self)._prepare_home_portal_values(counters)
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
