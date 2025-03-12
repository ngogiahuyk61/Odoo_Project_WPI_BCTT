# university_wpi/models/contact.py
from odoo import models, fields

class ContactRequest(models.Model):
    _name = 'contact.request'
    _description = 'Contact Request'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    message = fields.Text(string='Message')
    request_date = fields.Datetime(string='Request Date', default=fields.Datetime.now)
