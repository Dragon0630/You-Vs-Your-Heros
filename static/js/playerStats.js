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

// Assuming fetchHeroStats() grabs the hero name internally
function fetchHeroStats() {
    const safeheroName = document.getElementById('heroImage').alt;
    const url = `/get_hero_stats/${safeheroName}`;
    fetch(url)
        .then(response => response.json())
        .then(data => displayStats(data))
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


function webgl(){
    var canvas = document.getElementById("myCanvas")
    var gl = canvas.getContext("webgl");

    // WebGL initialization code
    if (!gl) {
        alert("WebGL not supported, please use a WebGL-enabled browser.");
    }

    // Vertex shader program
    var vsSource = `
        attribute vec4 aVertexPosition;

        void main(void) {
            gl_Position = aVertexPosition;
        }
    `;

    // Fragment shader program
    var fsSource = `
        void main(void) {
            gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); // Red color
        }
    `;

    // Initialize shaders
    var vertexShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertexShader, vsSource);
    gl.compileShader(vertexShader);

    var fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragmentShader, fsSource);
    gl.compileShader(fragmentShader);

    // Create shader program
    var shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);
    gl.useProgram(shaderProgram);

    // Set up geometry
    var vertices = [
        0.0,  0.5,  0.0,  // Top vertex
    -0.5, -0.5,  0.0,  // Bottom left vertex
        0.5, -0.5,  0.0   // Bottom right vertex
    ];

    var vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

    // Specify the layout of the vertex buffer
    var positionAttributeLocation = gl.getAttribLocation(shaderProgram, "aVertexPosition");
    gl.enableVertexAttribArray(positionAttributeLocation);
    gl.vertexAttribPointer(positionAttributeLocation, 3, gl.FLOAT, false, 0, 0);

    // Clear the canvas
    gl.clearColor(0.0, 0.0, 0.0, 1.0); // Clear to black, fully opaque
    gl.clear(gl.COLOR_BUFFER_BIT);

    // Draw the triangle
    gl.drawArrays(gl.TRIANGLES, 0, 3);
}

function startGame(){
    document.getElementById('unityIFrame').style.display = 'flex';
}