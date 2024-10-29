const express = require('express');
const serverless = require('serverless-http');
const jobsRoutes = require('./routes/jobs');
const errorHandler = require('./middleware/errorHandler');

const app = express();
app.use(express.json());

app.use('/api/v1', jobsRoutes);

app.get('/', (req, res) => {
    res.json({ "Welcome to the devpsAPI!": "Use the /api/v1/jobs endpoint to find Software Engineer Jobs." });
});

app.use(errorHandler);

module.exports.handler = serverless(app);
