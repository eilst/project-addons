# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Project Task Shift Timesheet',
    'version': '11.0.1.0.0',
    'author': 'Savoir-faire Linux, Odoo Community Association (OCA)',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'LGPL-3',
    'category': 'Project Management',
    'summary': 'Project Event Shift Timesheet module',
    'depends': [
        'project_event',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'views/project_task_shift_timesheet_view.xml',
        'views/project_task_view.xml'
    ],
    'installable': True,
    'application': False,
}
