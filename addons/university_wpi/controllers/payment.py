# university_wpi/controllers/payment.py
from odoo import http
from odoo.http import request

class UniversityPayment(http.Controller):

    @http.route('/payment/process', type='http', auth="public", methods=['POST'])
    def process_payment(self, **post):
        order_id = post.get('order_id')
        order = request.env['web30s.order'].sudo().browse(int(order_id))
        order.write({'status': 'paid'})
        # Lưu giao dịch thanh toán nếu cần
        return request.redirect('/payment/success')

    @http.route('/payment/success', type='http', auth="public", website=True)
    def payment_success(self, **kwargs):
        return request.render("university_wpi.payment_success_template", {})
