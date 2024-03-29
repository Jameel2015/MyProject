#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Beneficiary Management System',
    'version': '0.1',
    'summary': 'Beneficiary Managemnet System',
    'description': """Beneficiary Managemnet System (Charity Management System)""",
    'depends': ['base','volunteer_management', 'account'],
    'category': 'management',
    'sequence': 111,
    'data': [
        'security/beneficiary_management_security.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_view.xml',
        'views/extra_models_view.xml',
        'bms_sequence.xml', 
        'views/inherited_views.xml',
        'report_data.xml',
        'report/report_custom.xml',
        'scheduler_data.xml',
        'bms_workflow.xml',
        'views/models_view.xml',
        'views/menu_account.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}