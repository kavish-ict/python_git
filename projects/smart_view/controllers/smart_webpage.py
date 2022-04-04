from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    @http.route(['/smart'], type='http', auth="user", website=True)
    def smart(self, **data):
        """
        function created to view all records of  smart view module
        """
        smart = request.env['smart.view'].sudo().search([])
        return request.render(
            "smart_view.smart_view_details_page", {'smart_details': smart})

    @http.route(['/smart/details/<model("smart.view"):smart>'], type='http', auth="user", website=True)
    def smart_record(self, smart):
        """
        function created to view details of record
        """
        return request.render(
            "smart_view.smart_view_form_page", {'smart_form': smart})

