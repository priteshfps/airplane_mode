# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tenant(Document):
	def before_save(self):
		#frappe.throw("Tes")
		self.full_name = ' '.join(filter(lambda x: x, [self.first_name,   self.last_name]))
