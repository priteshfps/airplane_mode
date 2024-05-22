# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from random import randint, randrange

class AirplaneTicket(Document):
	def before_insert(self):
		seatno = str(randint(1, 99))
		seatno += chr(random.randint(ord('A'), ord('E')))
		self.seat =seatno

	def before_save(self):
	  #pass
		self.set_total_amount()
		
	def set_total_amount(self):
		total_amount = self.flight_price
		for item in self.add_ons:
			total_amount += item.amount
		self.total_amount = total_amount
	
	def validate(self):	 
		docplane  = frappe.get_doc("Airplane Flight", self.flight)
		docairplane = frappe.get_doc("Airplane",docplane.airplane)
		capacity = docairplane.capacity
		
		ticketcount = frappe.db.count("Airplane Ticket", filters={'flight': self.flight})
		if(capacity <= ticketcount):
			frappe.throw("flight exceed the number of seats")
		
		self.set_validate_for_add_ons()
		#pass

	def before_submit(self):
		if (self.status != "Boarded"):
			frappe.throw("you can not submit ticket, ticket status must be boarded.")
	

	def set_validate_for_add_ons(self):
		vadd_ons = []
		for d in self.add_ons:
			if(d.item in vadd_ons):
				self.add_ons.remove(d)
				#frappe.throw("Same add ons cannot be entered multiple times.")
			else:
				vadd_ons.append(d.item)
	
		

