{
    'name': 'Music',
    'version': '1.0',
    'summary': 'idk, man, I like music',
    'category': 'Music',
    'description': '',
    'installable': True,
    'application': True,
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/music_album_views.xml',
        'views/music_track_views.xml',
        'views/music_artist_views.xml',
        'views/music_genre_views.xml',
        'views/music_playlist_views.xml',
        'views/music_menus.xml'
    ]
}