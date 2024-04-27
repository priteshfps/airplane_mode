// Copyright (c) 2024, air and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if(frm.doc.website != null )
        {  
            cur_frm.add_web_link(frm.doc.website,"Visit Website");
        }
	},
});
