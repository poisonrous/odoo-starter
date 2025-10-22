from odoo import models

class MusicAlbum(models.Model):
    _inherit = ['music.album']

    def action_add(self):
        return self.env['product.product'].create({
            'name': self.name,
            'type': 'product',
            'list_price': '7000.00',
            'standard_price': '5000.00',
        })