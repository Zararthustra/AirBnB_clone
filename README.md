![Alt Text](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)
# 0x00. AirBnB clone - The console
A command line interpreter tool built for storing and manipulating site data for development and debugging.
Almost like the [shell](https://github.com/ThibaudP/simple_shell) and the [monty](https://github.com/Zararthustra/monty) project.

# Usage
```
AirBnB_clone$ ./console.py
(hbnb) *enter command here*
```
## Commands
| Command | Description | Example |
| --- | --- | --- |
| create | Creates a new instance of BaseModel, saves it to the JSON file and prints the id | ```(hbnb) create <class name>``` |
| show | Prints the string representation of an instance based on the class name and id | ```(hbnb) show <class name> <id>``` |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file) | ```(hbnb) destroy <class name> <id>``` |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) | ```(hbnb) update <class name> <id> <attribute name> "<attribute value>"``` |
| all | Prints all string representation of all instances based **or not** on the class name | ```(hbnb) all <class name>``` |
| help | display help information | ```(hbnb) help <command>``` |
| quit | exit the program | ```(hbnb) quit``` |
| EOF | exit the program | ```(hbnb) ctrl+D``` |

## Learning Objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is * args and how to use it
- What is ** kwargs and how to use it
- How to handle named arguments in a function
