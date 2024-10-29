const axios = require('axios');
const cheerio = require('cheerio');

async function PythonOrg() {
    try {
        const response = await axios.get('https://www.python.org/jobs/location/telecommute/');
        const html = response.data;
        const $ = cheerio.load(html);
        const jobs = [];

        $('.list-recent-jobs li').each((_, element) => {
            const title = $(element).find('h2 a').text().trim();
            const location = $(element).find('.listing-location').text().trim();
            const datePostedText = $(element).find('.listing-posted').text().trim();
            const link = `https://www.python.org${$(element).find('h2 a').attr('href')}`;

            const isRemote = /remote/i.test(title) || /remote/i.test(location) ? "Yes" : "No";

            const datePosted = formatToBrazilianDate(datePostedText);

            jobs.push({ title, location, datePosted, link, remote: isRemote });
        });

        return jobs;
    } catch (error) {
        throw error('Error fetching jobs:', error);
    }
}

function formatToBrazilianDate(dateString) {
    const date = new Date(dateString);
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0'); 
    const year = date.getFullYear();

    return `${day}/${month}/${year}`;
}

module.exports = PythonOrg;
