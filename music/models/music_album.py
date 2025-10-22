from odoo import api, fields, models
from datetime import datetime, time, timedelta

class MusicAlbum(models.Model):
    _name = 'music.album'
    _description = 'Music Album'
    _inherit = ['media']

    name = fields.Char(
        string='Name',
        required=True
    )

    artist_id = fields.Many2one(
        'music.artist',
        string='Artist',
        required=True
    )

    artist_album_count = fields.Integer(
        related='artist_id.album_count',
        string='Artist Album Count',
        readonly=True
    )

    track_link_ids = fields.One2many(
        'music.track.link',
        'album_id',
        string='Tracks'
    )
    
    genre_id = fields.Many2one(
        'music.genre',
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

    @api.depends('track_link_ids.track_id.length')
    def _compute_length(self):
        for record in self:
            record.length = 0.0
            record.length = sum(link.track_id.length for link in record.track_link_ids if link.track_id)

    @api.onchange('artist_id')
    def _onchange_artist(self):
        self.genre_id=(self.artist_id.genre_id)

    def action_add(self):
        self._compute_status()