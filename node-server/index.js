const express = require('express');
const app = express();
const port = 5000;

app.get('/', (req, res) => res.send(`
    <div style="
        width: 500px;
        height: 500px;
        background-color: rgba(0, 255, 0, 0.2);
        line-height: 500px;
        text-align: center;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        box-sizing: border-box;
    ">
        <h1>Hello World!</h1>
    </div>
`));

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
