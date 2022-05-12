# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class Website(http.Controller):

    @http.route(['/referral'], type='http', auth="user", website=True)
    def referral_application(self, **kw):
        """
        function to open the form page
        """
        referal_name = request.env['hr.employee'].sudo().search([])
        degree = request.env['hr.recruitment.degree'].sudo().search([])
        department = request.env['hr.job'].sudo().search([])
        return request.render("referal.hr_referral_form", {'record': referal_name,
                                                           'degree_list': degree, 'department_key': department})

    @http.route(['/referral/submit'], type='http', auth="user", website=True)
    def create_referral(self, **kw):
        print("________________________", kw)
        if kw:
            request.env['hr.referral.application'].sudo().create(kw)
        return request.render(
            "referal.referral_form_record", {})
