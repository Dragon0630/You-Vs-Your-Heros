document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and display player stats
    window.fetchPlayerStats = function() {
        fetch('/get_player_stats')
        .then(response => response.json())
        .then(data => {
            const modal = document.getElementById('myModal');
            const modalBody = document.getElementById('modalBody');
            modalBody.innerHTML = ''; // Clear previous data

            // Function to add data to the modal body
            function addDataToModal(label, value) {
                modalBody.innerHTML += `<p><strong>${label}:</strong> ${value}</p>`;
            }

            // Iterate through each key in the data object
            Object.keys(data).forEach(key => {
                const value = data[key];
                if (typeof value === 'object' && value !== null) {
                    // If the value is an object, iterate through its keys
                    addDataToModal(key, ''); // Add a section title for the category
                    Object.keys(value).forEach(subKey => {
                        addDataToModal(subKey, value[subKey]);
                    });
                } else {
                    // If the value is not an object, directly add the data
                    addDataToModal(key, value);
                }
            });

            modal.style.display = "block";
        })
        .catch(error => console.error('Error fetching player stats:', error));
    };

    // Get the modal and close button elements
    const modal = document.getElementById('myModal');
    const close = document.getElementsByClassName("close")[0];

    // Close the modal when the close button (x) is clicked
    close.onclick = function() {
        modal.style.display = "none";
    };

    // Close the modal if the user clicks anywhere outside of the modal content
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});


function startGame(){
    document.getElementById('unityIFrame').style.display = 'block'; // Show the iframe
    document.getElementById('overlay').style.display = 'block'; // Show the overlay
}


function updateHeroImage(heroName) {
    document.getElementById('heroImage').src = 'static/img/${heroName}' + '.jpg'; // Sets the new image path
    document.getElementById('heroImage').alt = heroName; // Updates alt text
}