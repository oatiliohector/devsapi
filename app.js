const express = require('express');
const serverless = require('serverless-http');

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.json({ "Welcome to the devpsAPI!": "Use the /api/v1/jobs endpoint to find Software Engineer Jobs." });
});

app.post('/api/v1/jobs', async (req, res) => {
    res.json({ "Jobs!": "Building." });
});

module.exports.handler = serverless(app);
