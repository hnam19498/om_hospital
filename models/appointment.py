from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender', string='Gender')
    appointment_time = fields.Datetime(string='Appointment time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very high')], string='Priority')
    state = fields.Selection(
        [('draft', 'Draft'), ('in_consultation', 'In consultation'), ('done', 'Done'), ('cancel', 'Cancel')],
        default='draft', required=True, string='Status')
    doctor_id = fields.Many2one('res.users', string='Doctor')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print('Button clicked!!!')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "ahihi",
                'type': "rainbow_man",
            }
        }
