// Get the update_header element
const updateHeader = document.getElementById('update_header');

// Add click event listener to update_header
updateHeader.addEventListener('click', function() {
    // Get the header element and update its text
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
}); 