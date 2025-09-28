from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MusicTrackLink(models.Model):
    _name = 'music.track.link'
    _description = 'Track Link (Playlist or Album)'
    _order = 'sequence'

    track_id = fields.Many2one(
        'music.track',
        string='',
        required=True,
        ondelete='cascade'
    )

    playlist_id = fields.Many2one(
        'music.playlist',
        string='Playlist',
        ondelete='cascade'
    )

    album_id = fields.Many2one(
        'music.album',
        string='Album',
        ondelete='cascade'
    )

    sequence = fields.Integer(
        string=''
    )

    @api.model
    def create(self, vals):
        if 'sequence' not in vals or vals['sequence'] == 0:
            domain = []
            if vals.get('playlist_id'):
                domain = [('playlist_id', '=', vals['playlist_id'])]
            elif vals.get('album_id'):
                domain = [('album_id', '=', vals['album_id'])]

            last = self.search(domain, order='sequence desc', limit=1)
            vals['sequence'] = last.sequence + 1 if last else 1

        return super(MusicTrackLink, self).create(vals)

    @api.constrains('album_id', 'track_id')
    def _check_duplicate(self):
        for record in self:
            if self.search([('album_id', '=', record.album_id.id),
            ('track_id', '=', record.track_id.id), ('id', '!=', record.id)]):
                raise ValidationError("You can't have a song twice in an album.")
