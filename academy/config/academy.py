from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Academy Settings"),
			"items": [
				{
					"type": "doctype",
					"name": "Academy Settings",
				}
			]
		}
	]
