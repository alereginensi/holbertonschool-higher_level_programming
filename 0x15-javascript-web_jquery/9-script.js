// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').append(data.hello);
});
