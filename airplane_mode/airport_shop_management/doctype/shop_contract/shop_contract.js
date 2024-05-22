// Copyright (c) 2024, air and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Contract", {
    setup: function(frm) {
		frm.set_query("shop",  function() {
			return {
				"filters": {
                     "is_available": 1
                    }
			};
		});
	},
	refresh(frm) {

	},
	onload: function(frm)
	{
		//alert(frm.doc.rent_amount!== "undefined");
		//if (frm.doc.rent_amount !== "undefined") 
		//if (!frm.doc.rent_amount ) 
		
		//alert(default_rate);
		if(frm.is_new())
		{
			frappe.db.get_single_value("Global Configuration", "default_rent").then(default_rent => {
				
				console.log(default_rent);
				frm.set_value("rent_amount", default_rent);
			})
			
		}
	}
  
});
