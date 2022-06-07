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
		contact_name = request.env['res.partner'].sudo().search([])
		return request.render("kavish_frontend.exam_frontend_form", {'record': contact_name})

	@http.route(['/form/submit'], type='http', auth="user", website=True)
	def create_contact(self, **kw):
		"""
		function to create record in res partner
		"""
		files = request.httprequest.files.getlist('image_1920')
		print("files-----------------------", files)
		for file in files:
			partner = request.env['res.partner'].create({
				'name': kw.get('name'),
				'email': kw.get('email'),
				'phone': kw.get('phone'),
				'image_1920': base64.b64encode(file.read())
			})
			print("-------------------", partner)
		return request.render(
			"kavish_frontend.contact_form_record", {})
