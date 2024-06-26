const { spawn } = require('child_process');

// Define the Python script and its arguments
const pythonProcess = spawn('python', ['chatgpt.py']);

// Optional: Listen to Python process stdout
pythonProcess.stdout.on('data', (data) => {
  console.log(`Python stdout: ${data}`);
});

// Optional: Listen to Python process stderr
pythonProcess.stderr.on('data', (data) => {
  console.error(`Python stderr: ${data}`);
});

// Handle Python process exit
pythonProcess.on('close', (code) => {
  console.log(`Python process exited with code ${code}`);
});
