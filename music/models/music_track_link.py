from odoo import api, fields, models

class MusicTrackLink(models.Model):
    _name = 'music_track_link'
    _description = 'Track Link (Playlist or Album)'
    _order = 'sequence'

    track_id = fields.Many2one(
        'music_track',
        string='Track',
        required=True,
        ondelete='cascade'
    )

    playlist_id = fields.Many2one(
        'music_playlist',
        string='Playlist',
        ondelete='cascade'
    )

    album_id = fields.Many2one(
        'music_album',
        string='Album',
        ondelete='cascade'
    )

    sequence = fields.Integer(
        string='..'
    )

"""    @api.model
    def create(self, vals_list):
        new_vals_list = []
        for vals in vals_list:
            if not isinstance(vals, dict):
                continue
            domain = []
            if vals.get('playlist_id'):
                domain = [('playlist_id', '=', vals['playlist_id'])]
            elif vals.get('album_id'):
                domain = [('album_id', '=', vals['album_id'])]
            last = self.search(domain, order='sequence desc', limit=1)
            vals['sequence'] = last.sequence + 1 if last else 1
            new_vals_list.append(vals)
        return super().create(new_vals_list)"""