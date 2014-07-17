/* Are the Dash Playing Global JS */
/* Copyright The Variable */
/* Author: Patrick Beeson, pbeeson@thevariable.com */

// Open ticket URL in new window
$('.ticket_push a').attr("target", "_blank");

// Get current year and place in copyright
$(document).ready(function() {
	var currentYear = (new Date).getFullYear();
	$("#year").text( (new Date).getFullYear() );
});

// Track clicks to the ticket URL in GA
$('.ticket_push a').on('click', function() {
  ga('send', 'event', 'ticket_push', 'click', 'engagement', 10);
});