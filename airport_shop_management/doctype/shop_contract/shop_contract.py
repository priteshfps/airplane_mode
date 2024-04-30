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
			frappe.msgprint(str(self.name))
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
	send_rent_reminder = frappe.db.get_single_value("Global Configuration", "send_rent_reminder")
	if (send_rent_reminder):
		data= frappe.db.sql(
			"""select t.full_name ,t.email,s.name,ci.name ciname,ci.contract, ci.contract_invoice_date,ci.amount,LAST_DAY(CURRENT_DATE)  from `tabContract Invoice` ci inner join
			`tabAirport Shop` s on s.name = ci.shop inner join `tabTenant` t on t.name = ci.tenant  left join `tabPayment Receipt` pr on ci.name = pr.contract_invoice where ci.contract_invoice_date <=
			LAST_DAY(CURRENT_DATE) and pr.amount is null ; 
			""",
			as_dict=1,
		)

		for d in data:
			
			message = (
			_("Hello {0},").format(d.full_name)
			+ "<br><br>"
			+ _("Reminder for shop contract payment due of contract No. : {0}").format(
				d.contract
			)
			+ "."
			+ "<br><br>"
			+ _(" you have pending amount : {0} ,  against contract invoice# : {1} for the shop : {2}. invoice date is {3}").format(
				d.amount,d.ciname,d.name,d.contract_invoice_date
			)
			+ "."
			+ "<br><br>"
			+ _("Please pay earliest to avoid penalty charges ")
			)
			frappe.sendmail(
				recipients=d.email,
				subject=_("Reminder for Rent Due of contract - {0}").format(d.contract),
				message=message,
			)

