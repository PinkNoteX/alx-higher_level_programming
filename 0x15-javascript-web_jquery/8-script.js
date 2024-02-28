$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (x) {
  for (const y of x.results) {
    $('ul#list_movies').append(`<li>${y.title}</li>`);
  }
});
