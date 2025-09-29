from odoo import models

class MusicGenre(models.Model):
    _name = 'music.genre'
    _description = 'Genre'
    _inherit = ['media.genre']
