const express = require('express');
const serverless = require('serverless-http');

const app = express();

const title = "Devs API";
const description = "Software Engineer Jobs API";
const version = "1.0.0";

app.get('/', (req, res) => {
    res.json({ "Welcome to the devpsAPI!": "Know more about on the route /docs" });
});

app.get('/lindo/teste', (req, res) => {
    res.json({ "Welcome to the devpsAPI!": "Teste mais eficaz que tudo!" });
});


app.get('/api/jobs/:job_id', (req, res) => {
    const job_id = req.params.job_id;
    res.json({
        job_id: job_id,
        job_title: "Software Engineer",
        company: "Devs"
    });
});

module.exports.handler = serverless(app);
