# -*- coding: utf-8 -*-

{
    'name': 'Python Odoo Website Assessment',
    'category': 'Website',
    'summary': 'Modifies the website header with an image cover and hamburger menu',
    'depends': ['website'],
    'data': [
        'views/navbar_header.xml',
        'views/image_cover.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_assessment/static/src/scss/navbar_header.scss',
        ],
    },
}
