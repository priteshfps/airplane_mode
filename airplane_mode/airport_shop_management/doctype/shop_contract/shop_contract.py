# Copyright (c) 2024, air and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, today, getdate, add_months, get_datetime, now,add_to_date 
from datetime import datetime, timedelta


class ShopContract(Document):
	
	def validate(self):
		if(self.start_date > self.date_of_expiry):
			frappe.throw("Expiry date must be more than start date")
		#self.Insert_ContractInvoice()
	#pass
	def on_submit(self):
		self.Insert_ContractInvoice()
		docshop = frappe.get_doc("Airport Shop", self.shop)
		docshop.is_available = 0
		docshop.save()
		
	def Insert_ContractInvoice(self):
		try:
			invoice_startdate = getdate(self.start_date)
			invoice_Enddate = getdate(self.date_of_expiry)
			#frappe.msgprint(str(invoice_startdate.month))
			days = invoice_startdate.day
			#frappe.msgprint(str(invoice_startdate.day))
			invdate =   add_to_date(invoice_startdate, days=days*-1,months=1, as_datetime=True)
			#frappe.msgprint(str(self.name))
			while invdate <=  invoice_Enddate:
				nameseries = "CI-"+self.shop+invdate.strftime('-%y%m-')+""
				#frappe.msgprint( nameseries)
				contract_invoice = frappe.get_doc(
					dict(
						doctype="Contract Invoice",
						contract=self.name,
						contract_invoice_date=invdate,
						amount=self.rent_amount,
						shop=self.shop,
						tenant=self.tenant,
						naming_series=nameseries,
						)
						).insert()
				contract_invoice.submit()	
				nextdate =  add_to_date(invdate,  months=1, as_datetime=True)
				nextdate= self.last_day_of_month(nextdate)
				#invdate =  nextdate, 
				if nextdate < invoice_Enddate: 
					invdate = nextdate
				elif nextdate.month == invoice_Enddate.month:
					invdate = invoice_Enddate
				else:
					break
		except Exception as e:
			frappe.msgprint( str(e))
	def last_day_of_month(self,date):
		if date.month == 12:
			return date.replace(day=31)
		return date.replace(month=date.month+1, day=1) - timedelta(days=1)

	#yesterday = add_days(today(), -1)
	
