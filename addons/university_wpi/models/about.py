# university_wpi/models/about.py
from odoo import models, fields

class About(models.Model):
    _name = 'about.about'
    _description = 'About Us'

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    image = fields.Binary(string='Image')
    video_url = fields.Char(string='Video URL')
