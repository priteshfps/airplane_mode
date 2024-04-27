// Copyright (c) 2024, air and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) { 

        if(frm.doc.seat == null)
        { 
            frm.add_custom_button("Assign Seat",() => {
                
            // prompt for single value of any type
            frappe.prompt({
                label: 'Seat Number',
                fieldname: 'seat',
                fieldtype: 'Data',
                reqd: 1,
                length: 3
            }, (values) => {
                console.log(values.seat);
                frm.set_value("seat",values.seat);
                frm.save();
            },
            'Select Seat',
            'Assign'
            )

                // frm.set_value("status","Accepted");
                // frm.save();



            },"Action")
 
        }

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
// frappe.ui.form.on('Airplane Ticket Add-on Item', {
//     duplicate_field_name: function(frm, cdt, cdn) {
//         var d = locals[cdt][cdn];
//         $.each(frm.doc.table_name, function(i, row) {
//             if (row.duplicate_field_name === d.duplicate_field_name && row.name != d.name) {
//                frappe.msgprint('You added already exists on the table.');
//                frappe.model.remove_from_locals(cdt, cdn);
//                frm.refresh_field('table_name');
//                return false;
//             }
//         });
//     }
// });

// frappe.ui.form.on("Vehicle Item", {
//     vehicle_items_add: function(frm, cdt, cdn) {
//         $.each(locals[cdt][cdn].vehicle_items, function(row) {
//             if (row.vehicle_item === cdt.vehicle_item) {
//                 frappe.msgprint({
//                     title: __('Duplicated Item'),
//                     indicator: 'red',
//                     message: __('The item you added already exist in the table.')
//                 });
//                 frappe.model.delete_doc(cdt, cdn);
//frappe.model.delete_doc(cdt, cdn);
//                 frm.refresh_field('vehicle_items');
//                 return false;
//             }
//         });
//     }
// });

// // change Parent DocType
// frappe.ui.form.on('Parent DocType', {
//     validate: function (frm) {
//       var existingValues = [];
//       var duplicatesFound = false;
  
//       // change child_table . Iterate through the child table rows
//       frm.doc.child_table.forEach(function (row) {
//          // change unique_field
//         var fieldValue = row.unique_field;
  
//         if (existingValues.indexOf(fieldValue) !== -1) {
//           // Duplicate value found
//           duplicatesFound = true;
//           frappe.msgprint(__('Duplicate value in child table: {0}', [fieldValue]));
//           frappe.validated = false; // Prevent saving
//           return false; // Exit the loop
//         }
  
//         existingValues.push(fieldValue);
//       });
  
//       if (!duplicatesFound) {
//         frappe.validated = true; // No duplicates found, allow saving
//       }
//     },
//   });