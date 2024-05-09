# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		#if not self.last_name:
		#	frappe.throw("Last name is required")
		#self.full_name = f"{self.first_name} {self.last_name}"
		# self.full_name = f"{self.first_name}" +  str(self.last_name or "") 
		self.full_name = ' '.join(filter(lambda x: x, [self.first_name,   self.last_name]))