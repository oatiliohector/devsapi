const express = require('express');
const { getJobs } = require('../controllers/jobController');

const router = express.Router();

router.get('/jobs', getJobs);

module.exports = router;
