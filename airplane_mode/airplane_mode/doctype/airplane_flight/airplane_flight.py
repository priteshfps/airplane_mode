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
	def on_update(self):
		
		if(self.has_value_changed("gate_no") ):
			
			airplanetickets = frappe.get_all('Airplane Ticket', 'name',
			dict(flight=self.name ) )
			
			for airticket in airplanetickets:
				frappe.db.set_value("Airplane Ticket", airticket.name, "gate_no", self.gate_no)
				
			frappe.db.commit()
				
	def on_submit(self):
		self.status = "Completed"



	pass
	