$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (x) {
  $('div#character').text(x.name);
});
