# Postgres Psql Cheat Sheet

[SQL Notes Gitbook](https://gawdiseattle.gitbook.io/wdi/04-databases/sql-intro)

[psql shell reference](https://www.postgresql.org/docs/13/app-psql.html)

### Start psql shell in terminal 

`psql`

the psql shell doesn't like upper case letters dashes `-` so underscores `_` should be used for
spaces. 

```shell
example_database_name

doNotDoCamelCase
```

qoutes can be used to escape 'camelCase'


### Psql shell commands start with backslash `\`

Function | Command | Description
| ------ | ------- | ---------- |
help | `\?` | list help for the psql shell
help | `\h  SELECT` | get help for a specific SQL command 
quit | `\q` | quit the shell
list | `\l` | lists all availible dbs found in the cluster
connect | `\c` | connect to a database
describe tables | `\dt` | list all the tables in the current database
describe table | `\d table_name` | lists a table's columns and datatypes
edit command | `\e` | opens last command in your shell's default editor
expanded display | `\x off | on | auto` | will change the wrap behavior of column display
shell command | `\! clear` | \! escapes to the shell to execute a shell command
change dir | `\cd` | for some reason cd doesn't work like the other shell commands
describe schema | `\dn` | lists schema associated with current database
describe functions | `\df` | lists functions availible in the current database
echo | `\echo` | prints input to standard output


