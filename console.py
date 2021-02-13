#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
import sys
import json

from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Class of the command interpreter
    """
    
    prompt = '(hbnb) '
    file = None
    __file_path = "file.json"

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if arg == "":
            print("** class name missing **")
        if arg == "BaseModel":
            obj = eval(arg + "()")
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if args[0] == "":
            print("** class name missing **")
        print("ALO1")
        if args[0] == "BaseModel":
            key = args[0] + "." + args[1]
            stor_a = storage.all()
            print(storage.all())
            print("ALO2")
            print(stor_a)
            if key in stor_a:
                print(stor_a["key"])
        else:
            print("** class doesn't exist **")


    def do_help(self, arg):
        """
        Display an help for commands.
        arg (str): precise the command where the help is needed.
        """

        tab = ["quit", "EOF"]
        if arg == "help" or arg == "":
            print()
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")
            print()
        if arg in tab:
            eval("self.help_" + arg + "()")

    def help_quit(self):
        """
        Display the help for the command "quit".
        """

        print("Quit command to exit the program")
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

    def close(self):
        """
        Close a file.
        """

        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
