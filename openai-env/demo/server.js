const express = require('express');
const { exec } = require('child_process');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Node.js server is running!');
});

app.post('/sendMessage', (req, res) => {
  const { message } = req.body;
  const query = message;

  exec(`python dynaChatGPT.py "${query}"`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      res.status(500).send('Internal Server Error');
      return;
    }
    if (stderr) {
      console.error(`StdError: ${stderr}`);
    }

    // Send the response (stdout) back to the frontend
    res.send(stdout);
  });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
