from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Accademy(models.Model):
    _name = 'accademy.accademy'
    _description = 'accademy.accademy'

    name = fields.Char(string='course name', required=True)
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    active = fields.Boolean(string='Active', default=True)
    resposible_id = fields.Many2one('res.users', string='Responsible', ondelete='set null')
    session_ids = fields.One2many('accademy.session', 'course_id', string='Sessions')


class Session(models.Model):
    _name = 'accademy.session'
    _description = 'accademy.session'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Session name')
    start_date = fields.Date(default=fields.Date.today, string='Start Date')
    active = fields.Boolean(string='Active', default=True)
    duration = fields.Float(digits=(6, 2), help='Duration in hours')
    seats = fields.Integer(string='Number of Seats')
    course_id = fields.Many2one('accademy.accademy', string='Course', ondelete='cascade', required=True)
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    taken_seats = fields.Float(string='Taken Seats', compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=1, compute="_get_end_date", inverse="_set_end_date")
    attendees_count = fields.Integer(string='Number of Attendees', store=True, compute="_get_attendees_count")

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for rec in self:
            if not rec.seats:
                rec.taken_seats = 0
            else:
                rec.taken_seats = 100 * (len(rec.attendee_ids) / rec.seats)

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': 'Seats value error',
                    'message': 'The number of seats must be greater than 0 !'
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': 'Too many attended',
                    'message': 'Seats less than the number of attended'
                }
            }

    @api.constrains('instructor_id')
    def _check_instructor_attendence(self):
        for rec in self:
            if rec.instructor_id:
                if rec.instructor_id in rec.attendee_ids:
                    raise ValidationError("This can not be instructor !")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for rec in self:
            if rec.start_date and rec.duration:
                duration = timedelta(days=rec.duration, seconds=-1)
                rec.end_date = rec.start_date + duration
            else:
                rec.end_date = rec.start_date

    def _set_end_date(self):
        for rec in self:
            if rec.end_date and rec.start_date:
                rec.duration = (rec.end_date - rec.start_date).days

            else:
                continue

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_ids)

    #action add attendee within wizard
    def open_attendee_wizard(self):
        print(self)
        return {
            'name': 'add Attende',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'accademy.wizard',
            'target': 'new',
            'context': {'attendee_context_id': self.id},
        }
