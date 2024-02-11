#!/usr/bin/env python3
# console.py
"""This module defines the HBNBCommand class, a command interpreter"""

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNB Command Interpreter """

    prompt = "(hbnb) "  # Shows a prompt

    def do_create(self, arg):
        """ Create a new instance of BaseModel """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        new_instance = eval("{}()".format(class_name))
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Show string representation of an instance """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """ Destroy an instance by ID """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """ Print all instances """
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items() if key.split('.')[0] == class_name])

    def do_update(self, arg):
        """ Update an instance by ID """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        storage.save()

    def do_count(self, arg):
        """ Count instances of a class """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        print(len([obj for key, obj in storage.all().items() if key.split('.')[0] == class_name]))

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Do nothing on empty input line """
        pass

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit command to exit the program on EOF(Ctrl+D))\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()