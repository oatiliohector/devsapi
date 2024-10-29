const PythonOrg = require('../modules/python/python-org');

const getJobs = async (req, res) => {
    try {
        const jobs = await PythonOrg();
        res.json({ jobs });
    } catch (error) {
        res.status(500).json({ error: 'Error fetching jobs' });
    }
};

module.exports = { getJobs };
