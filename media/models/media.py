from odoo import api, fields, models
from datetime import datetime, time, timedelta

class Media(models.Model):
    _name = 'media'
    _description = 'Media'

    release_date = fields.Date(
        string='Release Date',
        copy=False
    )

    status = fields.Selection(
        compute='_compute_status',
        selection=[('coming','Coming'),('new','New'),('released','Released')],
        copy=False,
        default='coming',
        store=True
    )

    @api.depends('release_date')
    def _compute_status(self):
        for record in self:
            if not record.release_date:
                record.status = 'coming'
                continue

            release_dt = datetime.combine(record.release_date, time(0, 0))
            now = datetime.now()

            if now < release_dt:
                record.status = 'coming'
            elif release_dt <= now <= release_dt + timedelta(days=30):
                record.status = 'new'
            else:
                record.status = 'released'

    def _recompute_status_all(self):
        records = self.search([])
        records._compute_status()