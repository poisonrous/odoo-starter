from odoo import fields, models

class MusicGenre(models.Model):
    _name = 'music_genre'
    _description = 'Genre'

    name = fields.Char(
        string='Name',
        required=True
    )

    active = fields.Boolean(
        default=True
    )