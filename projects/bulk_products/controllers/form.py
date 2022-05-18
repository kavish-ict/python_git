# -*- coding: utf-8 -*-
import base64
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class BulkProductsPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(BulkProductsPortal, self)._prepare_home_portal_values(counters)
        products_count = request.env["hr.contract"].search_count(
            [('employee_id', '=', request.env.user.employee_id.id)])
        values.update({
            'products_count': products_count
        })
        return values

    @http.route(['/my/contracts'], type='http', auth="user", website=True)
    def show_contracts(self):
        print("========\n\n", request.env.user.employee_id.id)
        contract_list = request.env['hr.contract'].sudo().search(
            [('employee_id', '=', request.env.user.employee_id.id)])
        return request.render(
            "bulk_products.portal_my_contract", {'show_contracts': contract_list})

    @http.route(['/my/contracts/details<model("hr.contract"):record>'], type='http', auth="user", website=True)
    def show_contracts_details_id(self, record):
        return request.render(
            "bulk_products.contract_form_page_id", {'show_contracts_details_id': record})

    @http.route('/submit', type='http', auth="public", website=True, csrf=False)
    def upload_files(self, **post):
        values = {}
        attached_files = request.httprequest.files.getlist('attachment')
        for attach in attached_files:
            print("-----------------------------post", attach)
            Attachments = request.env['ir.attachment']
            print("_______attachment-------------", Attachments)
            name = post.get('attachment').filename
            print("-------------name--------", name)
            upload_file = post.get('attachment')
            print("---------------file----------------", type(upload_file))
            project_id = post.get('project_id')
            print("-----------------", project_id)
            attachment_id = Attachments.sudo().create({
                'name': name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'hr.contract',
                'res_id': project_id,
                'datas': base64.b64encode(upload_file.read()),
            })
            value = {
                'attachment': attachment_id
            }
