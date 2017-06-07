Rock Paper Scissors
===================

Program an API to play Rock Paper Scissors. Submit your
'choice' of 'rock', 'paper', or 'scissors', via a
querystring and return a JSON object with the following
key/value pairs:

{
  "you": "<user submitted data>",
  "comp": "<randomly generated choice>",
  "win": "<game result>"
}

An example query of `http://localhost:5000?choice=rock`
might return:

{
  "you": "rock",
  "comp": "scissors",
  "win": "WIN"
}

Your API can be tested at `localhost:5000` and
`localhost:5000/play`. At `localhost:5000/v1` a pre-built
HTML template will test your API and allow you to play the
game.

## Version Two
At `localhost:5000/v2` a pre-built template  allows
presentation of total game wins, which can be tracked
globally.

## Version Three
At `localhost:5000/v3` a pre-built template allows
password-free user login, and the presentation of a user's
total wins. Use Flask's `session` property to enable this
feature.
