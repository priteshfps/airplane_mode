import frappe
from frappe import _  

@frappe.whitelist()
def CheckContract_SetAvailable():
	for d in frappe.db.sql(
		"""select s.name from `tabAirport Shop` s  left join `tabShop Contract` c on s.name= c.shop and c.date_of_expiry >  CURDATE() 
			where s.is_available =0 and c.shop IS  NULL ; """,
		as_dict=1,
	):
		docshop = frappe.get_doc("Airport Shop", d)
		docshop.is_available = 1
		docshop.save()

@frappe.whitelist()
def send_Payment_Reminder_email_to_tenant():
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

