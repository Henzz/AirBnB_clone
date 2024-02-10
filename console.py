#!/usr/bin/python3
"""Module for HBNB command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        except IndexError:
            pass

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()
        except IndexError:
            pass

    def do_all(self, arg):
        """Print all string representation of all instances"""
        args = arg.split()
        if not arg or args[0] not in globals():
            print("** class doesn't exist **")
            return
        objects = storage.all()
        print([str(obj) for obj in objects.values() if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3].strip('"'))
            storage.all()[key].save()
        except IndexError:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
