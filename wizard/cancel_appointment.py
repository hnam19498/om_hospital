from odoo import fields, models, api


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    apopointment_id = fields.Many2one('hospital.appointment', string='Appointment')
