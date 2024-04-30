# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirportShop(WebsiteGenerator):
	website = frappe._dict(
		condition_field = "is_available", 
    )

	def get_context(self,context):
		context.add_breadcrumbs =1
		context.no_cache = 1

		context.parents = [dict(route='/shops',label='Shops')]
	
	# """select s.name from `tabAirport Shop` s  left join `tabShop Contract` c on s.name= c.shop and c.date_of_expiry >  CURDATE() 
	# 		where s.is_available =0 and c.shop IS NOT NULL ;""",
	
	
	
	pass




