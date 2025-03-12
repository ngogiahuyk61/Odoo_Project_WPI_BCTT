# university_wpi/models/payment.py
from odoo import models, fields

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'
    # Thêm các trường hoặc override nếu cần

    order_id = fields.Many2one('web30s.order', string='Order', required=True)
    transaction_id = fields.Char(string='Transaction ID')
    amount = fields.Float(string='Amount')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ], default='pending')
