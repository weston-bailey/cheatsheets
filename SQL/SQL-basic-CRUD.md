# Basic SQL CRUD operations 

## Super basics

```sql
--comments start with two hyphens

--commands end with a semicolon ;

--commands are not case sensitive, but convention prescribes that
--all commands be written in UPPER CASE so that they are visually distinquishable
--from database, table and column names

--database and table names should be plural while columns names should be singular 
```

## Managing databases

```sql
--creates a new database
CREATE DATABASE database_name;
--deletes a database
DROP DATABASE database_name;
```

## Basic READ: with `SELECT`

```sql
--select all rows and columns from a table
SELECT * FROM table;
SELECT ALL FROM table;

--select all rows with specific columns from a table
SELECT column_one, column_two FROM table;

SELECT * FROM table WHERE key = value;
```

Select specific

> `SELECT` key1, key2 `FROM` table;

Remove all data from a table

[More Info](https://www.postgresqltutorial.com/postgresql-truncate-table/)

> `TRUNCATE TABLE` table;
>
> `TRUNCATE TABLE` table `RESTART IDENTITY`;

Remove all foreign keys

> `TRUNCATE TABLE` table `CASCADE`

Delete Table

> `DROP TABLE` table;






