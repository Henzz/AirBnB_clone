#!/usr/bin/env python3
# console.py
"""Command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnh) "  # Shows a prompt

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, line):
        """Exits the console on EOF (Ctrl+D)"""
        return True

    def do_quit(self, args):
        """Exits my cmd console"""
        return True

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
