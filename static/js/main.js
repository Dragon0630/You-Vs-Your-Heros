const fs = require('fs');

// Step 1: Read the JSON file
fs.readFile('../template.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

    // Step 2: Parse the JSON
    const jsonObject = JSON.parse(data);

    // Step 3: Modify the JavaScript object
    jsonObject.newkey = 'New Value'; // Example modification

    // Step 4: Convert the JavaScript object back to JSON
    const modifiedJSON = JSON.stringify(jsonObject, null, 2); // null and 2 for formatting

    // Step 5: Write the JSON back to the file
    fs.writeFile('data.json', modifiedJSON, 'utf8', (err) => {
        if (err) {
            console.error('Error writing file:', err);
            return;
        }
        console.log('File has been modified successfully.');
    });
});