from odoo import api, fields, models
from datetime import datetime, time
import random

class MusicPlaylist(models.Model):
    _name = 'music_playlist'
    _description = 'Music Playlist'

    name = fields.Char(
        string='Name',
        required=True
    )

    track_link_ids = fields.One2many(
        'music_track_link',
        'playlist_id',
        string='Tracks'
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

    def action_randomize(self):
        for record in self:
            shuffled_links = random.sample(record.track_link_ids, len(record.track_link_ids))
            for i, link in enumerate(shuffled_links):
                link.sequence = i