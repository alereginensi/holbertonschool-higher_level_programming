// script that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (character) {
  $('DIV#character').append(character.name);
});
