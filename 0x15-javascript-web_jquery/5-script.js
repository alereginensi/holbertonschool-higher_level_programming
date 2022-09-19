// script that adds a <li> element to a list when the user clicks on the tag DIV#add_item
// https://www.tutorialrepublic.com/faq/how-to-add-li-in-an-existing-ul-using-jquery.php

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
