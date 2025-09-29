from odoo import fields, models

class Film(models.Model):
    _name = 'film'
    _description = 'Film'
    _inherit = ['media']

    name = fields.Char(
        string='Title',
        required=True
    )

    genre_id = fields.Many2one(
        'film.genre',
        string='Genre'
    )

    length = fields.Float(
        string='Length',
        required=True
    )

    active = fields.Boolean(
        default=True
    )