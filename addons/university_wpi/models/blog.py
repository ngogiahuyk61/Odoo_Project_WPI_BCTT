# university_wpi/models/blog.py
from odoo import models, fields

class BlogPost(models.Model):
    _name = 'blog.post'
    _description = 'Blog Post'

    title = fields.Char(string='Title', required=True)
    content = fields.Html(string='Content')
    author_id = fields.Many2one('res.users', string='Author', default=lambda self: self.env.user)
    image = fields.Binary(string='Featured Image')
    status = fields.Selection([('draft', 'Draft'), ('published', 'Published')], default='draft')
    create_date = fields.Datetime(string='Created Date', readonly=True)
