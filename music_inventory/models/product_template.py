from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = ['product.template']
    album_type = fields.Selection([('cd','CD'), ('vinyl','Vinyl'), ('digital','Digital')], string='Album Type')