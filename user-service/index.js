const express = require('express');

const users = [
  {
    id: 1,
    name: {
      first: 'Alexandre',
      last: 'Cisneiros'
    },
    birthday: {
      year: 1993,
      month: 2,
      day: 16
    },
    password: 'duda'
  },
  {
    id: 2,
    name: {
      first: 'Joao',
      last: 'Sementedemaca'
    },
    birthday: {
      year: 1992,
      month: 7,
      day: 20
    },
    password: 'think'
  },
  {
    id: 3,
    name: {
      first: 'Guilherme',
      last: 'Empregos'
    },
    birthday: {
      year: 1992,
      month: 7,
      day: 20
    },
    password: 'start'
  }
];

const app = express();

app.get('/login/:id/:password', (req, res) => {
  let found = false;
  users.forEach((user) => {
    if (user.id === parseInt(req.params.id)) {
      found = user;
    }
  });

  if (found) {
    if (found.password === req.params.password) {
      res.json({
        id: found.id,
        name: found.name,
        birthday: found.birthday
      });
    } else {
      res.sendStatus(401);
    }
  } else {
    res.sendStatus(404);
  }
});

const port = 3000;

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
});
