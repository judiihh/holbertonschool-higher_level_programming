// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Fetch hello translation from the API
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            // Get the hello element and update its text
            const hello = document.getElementById('hello');
            hello.textContent = data.hello;
        })
        .catch(error => console.error('Error:', error)); // Handle any errors that occur during the fetch operation
}); 