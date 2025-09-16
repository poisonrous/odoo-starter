from odoo import api, fields, models
from datetime import datetime, time

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

    listened = fields.Boolean(
        default=False
    )

    status = fields.Selection(
        compute='_compute_status',
        inverse='_inverse_status',
        selection=[('coming','Coming'),('new','New'),('listened','Listened')],
        copy=False,
        default='coming'
    )

    @api.depends('tracks')
    def _compute_length(self):
        for record in self:
            record.length = 0.0
            for track in self.tracks:
                record.length = record.length + track.length

    @api.depends('listened', 'release_date')
    def _compute_status(self):
        for record in self:
            if record.listened:
                record.status='listened'
            elif datetime.now() > datetime.combine(record.release_date, time(0,0)):
                record.status='new'
            else:
                record.status='coming'
    def _inverse_status(self):
        for record in self:
            if record.status=='listened':
                record.listened=True
            else:
                record.listened=False

    @api.onchange('artist')
    def _onchange_artist(self):
        self.genre=(self.artist.genre)