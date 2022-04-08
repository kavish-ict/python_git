"""
new module
"""
import xlwt
from xlwt import easyxf
from io import BytesIO

work_book = xlwt.Workbook()
sheet = work_book.add_sheet("test sheet")
header_style = easyxf('font:height 500; align: horiz center;font:bold True;')
sheet.write_merge(2, 3, 3, 6, "TimeSheet", header_style)
sheet.col(0).width = 3000
sheet.write(9,1,'Name')
fp = BytesIO()

work_book.save("new.xls")
