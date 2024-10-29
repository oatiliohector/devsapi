const express = require('express');
const serverless = require('serverless-http');
const PythonOrg = require('./modules/python/python-org');

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.json({ "Welcome to the devpsAPI!": "Use the /api/v1/jobs endpoint to find Software Engineer Jobs." });
});

app.get('/api/v1/jobs', async (req, res) => {
    const jobs = await PythonOrg();
    res.json({ jobs });
});

module.exports.handler = serverless(app);
