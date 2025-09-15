from odoo import fields, models

class MusicArtist(models.Model):
    _name = 'music_artist'
    _description = 'Artist'

    name = fields.Char(
        string='Name',
        required=True
    )

    genre = fields.Many2one(
        'music_genre',
        string='Genre'
    )

    active = fields.Boolean(
        default=True
    )