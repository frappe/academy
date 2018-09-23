import frappe


def get_context(context):
    context.courses = frappe.get_all("Course", fields="name", order_by="name")