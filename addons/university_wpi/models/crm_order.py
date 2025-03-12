# university_wpi/models/crm_order.py
from odoo import models, fields

class CRMCustomer(models.Model):
    _name = 'crm.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    order_ids = fields.One2many('web30s.order', 'customer_id', string='Orders')

class Web30sOrder(models.Model):
    _name = 'web30s.order'
    _description = 'Order'

    name = fields.Char(string='Order Reference', required=True)
    customer_id = fields.Many2one('crm.customer', string='Customer', required=True)
    create_date = fields.Datetime(string='Order Date', readonly=True)
    payment_method = fields.Selection([
        ('cod', 'Cash on Delivery'),
        ('vnpay', 'VNPay'),
        ('momo', 'MoMo'),
        ('zalopay', 'ZaloPay'),
        ('card', 'Credit Card')
    ], string='Payment Method')
    total_amount = fields.Float(string='Total Amount')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('done', 'Done')
    ], default='draft')
