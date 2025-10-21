{
    'name': 'Media',
    'version': '1.0',
    'summary': 'parent module for media',
    'category': 'Media',
    'description': '',
    'installable': True,
    'application': True,
    'depends': ['base', 'web'],
        'data': [
        'views/media_genre_views.xml',
        'data/cron.xml'
    ]
}