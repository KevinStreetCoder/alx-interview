#!/usr/bin/node

const request = require('request');

// Parse command-line arguments
const movieId = process.argv[2];

// Make HTTP GET request to the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie information:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  // Parse the API response
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Make additional requests for each character
  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character information:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
