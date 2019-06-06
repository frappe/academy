# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Academy",
			"category": "Modules",
			"label": _("Academy"),
			"color": "#1abc9c",
			"icon": "fa fa-check-square-o",
			"type": "module",
			"disable_after_onboard": 1,
			"description": "Configure ERPNext Academy.",
			"onboard_present": 0
		},
	]
