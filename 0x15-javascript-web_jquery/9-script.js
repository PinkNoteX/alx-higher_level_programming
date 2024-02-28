$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (x) {
  $('DIV#hello').text(x.hello);
});
