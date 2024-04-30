// Copyright (c) 2024, air and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) { 

        //if(frm.doc.seat == null)
        //{ 
            frm.add_custom_button("Assign Seat",() => {
               // frm.add_custom_button("Assign Seat, Gate No.",() => {
            // prompt for single value of any type
            frappe.prompt([{
                label: 'Seat Number',
                fieldname: 'seat',
                fieldtype: 'Data'
                // ,
                // reqd: 1,
                // length: 3
            }
            // ,
            // {
            //     label: 'Gate Number',
            //     fieldname: 'gate',
            //     fieldtype: 'Data'
            //     // ,
            //     // reqd: 1,
            //     // length: 3
            // }
        ], (values) => {
                //console.log(values.seat);
                frm.set_value("seat",values.seat);

                //frm.set_value("gate_no",values.gate);
                frm.save();
            },
            'Select Seat',
            'Assign'
            )

                // frm.set_value("status","Accepted");
                // frm.save();



            },"Action")
 
        //}

	},
    flight_price(frm)
    {
        let total_amount =frm.doc.flight_price
        for(let item of frm.doc.add_ons)
        {
            total_amount+= item.amount
        }
        frm.set_value("total_amount" ,total_amount) 
    }
});


frappe.ui.form.on("Airplane Ticket Add-on Item", {
	 

    amount(frm,cdt,cdn)
    {
        let total_amount =frm.doc.flight_price
        for(let item of frm.doc.add_ons)
        {
            total_amount+= item.amount
        }
        frm.set_value("total_amount" ,total_amount) 
    },
});
