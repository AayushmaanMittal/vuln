const express = require('express');
const app = express();
app.use(express.json());

app.post('/login', (req, res) => {
  const q = "SELECT * FROM users WHERE user='" + req.body.user + "'";
  db.query(q, (err, result) => res.json(result));
});

app.listen(3000);