// script that fetches and lists the title for all movies by using this URL
// https://swapi-api.hbtn.io/api/films/?format=json

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movie) {
  const movies = movie.results;
  for (const x in movies) {
    $('UL#list_movies').append('<li>' + movies[x].title + '</li>');
  }
});
