#!/usr/bin/node

const rp = require('request-promise');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

async function getCharacterNames (characters) {
  const characterNames = [];
  for (const characterUrl of characters) {
    try {
      const character = await rp({ uri: characterUrl, json: true });
      characterNames.push(character.name);
    } catch (error) {
      console.error('Error fetching character:', error);
    }
  }
  return characterNames;
}

async function main () {
  try {
    const movie = await rp({ uri: url, json: true });
    const characters = movie.characters;
    const characterNames = await getCharacterNames(characters);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error('Error fetching movie:', error);
  }
}

main();
