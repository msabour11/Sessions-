from odoo import api, fields, models


class AccademyWizard(models.TransientModel):
    _name = 'accademy.wizard'
    _description = 'quick registration of academy attendee'

    def _default_session(self):
        return self.env['accademy.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('accademy.session', string='Session', default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    def add_attendee(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}
