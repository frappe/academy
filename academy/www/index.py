from __future__ import unicode_literals
import frappe

def get_context(context):
    context.featured = frappe.get_all('Classroom', filters={'make_featured': 1}, fields=['class_name', 'short_description', 'intro_video', 'hero_image', 'route'])