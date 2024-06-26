const { exec } = require('child_process');

// Define the query dynamically
const query = "explain the contents in the page number 7";


// Execute the Python script with query as a parameter
exec(`python Chatgpt-pdf.py "${query}"`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`StdError: ${stderr}`);
       // return;
    }
    if (stdout){
        console.log('SK: ##############################################################')
        console.log(`Output: ${stdout}`);
        console.log('SK: ##############################################################')
    }
    
});

// node demo/dynaChatNodeJS.js