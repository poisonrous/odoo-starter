from odoo import fields, models

class MusicArtist(models.Model):
    _name = 'music.artist'
    _description = 'Artist'

    partner_id = fields.Many2one(
        'res.partner',
        string='Contact',
        delegate=True,
        required=True,
        ondelete='restrict'
    )

    genre_id = fields.Many2one(
        'music.genre',
        string='Genre'
    )

    active = fields.Boolean(
        default=True
    )

    album_ids = fields.One2many(
        'music.album', 'artist_id'
    )


    album_count = fields.Integer(
        compute='_compute_count',
        string='Albums'
    )

    def _compute_count(self):
        for record in self:
            record.album_count = len(record.album_ids)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    album_ids = fields.One2many(
        'music.album',
        compute='_compute_album_ids',
        string='Albums',
        store=False
    )

    def _compute_album_ids(self):
        for partner in self:
            artist = self.env['music.artist'].search([('partner_id', '=', partner.id)], limit=1)
            partner.album_ids = artist.album_ids if artist else False
