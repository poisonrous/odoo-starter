from odoo import fields, models

class MusicTrack(models.Model):
    _name = 'music_track'
    _description = 'Music Track'

    name = fields.Char(
        string='Name',
        required=True
    )

    artist = fields.Many2many(
        'music_artist',
        string='Artist',
        required=True
    )
    
    length = fields.Float(
        string='Length',
        copy=False,
        required=True
    )

    active = fields.Boolean(
        default=True
    )

    explicit = fields.Boolean(
        default=False
    )

    _sql_constraints = [
        ('positive_length', 'CHECK(length > 0)', 'Track length should be a positive number.')
    ]