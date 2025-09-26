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

    album_ids = fields.One2many(
        'music_album', 'artist'
    )


    album_count = fields.Integer(
        compute='_compute_count',
        string='Albums'
    )

    def _compute_count(self):
        for record in self:
            record.count = len(record.album_ids)