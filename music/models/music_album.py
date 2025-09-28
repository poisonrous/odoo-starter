from odoo import api, fields, models
from datetime import datetime, time

class MusicAlbum(models.Model):
    _name = 'music.album'
    _description = 'Music Album'

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
        store=True,
        readonly=True
    )

    track_link_ids = fields.One2many(
        'music.track.link',
        'album_id',
        string='Tracks'
    )

    release_date = fields.Date(
        string='Release Date',
        copy=False
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

    listened = fields.Boolean(
        default=False
    )

    status = fields.Selection(
        compute='_compute_status',
        inverse='_inverse_status',
        selection=[('coming','Coming'),('new','New'),('listened','Listened')],
        copy=False,
        default='coming',
        store=True
    )

    @api.depends('track_link_ids.track_id.length')
    def _compute_length(self):
        for record in self:
            record.length = 0.0
            record.length = sum(link.track_id.length for link in record.track_link_ids if link.track_id)

    @api.depends('listened', 'release_date')
    def action_listened(self):
        for record in self:
            record.listened=True

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

    @api.onchange('artist_id')
    def _onchange_artist(self):
        self.genre_id=(self.artist_id.genre_id)