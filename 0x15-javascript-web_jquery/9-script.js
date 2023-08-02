$(document).ready(function () {
	$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
		$("DIV#hello").text(data.hello);
	});
});
