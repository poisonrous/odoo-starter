from odoo import models

class FilmGenre(models.Model):
    _name = 'film.genre'
    _description = 'Genre'
    _inherit = ['media.genre']