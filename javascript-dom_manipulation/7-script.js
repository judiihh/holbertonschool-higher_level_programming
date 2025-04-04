// Fetch movies data from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        // Get the list_movies element
        const listMovies = document.getElementById('list_movies');
        
        // Loop through each movie and add it to the list
        data.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            listMovies.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error)); 