# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "training"
app_title = "Training"
app_publisher = "Frappe"
app_description = "ERPNext Training App"
app_icon = "octicon octicon-book"
app_color = "grey"
app_email = "info@frappe.io"
app_license = "MIT"

website_context = {
	"brand_html": "<img class='mr-2 d-inline-block align-top' src='/assets/training/img/erpnext-logo-blue.svg' />ERPNext Academy",
	"top_bar_items": [
		{"label": "Classrooms", "right":1, "child_items": [
			{"label": "ERPNext Expert", "url":"/classrooms/expert-user"},
			{"label": "ERPNext Developer", "url":"/classrooms"},
			{"label": "ERPNext Implementer", "url":"/classrooms"},
		]},
		{"label": "Enroll", "url": "/enroll", "right":1},
		{"label": "About", "url": "/about", "right":1},
        # {"label": "Login", "url": "/login", "right":1},
	],
	"hide_login": 1,
	"favicon": "/assets/training/img/erpnext-logo-blue.png"
}

website_redirects = [
	{'source': '/blog', 'target': 'https://frappe.io/blog' },
	{'source': '/about', 'target': 'https://erpnext.com/about' },
	{'source': '/features', 'target': '/learn' },
	{'source': '/download', 'target': 'https://erpnext.org/get-started' },
	{'source': '/faq', 'target': 'https://erpnext.org/faq' },
	{'source': '/open-source', 'target': 'https://erpnext.org/open-source' },
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/training/css/training.css"
# app_include_js = "/assets/training/js/training.js"

# include js, css files in header of web template
# web_include_css = "/assets/training/css/training.css"
# web_include_js = "/assets/training/js/training.js"

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
# get_website_user_home_page = "training.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "training.install.before_install"
# after_install = "training.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "training.notifications.get_notification_config"

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
# 		"training.tasks.all"
# 	],
# 	"daily": [
# 		"training.tasks.daily"
# 	],
# 	"hourly": [
# 		"training.tasks.hourly"
# 	],
# 	"weekly": [
# 		"training.tasks.weekly"
# 	]
# 	"monthly": [
# 		"training.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "training.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "training.event.get_events"
# }

