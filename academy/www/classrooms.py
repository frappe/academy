from __future__ import unicode_literals
import frappe


# Get the classroom's route parameter from the url
url_param = frappe.form_dict["c"]

# Get classroom name from the route
classroom_name = frappe.get_all('Classroom', filters={'route': url_param})[0].name

# Get classroom from classroom_name
current_classroom = frappe.get_doc("Classroom", classroom_name)

def get_context(context):
    context.test = "test"
    context.classroom = frappe.get_doc("Classroom", classroom_name)
    context.module_list, context.module_data = get_modules()

def get_modules():
    module_data = {}
    module_names = [class_module.module_name for class_module in current_classroom.modules]
    classroom_modules = [frappe.get_doc('Module', name) for name in module_names]
    for module_item in classroom_modules:
        module_data[module_item.name] = [lesson.lesson_name for lesson in module_item.lessons]
    return module_names, module_data
