from __future__ import unicode_literals
import frappe  

if "module" in frappe.form_dict.keys() and "lesson" in frappe.form_dict.keys():
    current_module = frappe.get_doc("Module", frappe.form_dict["module"])
    current_lesson = frappe.get_doc("Lesson", frappe.form_dict["lesson"])
    data_available = True
else:
    print("no parmas")
    data_available = False

def get_context(context):
    if data_available:
        context.module = current_module
        context.lesson = current_lesson
        context.lesson_list = [lesson.lesson_name for lesson in current_module.lessons]
        context.next_lesson = get_next_lesson(context.lesson_list, context.lesson)
        context.quiz_list = [question.name for question in current_module.quiz]

def get_next_lesson(lesson_list, current_lesson):
    if data_available:
        next_index = lesson_list.index(current_lesson) + 1
        if next_index >= len(lesson_list):
            return None
        else:
            return lesson_list[next_index]