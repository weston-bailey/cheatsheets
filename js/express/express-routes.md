# Express Routes Cheat Sheet

[Express Notes Gitbook](https://gawdiseattle.gitbook.io/wdi/05-node-express/00readme-1/01intro-to-express)

set up express server

```javascript
//require express module
const express = require('express');
//call express method and assign it a variable
const app = express();

//example home route
app.get('/', function(req, res) {
    res.send('Hello, World!');
});

//call listen method and supply a port as an argument
app.listen(8000);

```

> (req, res)
>
> requests come from the client
>
> responses are made by the server

HTTP Verb | CRUD Action | Express Method
 ----------- | ----------- | ----------- 
 GET | READ | `app.get()`
 POST | CREATE | `app.post()`
 PUT | UPDATE | `app.put()`
 DELETE | DELETE | `app.delete()`

### Forms and Links Cheat sheet

#### POST - Request body

##### Html:

```html
<!-- method="VERB" anction="/route" name="req.body.name" -->
<form method="POST" action="/route">

  <label for="example">Input:</label>

  <input id="example" type="text" name="keyInReqBody">
  
  <input type="submit">
</form>
```
##### Route:

```javascript
//post forms use req.body
app.post('/route', (req, res) => {
  console.log(req.body.keyInReqBody)
});
```

#### GET - Request Parameters `req.params.htmlParam`

##### Html:

```html
<!-- URL: /route/param -->
<a href="/route/index">Link</a>

<!-- ejs scriplet -->
<a href="/route/"<%= index %>">Link</a>
```
##### Route:

```javascript
//found in params object
app.get('/route/:index', (req, res) => {
  console.log(req.params.index);
});
```

##### Html:

```html
<!-- URL: /route/param/param -->
<a href="/route/x/y">Link</a>

<!-- ejs scriplet -->
<a href="/route/"<%= x %>"/"<%= y %>"/>Link</a>
```
##### Route:

```javascript
//found in params object
app.get('/route/:x/:y', (req, res) => {
  console.log(req.params.x);
  console.log(req.params.x.y);
});
```

#### Get - Request Query `req.query.name`

##### Html:

```html
<!-- query strings always start with a ? -->

<!-- method="VERB" action="/route" name="req.query.name" -->
<form method="GET" action="/route">

  <label for="example">Input:</label>

  <input id="example" type="text" name="keyInReqQuery">
  
  <input type="submit">
</form>
```

##### Route:

```javascript
//GET forms use req.query
app.get('/route', (req, res) => {
  console.log(req.query.keyInReqQuery)
});
```

#### POST/GET (DELETE) - Request Query `req.params.htmlParam`

##### Html:

```html
<!-- query strings always start with a ? -->

<!-- here the query sting is ?_method=DELETE -->

<!-- POST form for delete -->
<form method="POST" action="/route/<%= index %>/?_method=DELETE">
  <input type="submit" value="Delete">
</form>

<!-- GET link for delete (untested) -->
<"/route/<%= index %>/?_method=DELETE"/>Delete</a>
```

##### Route:

```javascript
//required method overide for HTML delete
let express = require('express');
let methodOverride = require('method-override');
let app = express();
app.use(methodOverride('_method'));

//html params used for delete
app.delete('/route/:index', (req, res) => {
  console.log(req.params.index)
});
```

#### PUT - Request Parameters `req.params.htmlParam`

##### Html:

```html
<!-- URL: /route/param -->
<a href="/route/index>Edit</a>

<!-- ejs scriplet -->
<a href="/route/"<%= index %>">Edit</a>
```
##### Route:

```javascript
//found in params object
app.put('/route/:index', (req, res) => {
  console.log(req.params.index);
});
```

### Ejs forEach() and for(in) cheatsheet

#### Unordered list from array

##### Html:

```html
<ul>
  <% myArray.forEach( (element) => { %>

    <li> <%= element.key1 %> Yay list <%= element.key2 %>

      <!-- example with edit link and delete button  -->

      <a href="/route/"<%= element.index %>">Edit</a>

      <form method="POST" action="/route/"<%= element.index %>"/?_method=DELETE">
        <input type="submit" value="Delete">
      </form>

    </li>
  <% }) %>
</ul>
```

#### Unordered list from object

##### Html:

```html
<ul>
  <% for(let key in object) { %>
    <li><%= key %> : <%= object[key] %></li>
    <% } %>
</ul>
```
