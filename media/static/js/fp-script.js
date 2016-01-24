// JavaScript Document
$(document).ready(function() {
						 var height=$('.contentA').outerHeight();
						 var scrollTop=$(window).scrollTop();
						 $('.rules_bt').click(function() {
													   $('html,body').stop().animate({scrollTop:height});
													   });
						 $('.prizes_bt').click(function() {
													   $('html,body').stop().animate({scrollTop:height*2});
													   });
						 
						   });
																 