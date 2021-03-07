# Sequelize Cheat Sheet

[Notes in Gitbook](https://gawdiseattle.gitbook.io/wdi/05-node-express/express-sequelize)

### Install

*make sure to install version 5.21.13*

> `npm install sequelize@5.21.13`

install postgres 

> `npm i pg`

### Setting up a project

creates `./config/config.json`
 
> `sequelize init`

```javascript
{
  "development": {
    //remove user and password key/values
    "database": "databaseName", //update to database name
    "host": "127.0.0.1",
    "dialect": "postgres" //update to postgres dialect
  },
  "test": {
    "database": "userapp_test",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "database": "userapp_production",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

create models to be migrated as tables

> `sequelize model:create --name` table `--attributes` key1:string,key2:string,key3:integer,key4:string

> foreign keys should follow the pattern: `tableId:integer`

### Update models

1:M relationships need a foreign key that references the parent in the child model:

```javascript
//child table's model
'use strict';
module.exports = (sequelize, DataTypes) => {
  const childTable = sequelize.define('childTable', {
    content: DataTypes.TEXT,
    parentTableId: DataTypes.INTEGER
  }, {});
  childTable.associate = function(models) {
    // associations can be defined here
    models.childTable.belongsTo(models.parentTable);
  };
  return childTable;
};

//parent table's model
'use strict';
module.exports = (sequelize, DataTypes) => {
  const parentTable = sequelize.define('parentTable', {
    content: DataTypes.TEXT,
  }, {});
  parentTable.associate = function(models) {
    // associations can be defined here
    models.parentTable.hasMany(models.childTable);
  };
  return parentTable;
};
```

N:M relationships need a join table model definition:

> `sequelize model:create --name` siblingsOneSiblingsTwo `--attributes siblingOneId:integer,siblingTwoId:integer` 

```javascript
//join table model:
'use strict';
module.exports = (sequelize, DataTypes) => {
  const siblingsOneSiblingsTwo = sequelize.define('siblingsOneSiblingsTwo', {
    siblingOneId: DataTypes.INTEGER,
    siblingTwoId: DataTypes.INTEGER
  }, {});
  siblingsOneSiblingsTwo.associate = function(models) {
    // associations can be defined here
  };
  return siblingsOneSiblingsTwo;
};

//siblingOne table's model
'use strict';
module.exports = (sequelize, DataTypes) => {
  const siblingOne = sequelize.define('siblingOne', {
    content: DataTypes.TEXT,
  }, {});
  siblingOne.associate = function(models) {
    // associations can be defined here
    models.siblingOne.belongsToMany(models.siblingTwo, { through: 'siblingsOneSiblingsTwo'})
  };
  return siblingOne;
};

//siblingTwo table's model
'use strict';
module.exports = (sequelize, DataTypes) => {
  const siblingTwo = sequelize.define('siblingTwo', {
    content: DataTypes.TEXT,
  }, {});
  siblingTwo.associate = function(models) {
    // associations can be defined here
    models.siblingTwo.belongsToMany(models.siblingOne, { through: 'siblingsOneSiblingsTwo'})
  };
  return siblingTwo;
};

```

### Assiociations

> N:M 
> * `models.siblingTwo.belongsToMany(models.siblingOne, { through: 'siblingsOneSiblingsTwo'})`
> * `models.siblingOne.belongsToMany(models.siblingTwo, { through: 'siblingsOneSiblingsTwo'})`

> 1:M
> * `models.parentTable.hasMany(models.childTable);`
> * `models.childTable.belongsTo(models.parentTable);`



### Migration

update migrations where applicable

`allowNull: false,`

run migration

> `sequelize db:migrate`

undo last migration

> `sequelize db:migrate:undo`

## Sequalize CRUD Methods:

#### Promises:

`.promise()` | Description 
----------- | ----------- 
`.then()` | default promise called when a query is completed.
`.then([spread1, spread1])()` | used to spread an array of values to parameters. This is only used for findOrCreate
`.spread(spread1, spread2)` | see above
`.catch()` | triggered if something goes wrong (an error).
`.finally()` | triggered after all other callbacks. Can be used for cleanup.

#### Associations:

Once the association is set up, we can use the createModel, getModels, setModel, and addModel helper methods. "Model" in each of these is replaced with the model name you create. This uses nested methods

`method()` | Description 
----------- | ----------- 
`createModel()` | create entry in associated model
`getModel()` | read entries that are associated
`addModel()` |  used to associate existing entries 
`setModel()` | see above

#### 'Eager Loading'

used to load all the entries from a table if you might need them (include)

`[db.model]`

```javascript
db.user.findAll({
  include: [db.pet]
}).then(function(users){
  // users will have a .pets key with an array of pets
  console.log(users[0].pets);
});
```


### Handy error catch function:

```javascript
const errorHandler = error => {
  console.log(`error detected`);
  console.log(`🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥`);
  console.log(error);
}
```

### CREATE:
```javascript
db.table.create({
  firstName: 'Brian',
  lastName: 'Hague',
  age: 99
}).then(function(data) {
  // you can now access the newly created task via the variable data
});

db.user.create({  
  firstName: 'Steve',
  lastName: 'Peters',
  age: 44,
  email: 'stpets@gmail.com'
}).then(userData => { //promise syntax takes an anon function
  //now access new ever via userData variable
  console.log(`user ${userData}`);
}).catch( error => {
  errorHandler(error);
});

//spread operator todo reseach
db.user.findOrCreate({
  //use unique data for find or create
  where: {
    email: 'b.hague@ga.com'
  },
  //defualt values if not found (only matter if not found)
  defaults: {
    firstName: 'Brian',
    lastName: 'Hague',
    age: 99
  }
  //promise with two arguments (spread operator args as array)
}).then( ([user, created]) => {
  console.log(`user ${user.firstName} was ${created ? 'created' : 'found'}`);
}).catch( error => {
  errorHandler(error);
});
```
### CREATE with associations:
```javascript
//(nested promises)
db.user.findOne().then( user => {
  user.createPet({
    name: 'Silly May',
    species: 'Mini Aussie',
    description: 'A big loaf of dog with different colored eyes'
  }).then( pet => {
    console.log(`🐕 hello there ${pet.name}`);
  }).catch( error => {
    errorHandler(error);
  });
}).catch( error => {
  errorHandler(error);
});

db.pet.findOrCreate({
  where: {
    name: 'Simba',
    species: 'Ginger Cat'
  },
  defaults: {
    description: 'Traumatised by a very jealous toy aussie, Simba is very cute but rarely comes out to play'
  }
}).then(function([pet, created]) {
  db.user.findOne().then(function(user) {
    //associate previously loaded pet instance
    user.addPet(pet);
    console.log('User ' + user.firstName + ' is the owner of ' + pet.name);
  });
});

```

### READ:

```javascript
db.user.findOne({
  where: {
    id: 1
  }
}).then(foundUser => {
  //what to do with found user
  console.log(`hey there ${foundUser.firstName} you are ${foundUser.age} years old`);
}).catch( error => {
  errorHandler(error);
});

db.user.findAll().then(users => {
  users.forEach( user =>  console.log(`👑 hey there ${user.firstName}!`)); //implicit return
}).catch(error => {
  errorHandler(error);
});
```

### READ with associations:
```javascript
db.user.findOne().then(function(user) {
  //load pets for this user
  user.getPets().then(function(pets) {
    //do something with pets here
  });
});
```

### UPDATE:
```javascript
// UPDATE users SET age = 99 WHERE email = 'b.hague@ga.co'
// takes two objects as args
db.user.update({ 
  age: 99 
}, { 
  where: { 
    email: 'b.hague@ga.com'
  } 
}).then( updated => {
  //return array with one value of the number of items updated
  console.log('🏆');
  console.log(updated);
}).catch( error => {
  errorHandler(error);
})

```

### DESTROY
```javascript
db.user.destroy({
  where: {
    firstName: 'Brian' //will destroy multiple brians
  }
}).then(deleted => {
  console.log('🔥');
  console.log(deleted); //number of deleted items (int)
}).catch( error => {
  errorHandler(error);
}).finally( () => { // triggered after all the promise actions
  console.log('finally done')
});
```




















