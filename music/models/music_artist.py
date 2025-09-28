from odoo import fields, models

class MusicArtist(models.Model):
    _name = 'music.artist'
    _description = 'Artist'

    name = fields.Char(
        string='Name',
        required=True
    )

    genre_id = fields.Many2one(
        'music.genre',
        string='Genre'
    )

    active = fields.Boolean(
        default=True
    )

    album_ids = fields.One2many(
        'music.album', 'artist_id'
    )


    album_count = fields.Integer(
        compute='_compute_count',
        string='Albums'
    )

    def _compute_count(self):
        for record in self:
            record.album_count = len(record.album_ids)