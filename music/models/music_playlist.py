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

    tracks = fields.Many2many(
        'music_track',
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

    @api.depends('tracks')
    def _compute_length(self):
        for record in self:
            record.length = 0.0
            for track in self.tracks:
                record.length = record.length + track.length

    def action_randomize(self):
        for record in self:
            random.shuffle(self.tracks)