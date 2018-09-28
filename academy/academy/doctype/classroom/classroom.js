// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Classroom', {
	class_name(frm) {
		cur_frm.fields_dict.route.set_value(cur_frm.fields_dict.class_name.value.replace(/ /g,"-").toLowerCase())
	}
	// refresh: console.log,
	// modules: function(doc, cdt, cdn) {
	// 	console.log(cdt)
	// 	console.log(cdn)
	// 	console.log(doc)
	// 	console.log('stupid')
	// },
	// description: console.log,
});

// frappe.ui.form.on('Classroom Module Map', {
// 	is_published(frm) {
// 		cur_frm.doc.modules[0].publish_date = new Date()
// 		cur_frm.refresh_field("modules")
// 	}
// })