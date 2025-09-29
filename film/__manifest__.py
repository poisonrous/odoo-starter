{
    'name': 'Film',
    'version': '1.0',
    'summary': 'Films and stuff',
    'category': 'Media',
    'description': '',
    'installable': True,
    'application': True,
    'depends': ['base', 'web', 'media'],
    'data': [
        'security/ir.model.access.csv',
        'views/film_views.xml',
        'views/film_genre_views.xml',
        'views/film_menus.xml'
    ]
}