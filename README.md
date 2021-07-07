# AirBnB_clone
<img src="https://i.imgur.com/6JaLQ4z.png" align="center">

### Welcome to the AirBnB clone project! (The Holberton B&B)
### By Francisco Calixto & Rodrigo Delgado

#### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the  **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

-   put in place a parent class (called  `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-   create all classes used for AirBnB (`User`,  `State`,  `City`,  `Place`…) that inherit from  `BaseModel`
-   create the first abstracted storage engine of the project: File storage.
-   create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

It’s just like the shell, exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of the project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## How to use the console:

### Execution examples:

#### Interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
### Built-in commands:
We have created built-in commands that can be used to modify different objects. These objects can belong to each of the following classes: BaseModel (father class), User, City, Amenity, Review, Place, State. All all of the last classes inherit from BaseModel.

#### The list of these built-in commands is:

 - create - `create <class name>` - Create class instance
 - destroy - `destroy <class name> <obj id>` - Destroy instance
 - update - `update <class name> <object id> <attribute name> "<attribute value>"` - Update or set given attribute
 - show - `show <class name> <obj id>` - show string representation of object
 - all - `all` or `all <class name>`- Prints all string representation of all instances based or not on the class name

#### Examples:
```
(hbnb) create User
29b75053-2282-47b0-aea4-fcc8558002f6
(hbnb) show User 29b75053-2282-47b0-aea4-fcc8558002f6
[User] (29b75053-2282-47b0-aea4-fcc8558002f6) {'created_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707721), 'updated_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707745), 'id': '29b75053-2282-47b0-aea4-fcc8558002f6'}
(hbnb) all
["[User] (29b75053-2282-47b0-aea4-fcc8558002f6) {'created_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707721), 'updated_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707745), 'id': '29b75053-2282-47b0-aea4-fcc8558002f6'}"]
(hbnb) update User 29b75053-2282-47b0-aea4-fcc8558002f6 first_name "Francisco"
(hbnb) all User
["[User] (29b75053-2282-47b0-aea4-fcc8558002f6) {'first_name': 'Francisco', 'updated_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707745), 'created_at': datetime.datetime(2021, 7, 5, 21, 6, 42, 707721), 'id': '29b75053-2282-47b0-aea4-fcc8558002f6'}"]
(hbnb) destroy User 29b75053-2282-47b0-aea4-fcc8558002f6
(hbnb) all
[]
(hbnb) 
```
### Exiting the console:

 - quit:
```
(hbnb) destroy User 29b75053-2282-47b0-aea4-fcc8558002f6
(hbnb) all
[]
(hbnb) quit
root@841fb2799066:/AirBnB_clone#
```
 - EOF:
 ```
(hbnb) destroy User 29b75053-2282-47b0-aea4-fcc8558002f6
(hbnb) all
[]
(hbnb) EOF
root@841fb2799066:/AirBnB_clone#
 ```

## Important info:


`models/__init__.py`: creates a unique `FileStorage` instance for the program, this instance 'storage' is used until the program is killed.

By default, the .json file which is created to store the representation of all objects is called "file.json". This string is set in the `__file_path` private class attribute in `model/engine/file_strorage.py`.
