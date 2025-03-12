# university_wpi/controllers/website.py
from odoo import http
from odoo.http import request

class UniversityWebsite(http.Controller):

    @http.route('/', type='http', auth="public", website=True)
    def home(self, **kwargs):
        return request.render("university_wpi.home_template", {})

    @http.route('/about', type='http', auth="public", website=True)
    def about(self, **kwargs):
        company = request.env['about.about'].sudo().search([], limit=1)
        experts = request.env['hr.employee'].sudo().search([('is_expert','=',True)])
        return request.render("university_wpi.about_template", {'company': company, 'experts': experts})

    @http.route('/projects', type='http', auth="public", website=True)
    def projects(self, **kwargs):
        return request.render("university_wpi.projects_template", {})

    @http.route('/admission', type='http', auth="public", website=True)
    def admission(self, **kwargs):
        return request.render("university_wpi.admission_template", {})

    @http.route('/news', type='http', auth="public", website=True)
    def news(self, **kwargs):
        posts = request.env['blog.post'].sudo().search([])
        return request.render("university_wpi.news_template", {'posts': posts})

    @http.route('/gallery', type='http', auth="public", website=True)
    def gallery(self, **kwargs):
        return request.render("university_wpi.gallery_template", {})

    @http.route('/video', type='http', auth="public", website=True)
    def video(self, **kwargs):
        return request.render("university_wpi.video_template", {})

    @http.route('/contact', type='http', auth="public", website=True)
    def contact(self, **kwargs):
        return request.render("university_wpi.contact_template", {})

    @http.route('/contact/submit', type='http', auth="public", website=True, methods=['POST'])
    def contact_submit(self, **post):
        vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'message': post.get('message'),
        }
        request.env['contact.request'].sudo().create(vals)
        # Có thể tích hợp gửi email thông báo tại đây
        return request.render("university_wpi.contact_thanks_template", {})
