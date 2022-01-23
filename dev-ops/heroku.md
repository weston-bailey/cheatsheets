# Heroku cheatsheat

## install heroku and heroku CLI

`brew tap heroku/brew && brew install heroku`

## Always make a procfile

`touch Procfile`

example adding a node server:

echo "web: node server.js" >> ProcFile

`cat Procfile`

## CLI
function | Command
|--------|--------|
login | `heroku login`
create app | `heroku apps:create <app name>`
set repo to heroku remote | `heroku git::remote -a <heroku app name>`
push repo to heroku | `git push heroku <main> or <master>`
moniter server logs | `heroku logs --tail`
open postgresQL termianl | `heroku pg:psql`
run node script | `heroku run node script.js`