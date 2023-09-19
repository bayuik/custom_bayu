from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    request_vendor = fields.Many2one('res.partner', string='Request Vendor')
    contract_number = fields.Char(string='Contract Number')
    with_po = fields.Boolean(string='With PO')
    purchase_order_ids = fields.One2many('purchase.order', 'sale_order_id', string='Purchase Order')

    def create_purchase_order(self):
        vals = {
            'partner_id': self.request_vendor.id,
            'partner_ref': self.name,
            'date_order': self.date_order,
            'currency_id': self.currency_id.id,
            'state': 'purchase',
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'product_qty': line.product_uom_qty,
                'product_uom': line.product_uom.id,
                'name': line.name,
                'price_unit': line.price_unit,
            }) for line in self.order_line],
        }
        self.env['purchase.order'].create(vals)

    def action_confirm(self):
        contract = self.env['sale.order'].search([('contract_number', '=', self.contract_number)])
        if contract:
            raise ValidationError(_('Contract Number already exist'))
        return super(SaleOrder, self).action_confirm()

    def action_import_so_lines(self):
        return {
            'name': _('Import SO Lines'),
            'view_mode': 'form',
            'res_model': 'import.so.lines',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

