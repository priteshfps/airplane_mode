# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words


class PaymentReceipt(Document):
	def before_save(self):
		#frappe.throw("Tes")
		#self.full_name = ' '.join(filter(lambda x: x, [self.first_name,   self.last_name]))
		self.amount_in_words = money_in_words(self.amount, main_currency=None, fraction_currency=None)
		#docci = frappe.get_doc("Contract Invoice", self.contract_invoice)
		#docci.payment_date = self.payment_receipt_date
		#docci.save() 


