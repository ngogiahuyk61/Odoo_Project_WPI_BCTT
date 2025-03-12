# university_wpi/models/event.py
from odoo import models, fields

class Event(models.Model):
    _name = 'event.event'
    _description = 'Event'

    name = fields.Char(string='Event Name', required=True)
    description = fields.Html(string='Description')
    event_date = fields.Datetime(string='Event Date')
    location = fields.Char(string='Location')
    image = fields.Binary(string='Image')
    status = fields.Selection([('upcoming', 'Upcoming'), ('past', 'Past')], default='upcoming')
