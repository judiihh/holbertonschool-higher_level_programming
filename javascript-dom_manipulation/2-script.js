// Get the red_header element
const redHeader = document.getElementById('red_header');

// Add click event listener to red_header
redHeader.addEventListener('click', function() {
    // Get the header element and add the red class
    const header = document.querySelector('header');
    header.classList.add('red');
}); 