# university_wpi/controllers/api.py
from odoo import http
from odoo.http import request

class UniversityAPI(http.Controller):

    @http.route('/api/blog', type='json', auth="public", methods=['GET'])
    def api_get_blog(self, **kwargs):
        posts = request.env['blog.post'].sudo().search([])
        result = []
        for post in posts:
            result.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'create_date': post.create_date,
            })
        return result

    # Bạn có thể xây dựng thêm API cho Event, Order, … tương tự
