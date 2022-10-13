// Copyright (c) 2022, Harpiya Software Technologies
// MIT License. See license.txt

harpiya.ready(function() {

	if(harpiya.utils.get_url_arg('subject')) {
	  $('[name="subject"]').val(harpiya.utils.get_url_arg('subject'));
	}

	$('.btn-send').off("click").on("click", function() {
		var email = $('[name="email"]').val();
		var message = $('[name="message"]').val();

		if(!(email && message)) {
			harpiya.msgprint('{{ _("Please enter both your email and message so that we can get back to you. Thanks!") }}');
			return false;
		}

		if(!validate_email(email)) {
			harpiya.msgprint('{{ _("You seem to have written your name instead of your email. Please enter a valid email address so that we can get back.") }}');
			$('[name="email"]').focus();
			return false;
		}

		$("#contact-alert").toggle(false);
		harpiya.send_message({
			subject: $('[name="subject"]').val(),
			sender: email,
			message: message,
			callback: function(r) {
				if(r.message==="okay") {
					harpiya.msgprint('{{ _("Thank you for your message") }}');
				} else {
					harpiya.msgprint('{{ _("There were errors") }}');
					console.log(r.exc);
				}
				$(':input').val('');
			}
		}, this);
		return false;
	});

});

var msgprint = function(txt) {
	if(txt) $("#contact-alert").html(txt).toggle(true);
}
