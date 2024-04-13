function modifyJSON() {
    // JSON data
    var name = document.getElementById('name').value;
    var curl = document.getElementById('curl').value;
    var squat = document.getElementById('squat').value;
    var bench = document.getElementById('bench').value;
    var run = document.getElementById('run').value;
    var swim = document.getElementById('swim').value;
    var climb = document.getElementById('climb').value;
    var sprint = document.getElementById('sprint').value;
    var jump = document.getElementById('jump').value;
    var reaction = document.getElementById('reaction').value;
    var newData = {
        name: name,
        strength:{
            curl: curl,
            squat: squat,
            bench: bench
        },
        endurance: {
            run: run,
            swim: swim,
            climb: climb
        },
        agility: {
            sprint: sprint,
            jump: jump,
            reaction, reaction
        }
    };

    // AJAX request to send the data to the server
    fetch('/modify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log('JSON file modified successfully.');
    })
    .catch(error => {
        console.error('There was a problem modifying the JSON file:', error);
    });
}