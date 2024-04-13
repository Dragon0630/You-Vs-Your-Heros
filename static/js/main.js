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
    window.location.href='/comparison';
}

var currentTab = 0;
function nextClick(){
    switch(currentTab){
        case 0:
            document.getElementById('navButtons').style.justifyContent = 'none';
            document.getElementById('nameFields').style.display = 'none';
            document.getElementById('Strength').style.display = 'flex';
            document.getElementById('back_button').style.display = 'flex';
            break;
        case 1:
            document.getElementById('Strength').style.display = 'none';
            document.getElementById('Endurance').style.display = 'flex';
            break;
        case 2:
            document.getElementById('Endurance').style.display = 'none';
            document.getElementById('Agility').style.display = 'flex';
            document.getElementById('submit_button').style.display = 'flex';
            document.getElementById('next_button').style.display = 'none';
            break;
        default:
            break;
    }
    currentTab++;
}

function backClick(){
    currentTab--;
    switch(currentTab){
        case 0:
            document.getElementById('nameFields').style.display = 'flex';
            document.getElementById('Strength').style.display = 'none';
            document.getElementById('back_button').style.display = 'none';
            break;
        case 1:
            document.getElementById('nameFields').style.display = 'none';
            document.getElementById('Strength').style.display = 'flex';
            document.getElementById('back_button').style.display = 'flex';
            document.getElementById('Endurance').style.display = 'none';
            break;
        case 2:
            document.getElementById('Strength').style.display = 'none';
            document.getElementById('Endurance').style.display = 'flex';
            document.getElementById('Agility').style.display = 'none';
            document.getElementById('submit_button').style.display = 'none';
            document.getElementById('next_button').style.display = 'flex';
            break;
        case 3:
            document.getElementById('Endurance').style.display = 'none';
            document.getElementById('Agility').style.display = 'flex';
            document.getElementById('submit_button').style.display = 'flex';
            document.getElementById('next_button').style.display = 'none';
            break;
        default:
            break;
    }
}

function playerStat(){
    
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

window.onload = webgl();
