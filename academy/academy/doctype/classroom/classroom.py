# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

# For
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class Classroom(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/class.html",
		condition_field = "publish",
		page_title_field = "class_name",
	)

	def get_module_names(self):
		return [class_module.module_name for class_module in self.modules]
	
	def get_classroom_modules(self):
		module_names = self.get_module_names()
		module_list = []
		module_data = {}

		for name in module_names:
			module_list.append(frappe.get_doc('Module',name))

		for module_item in module_list:
			module_data[module_item.name] = [lesson.lesson_name for lesson in module_item.lessons]
		
		return module_list, module_data

	def get_context(self, context):
		context.module_list, context.module_data = self.get_classroom_modules()
		context.mock_content = ["Introduction to ERPNext", "Setting up your company"]
		context.mock_route = "classrooms/module"