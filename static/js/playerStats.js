document.addEventListener('DOMContentLoaded', function() {
    setupModalInteractions();
    setupButtonListeners();
});

function setupModalInteractions() {
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
}



function setupButtonListeners() {
    const playerStatsBtn = document.getElementById('player_stat');
    const heroStatsBtn = document.getElementById('hero_stat');

    if (playerStatsBtn) {
        playerStatsBtn.addEventListener('click', fetchPlayerStats);
    }
    if (heroStatsBtn) {
        heroStatsBtn.addEventListener('click', function() {
            const heroName = document.getElementById('heroImage').alt; // Assuming the hero name is stored in the alt text of the hero image
            fetchHeroStats(heroName);
        });
    }
}

function fetchPlayerStats() {
    fetch('/get_player_stats')
        .then(response => response.json())
        .then(data => {
            displayStats(data);
        })
        .catch(error => console.error('Error fetching player stats:', error));
}

function fetchHeroStats(heroName) {
    fetch('/get_hero_stats/${heroName}')
        .then(response => response.json())
        .then(data => {
            displayStats(data);
        })
        .catch(error => console.error('Error fetching hero stats:', error));
}

heroStatsBtn.addEventListener('click', function() {
    const heroName = document.getElementById('heroImage').alt; // This needs to match exactly with the JSON filenames
    fetchHeroStats(heroName);
});

function displayStats(data) {
    const modal = document.getElementById('myModal');
    const modalBody = document.getElementById('modalBody');
    modalBody.innerHTML = ''; // Clear previous data

    Object.keys(data).forEach(key => {
        const value = data[key];
        if (typeof value === 'object' && value !== null) {
            modalBody.innerHTML += `<p><strong>${key}:</strong></p>`; // Add a section title for the category
            Object.keys(value).forEach(subKey => {
                modalBody.innerHTML += `<p>${subKey}: ${value[subKey]}</p>`; // Display each stat
            });
        } else {
            modalBody.innerHTML += `<p><strong>${key}:</strong> ${value}</p>`; // Display scalar values directly
        }
    });

    modal.style.display = "block";
}
