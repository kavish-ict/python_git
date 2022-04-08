"""
new module
"""
from odoo import models, fields, api
import io
import xlwt
from datetime import datetime, timedelta
import base64
from odoo.exceptions import ValidationError
from xlwt import easyxf


class HrWizard(models.Model):
    _name = 'hr.wizard'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "create new object for rental"
    # _rec_name = 'name'

    # name = fields.Many2many(string="Name")
    employee_ids = fields.Many2many('hr.employee', string="Employee name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    excel_name = fields.Binary('Download report', readonly=True)
    state = fields.Selection([('choose', 'choose'), ('get', 'get')],
                             default='choose')

    # work_book = xlwt.Workbook()
    # sheet = work_book.add_sheet("test sheet")
    # header_style = easyxf('font:height 500; align: horiz center;font:bold True;')
    # sheet.write_merge(2, 3, 3, 6, "TimeSheet", header_style)
    # sheet.col(0).width = 3000
    # sheet.write(9, 1, 'Name')
    # fp = io.BytesIO()
    #
    # work_book.save(fp)
    # fp.seek(0)
    # excel_file = base64.encodestring(fp.read())
    # fp.close()
    # self.write(
    #     {'state': 'get', 'file_name': base64.encodestring(fp.getvalue()), 'summary_data': file_name})
    # fp.close()
    # return {
    #     'type': 'ir.actions.act_window',
    #     'res_model': 'advance.report',
    #     'view_mode': 'form',
    #     'view_type': 'form',
    #     'res_id': self.id,
    #     'target': 'new',
    # }

    def action_xlwt_report(self):
        # company_name = self.name
        account_env = self.env['account.analytic.line']
        file_name = 'Timesheet.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")
        format0 = xlwt.easyxf(
            'font:height 500,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: '
            'top_color black, bottom_color black, right_color black, left_color black,\ left thin, right thin, '
            'top thin, bottom thin;')
        format1 = xlwt.easyxf('font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz left; borders: '
                              'top_color black, bottom_color black, right_color black, left_color black,\ left thin, '
                              'right thin, top thin, bottom thin;')
        sheet = workbook.add_sheet("Timesheet")

        sheet.col(0).width = int(7 * 260)
        sheet.col(1).width = int(30 * 260)
        sheet.col(2).width = int(40 * 260)
        sheet.col(3).width = int(30 * 280)
        sheet.col(4).width = int(30 * 280)
        sheet.row(0).height = 150 * 4
        sheet.row(1).height = 150 * 2
        # sheet.row(2).height = 150 * 3
        sheet.row(3).height = 150 * 4
        sheet.write_merge(0, 0, 1, 5, 'TimeSheet Report', format0)
        sheet.write(3, 1, 'Employee Name', format1)
        sheet.write(3, 2, 'Project', format1)
        sheet.write(3, 3, 'Task', format1)
        sheet.write(3, 4, 'Description', format1)
        sheet.write(3, 5, 'Hours', format1)
        row = 3
        for record in self.employee_ids:
            col = 1
            row += 1
            sheet.write(row, col, record.name)
            data = account_env.search([("employee_id", "=", record.id)])

            new_row = row
            for project in data:
                col = 2
                sheet.write(new_row, col, project.project_id.name)
                new_row += 1

            new_row = row
            for task in data:
                col = 3
                sheet.write(new_row, col, task.task_id.name)
                new_row += 1

            new_row = row
            for description in data:
                col = 4
                sheet.write(new_row, col, description.name)
                new_row += 1

            new_row = row
            for hours in data:
                col = 5
                sheet.write(new_row, col, hours.unit_amount)
                new_row += 1
                row = new_row
        fp = io.BytesIO()
        workbook.save(fp)
        fp.seek(0)
        excel_name = base64.encodebytes(fp.getvalue())
        self.write(
            {'excel_name': excel_name})

        fp.close()
        url = ('web/content/?model=hr.wizard&download=true&field=excel_name&id=%s&file_name=%s' % (
            self.id, file_name))
        if self.excel_name:
            return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new'
            }

    _sql_constraints = [
        ('name_uniq', 'CHECK(start_date<end_date)', "START DATE SHOULD BE LESS THAN END DATE "),
    ]

#
# self.write({
#             'excel_file': excel_file
#         })
#         url = ('web/content/?model=timesheet.wizard&download=true&field=excel_file&id=%s&filename=%s' % (
#             self.id, file_name))
#         if self.excel_file:
#             return{
#                 'type': 'ir.actions.act_url',
#                 'url': url,
#                 'target': 'new'
#             }