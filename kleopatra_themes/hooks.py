from . import __version__ as app_version

app_name = "kleopatra_themes"
app_title = "Kleopatra Themes"
app_publisher = "Harpiya Software Technologies"
app_description = "Kleopatra Themes"
app_email = "info@harpiya.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kleopatra_themes/css/kleopatra_themes.css"
# app_include_js = "/assets/kleopatra_themes/js/kleopatra_themes.js"

# include js, css files in header of web template
web_include_css = [
    "/assets/kleopatra_themes/libs/tobii/css/tobii.min.css",
    "/assets/kleopatra_themes/libs/tiny-slider/tiny-slider.css",
    "/assets/kleopatra_themes/libs/@iconscout/unicons/css/line.css",
    "/assets/kleopatra_themes/css/icons.min.css",
    "/assets/kleopatra_themes/css/tailwind.min.css",
    ]
web_include_js = [
    "/assets/kleopatra_themes/libs/tiny-slider/min/tiny-slider.js",
    "/assets/kleopatra_themes/libs/tobii/js/tobii.min.js",
    "/assets/kleopatra_themes/libs/feather-icons/feather.min.js",
    "/assets/kleopatra_themes/js/plugins.init.js",
    "/assets/kleopatra_themes/js/app.js",
    "/assets/kleopatra_themes/js/website_utils.js",
    ]

website_route_rules = [
	{"from_route": "/product/<category>", "to_route": "Product"},
]


# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "kleopatra_themes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "kleopatra_themes.utils.jinja_methods",
#	"filters": "kleopatra_themes.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "kleopatra_themes.install.before_install"
# after_install = "kleopatra_themes.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "kleopatra_themes.uninstall.before_uninstall"
# after_uninstall = "kleopatra_themes.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See harpiya.core.notifications.get_notification_config

# notification_config = "kleopatra_themes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "harpiya.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "harpiya.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"kleopatra_themes.tasks.all"
#	],
#	"daily": [
#		"kleopatra_themes.tasks.daily"
#	],
#	"hourly": [
#		"kleopatra_themes.tasks.hourly"
#	],
#	"weekly": [
#		"kleopatra_themes.tasks.weekly"
#	],
#	"monthly": [
#		"kleopatra_themes.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "kleopatra_themes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"harpiya.desk.doctype.event.event.get_events": "kleopatra_themes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Harpiya apps
# override_doctype_dashboards = {
#	"Task": "kleopatra_themes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"kleopatra_themes.auth.validate"
# ]
