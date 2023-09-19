import base64
import io
import pandas as pd
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ImportSoLines(models.TransientModel):
    _name = "import.so.lines"
    file = fields.Binary(string='File')

    def import_excel(self):
        a = ''
        if self.file:
            file = base64.b64decode(self.file)
            excel_data = pd.read_excel(io.BytesIO(file))
            for index, row in excel_data.iterrows():
                product = self.env['product.product'].search([('default_code', '=', row['Product Code'])])
                if product:
                    a += row['Product Code'] + ' '
                    self.env['sale.order.line'].create({
                        'product_id': product.id,
                        'product_uom_qty': row['Qty'],
                        'product_uom': product.uom_id.id,
                        'name': product.name,
                        'price_unit': row['Unit Price'],
                        'order_id': self.env.context.get('active_id')
                    })
        else:
            raise ValidationError(_('Please upload file first'))

    def download_template(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/custom_bayu/static/template/SO_Lines_template.xlsx',
            'target': 'new',
        }
