// Fetch character data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        // Get the character element and update its text
        const character = document.getElementById('character');
        character.textContent = data.name;
    })
    .catch(error => console.error('Error:', error)); 