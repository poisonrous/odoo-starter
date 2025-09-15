from odoo import api, fields, models

class MusicAlbum(models.Model):
    _name = 'music_album'
    _description = 'Music Album'

    name = fields.Char(
        string='Name',
        required=True
    )

    artist = fields.Many2one(
        'music_artist',
        string='Artist',
        required=True
    )

    tracks = fields.Many2many(
        'music_track',
        string='Tracks'
    )

    release_date = fields.Date(
        string='Release Date',
        copy=False
    )
    
    genre = fields.Many2one(
        'music_genre',
        string='Genre'
    )
    
    length = fields.Float(
        compute='_compute_length',
        string='Length',
        copy=False
    )

    active = fields.Boolean(
        default=True
    )

    status = fields.Selection(
        required=True,
        selection=[('coming','Coming'),('new','New'),('listened','Listened')],
        default='coming',
        copy=False
    )

    @api.depends("tracks")
    def _compute_length(self):
        for record in self:
            for track in self.tracks:
                record.length = record.length + track.length