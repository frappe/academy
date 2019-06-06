from __future__ import unicode_literals
import frappe

def get_context(context):
	context.academy = frappe.get_single("Academy Settings")