// JavaScript Document
$(document).ready(function() {
						   $('.rules_bttn').click(function() {
														   $(this).fadeOut('fast');
														   $('.content_container').animate({width:"80%"});
														   $('.rules_div').animate({width:"20%"});
														   $('.line').hide();
														   });
						   $('#close_bttn').click(function() {
														    $('.rules_bttn').fadeIn('fast');
														   $('.content_container').css("width","100%");
														   $('.rules_div').css("width","0");
														   $('.line').fadeIn();
														   });
															   
						   
						   
						   
						   });