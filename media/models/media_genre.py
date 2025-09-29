from odoo import fields, models

class MediaGenre(models.Model):
    _name = 'media.genre'
    _description = 'Genre'

    name = fields.Char(
        string='Name',
        required=True
    )

    active = fields.Boolean(
        default=True
    )