# HBNB

Version two of the AirBnB clone as part of the Hokberton School of Software Engineering Curriculum

## AirBnB Clone

This is the command interpreter for the AirBnB clone. Console stores and retrieves objects in JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

Enter `./console.py` in the project directory via shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Console also supports the following format:
`<class name>.<command>(<parameters>)` syntax.

Ex:
`City.show(my_city_id)`

## Authors:
* [Nehal Shastri](https://github.com/nhlshstr)
* [Kyle Cambell](https://github.com/waffle52)
