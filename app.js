const express = require('express');
const serverless = require('serverless-http');
const axios = require('axios');

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

app.get('/lindo/teste2', (req, res) => {
    res.json({ "Welcome to the devpsAPI! 2": "Teste mais eficaz que tudo!" });
});

app.get('/api/jobs/:job_id', (req, res) => {
    const job_id = req.params.job_id;
    res.json({
        job_id: job_id,
        job_title: "Software Engineer",
        company: "Devs"
    });
});

app.get('/api/jobs', async (req, res) => {
    const urls = [
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/todos/2',
        'https://jsonplaceholder.typicode.com/todos/3',
        'https://jsonplaceholder.typicode.com/todos/4',
        'https://jsonplaceholder.typicode.com/todos/5',
        'https://jsonplaceholder.typicode.com/todos/6',
        'https://jsonplaceholder.typicode.com/todos/7',
        'https://jsonplaceholder.typicode.com/todos/8',
        'https://jsonplaceholder.typicode.com/todos/9',
        'https://jsonplaceholder.typicode.com/todos/10'
    ];

    const startTime = Date.now(); 

    try {
        const requests = urls.map(url => axios.get(url));
        const responses = await Promise.all(requests);
        const jobs = responses.map(response => response.data);

        const endTime = Date.now(); 
        const duration = (endTime - startTime) / 1000;

        res.json({
            message: "All requests completed",
            duration: `${duration} seconds`,
            data: jobs
        });
    } catch (error) {
        res.status(500).json({ message: "Error fetching jobs data", error: error.message });
    }
});

module.exports.handler = serverless(app);
