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

    line_ids = fields.One2many(
        "music_artist_line", "model_id"
    )

    album_count = fields.Integer(
        compute='_compute_count',
        string='Albums'
    )

    def _compute_count(self):
        for record in self:
            record.count = len(record.album_ids)

class MusicArtistLine(models.Model):
    _name = 'music_artist_line'
    _description = 'Music Artist Line'
    model_id = fields.Many2one('music_artist')

    name = fields.Char(
        related = 'music_album.name'
    )