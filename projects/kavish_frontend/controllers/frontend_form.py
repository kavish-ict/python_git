# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal
import base64
from base64 import decodestring


class Website(http.Controller):
    """
    class for Website
    """

    @http.route(['/form'], type='http', auth="user", website=True)
    def contact_creation(self):
        """
        function to open the form page and search records of
        res partner
        """
        # files = request.httprequest.files.getlist('image_1920')
        # for file in files:
        #     partner_id = int(kw.get('partner_id'))
        #     attachment = file.read()
        #     partner = request.env['res.partner'].sudo().browse(partner_id)
        #     if partner:
        #         partner.create({'image_1920': base64.encodestring(attachment)})
        contact_name = request.env['res.partner'].sudo().search([])
        return request.render("kavish_frontend.exam_frontend_form", {'record': contact_name})

    @http.route(['/form/submit'], type='http', auth="user", website=True)
    def create_contact(self, **kw):
        """
        function to create record in res partner
        """
        files = request.httprequest.files.getlist('image_1920')
        print("--------file", files)
        for file in files:
            # partner_id = kw.get('')
            # print("partner_id----------", partner_id)
            upload_file = kw.get('image_1920')
            name = kw.get('image_1920').filename
            print("attachment----------------", upload_file)
            partner = request.env['res.partner'].create({'name': name,
                                                         'image_1920': base64.b64encode(upload_file.read())})
            print("-------------------", partner)
        # request.env.user.image_1920 = base64.encodestring(attachment)
        # print("-----------------",kw)
        # attached_files = request.httprequest.files.getlist('image_1920')
        # print("--------------------attached_files--------------", attached_files)
        # # for attach in attached_files:
        # #     print("-----------------------------post", attach)
        # Attachments = request.env['res.partner']
        # print("_______attachment-------------", Attachments)
        # name = kw.get('image_1920').filename
        # print("-------------name--------", name)
        # upload_file = kw.get('image_1920')
        # print("---------------file----------------", upload_file)
        # attachment_id = Attachments.create({
        #         'name': name,
        #         'image_1920': base64.b64encode(upload_file.read()),
        #     })
        if kw:
            request.env['res.partner'].sudo().create(kw)
        return request.render(
            "kavish_frontend.contact_form_record", {})

    @http.route('/next', type='http', auth="public", website=True, csrf=False)
    def upload_image(self, **kw):
        attached_files = request.httprequest.files.getlist('image_1920')
        print("--------------------attached_files--------------", attached_files)
        for attach in attached_files:
            print("-----------------------------post", attach)
            Attachments = request.env['res.partner']
            print("_______attachment-------------", Attachments)
            name = kw.get('image_1920').filename
            print("-------------name--------", name)
            upload_file = kw.get('image_1920')
            print("---------------file----------------", type(upload_file))
            # project_id = post.get('project_id')
            # print("-----------------", project_id)
            attachment_id = Attachments.sudo().create({
                'name': name,
                'image_1920': base64.b64encode(upload_file.read()),
            })
