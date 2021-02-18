#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class of the command interpreter
    """

    prompt = '(hbnb) '
    file = None
    __file_path = "file.json"
    classes = ["BaseModel",
               "User",
               "Amenity",
               "City",
               "State",
               "Review",
               "Place"
               ]

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split()
        if args == [] or arg == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            stor_a = storage.all()
            key = args[0] + "." + args[1]
            setattr(stor_a[key], args[2], args[3])
            storage.save()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg + "()")
            obj.save()
            print(obj.id)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if args == [] or arg == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = args[0] + "." + args[1]
            stor_a = storage.all()
            if key in stor_a:
                del stor_a[key]
                storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = arg.split()
        if args == [] or arg == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = args[0] + "." + args[1]
            stor_a = storage.all()
            if key in stor_a:
                print(stor_a[key])

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        stor_a = storage.all()
        obj_list = []
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
            else:
                for key in stor_a:
                    class_id = key.split(".")
                    if class_id[0] == arg:
                        obj_list.append(stor_a[key].__str__())
                print(obj_list)
        else:
            for key in stor_a:
                obj_list.append(stor_a[key].__str__())
            print(obj_list)

    def do_help(self, arg):
        """
        Display an help for commands.
        arg (str): precise the command where the help is needed.
        """

        tab = ["quit", "EOF", "show", "create", "destroy", "all", "update"]
        if arg == "help" or arg == "":
            print()
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF help quit show create destroy all update")
            print()
        if arg in tab:
            eval("self.help_" + arg + "()")

    def help_quit(self):
        """
        Display the help for the command "quit".
        """

        print("Quit command to exit the program")
        print()

    def help_update(self):
        """
        Display the help for the command update.
        """

        print("Updates or add an instance attribute.")
        print("Usage:")
        print("update <class name> <id> <attribute name> <attribute value>")
        print()

    def help_all(self):
        """
        Display the help for the command all.
        """

        print("Display all object with or without class name.")
        print("Usage: all <class name>")
        print()

    def help_destroy(self):
        """
        Display the help for the command destroy.
        """

        print("Destroy an object.")
        print("Usage: destroy <class name> <id>")
        print()

    def help_show(self):
        """
        Display the help for the command show.
        """

        print("Show an object.")
        print("Usage: show <class name> <id>")
        print()

    def help_create(self):
        """
        Display the help for the command create.
        """

        print("Create an object.")
        print("Usage: create <class name>")
        print()

    def help_EOF(self):
        """
        Display the help for the command EOF.
        """

        print("End of file")
        print()

    def do_quit(self, arg):
        """
        Quit the console with the "quit" command.
        """

        self.close()
        return True

    def do_EOF(self, arg):
        """
        Quit the console with the "EOF" command.
        """

        self.close()
        return True

    def emptyline(self):
        """
        Emptyline method to do nothing when press enter
        """
        pass

    def close(self):
        """
        Close a file.
        """

        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
