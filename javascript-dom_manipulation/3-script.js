// Get the toggle_header element
const toggleHeader = document.getElementById('toggle_header');

// Add click event listener to toggle_header
toggleHeader.addEventListener('click', function() {
    // Get the header element
    const header = document.querySelector('header');
    
    // Toggle between red and green classes
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
}); 