from odoo import fields, models, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')