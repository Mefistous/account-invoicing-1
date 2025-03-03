##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
    'name': 'Account Invoice Move Currency',
    'version': '12.0.1.0.0',
    'author': 'ADHOC SA',
    'category': 'Accounting & Finance',
    'depends': [
        'account_ux'
    ],
    'data': [
        'views/account_invoice_views.xml',
        'wizards/account_change_currency_views.xml',
    ],
    'demo': [
        'demo/account_invoice_demo.yml',
    ],
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'installable': False,
    'auto_install': False,
    'application': False
}
