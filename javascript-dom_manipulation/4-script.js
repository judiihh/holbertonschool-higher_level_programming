// Get the add_item element
const addItem = document.getElementById('add_item');

// Add click event listener to add_item
addItem.addEventListener('click', function() {
    // Get the my_list element
    const myList = document.querySelector('.my_list');
    
    // Create new list item
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    
    // Add the new item to the list
    myList.appendChild(newItem);
}); 