{
    'name': 'University WPI',
    'version': '1.0',
    'summary': 'Trang web UNIVERSITY WPI với tích hợp CRM, thanh toán, email automation và quản trị nội dung',
    'author': 'Your Company',
    'website': 'https://www.web30s.vn/demo/WPI-Institute-1681?theme=t-default',
    'category': 'Website',
    'depends': ['base', 'website', 'mail', 'payment', 'crm', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/demo_data.xml',
        'views/menu.xml',
        'views/website_templates.xml',
        'views/blog_views.xml',
        'views/event_views.xml',
        'views/about_views.xml',
        'views/contact_views.xml',
        'views/crm_views.xml',
        'views/payment_views.xml',
    ],
    'assets': {
        'point-of-sale._asset_pos': [
            'university_wpi/static/src/**/*',
        ],
    },
    'installable': True,
    'application': True,
}
