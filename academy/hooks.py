# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "academy"
app_title = "Academy"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = "Website for academy.erpnext.com"
app_icon = "octicon octicon-book"
app_color = "grey"
app_email = "shivam@frappe.io"
app_license = "MIT"
app_version = "0.0.1"


website_context = {
	"repo": "frappe/academy",
	"logo_image_url": '/assets/academy/img/erpnext-logo-blue.png',
	'brand_name': 'Academy',
	"brand_html": "Academy",
	"top_bar_items": [
		{"label": "Discuss", "url": "https://discuss.erpnext.com"},
		{"label": "ERPNext", "url": "https://erpnext.com"}
	],
	"favicon": "/assets/academy/img/erpnext-logo-blue.png"
}

website_redirects = [
	{'source': '/lms', 'target': '/' }
]

home_page = "index"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/academy/css/academy.css"
# app_include_js = "/assets/academy/js/academy.js"

# include js, css files in header of web template
# web_include_css = "/assets/academy/css/academy.css"
# web_include_js = "/assets/academy/js/academy.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "academy.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "academy.install.before_install"
# after_install = "academy.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "academy.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"academy.tasks.all"
# 	],
# 	"daily": [
# 		"academy.tasks.daily"
# 	],
# 	"hourly": [
# 		"academy.tasks.hourly"
# 	],
# 	"weekly": [
# 		"academy.tasks.weekly"
# 	]
# 	"monthly": [
# 		"academy.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "academy.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "academy.event.get_events"
# }

