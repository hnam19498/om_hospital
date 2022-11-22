# -*- coding: utf-8 -*-
{
    'name': 'Hospital',
    'application': True,
    'auto_install': False,
    'author': "hnam",
    'sequence': -100,
    'version': '2.0',
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/patient_tag_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'license': 'LGPL-3',
}
