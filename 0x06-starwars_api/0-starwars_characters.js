#!/usr/bin/node
const request = require('request');

const filmID = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmID;

request(endpoint, (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((urlCharacter) => {
    request(urlCharacter, (err, res, charBody) => {
      if (err) {
        console.error('Error fetching character:', err);
        return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
