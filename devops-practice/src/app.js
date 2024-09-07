
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/delay', (req, res) => {
    setTimeout(() => {
        res.send('This was delayed by 2 seconds');
    }, 2000);
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 0; 
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}