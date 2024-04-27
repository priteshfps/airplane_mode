# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
#from frappe.website.website_generator import WebsiteGenerator
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def get_context(self,context):
		context.add_breadcrumbs =1
		context.no_cache = 1

		context.parents = [dict(route='/flights',label='Flights')]
	pass