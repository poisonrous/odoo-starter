from odoo import fields, models

class MusicAlbum(models.Model):
    _name = 'music_album'
    _description = 'Music Album'

    name = fields.Char(
        string='Name',
        required=True
    )
    artist = fields.Char(
        string='Artist',
        required=True
    )
    release_date = fields.Date(
        string='Release Date',
        copy=False
    )
    genre = fields.Selection(
        string='Genre',
        selection=[('pop','Pop'),('rock','Rock'),('country','Country')],
        default='pop'
    )
    
    length = fields.Float(
        string='Length',
        copy=False
    )

    active = fields.Boolean(
        default=True
    )

    status = fields.Selection(
        required=True,
        selection=[('coming','Coming'),('new','New'),('listened','Listened')],
        default='coming',
        copy=False
    )