#!/usr/bin/env python3
# console.py
"""Command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnh) "  # Shows a prompt

    def do_greet(self, args):
        """Greets the user"""
        print("Greetings, How may I help you?")

    def do_sum(self, args):
        """Sums up two numbers"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 + num2
            print(f"The sum is {result}")
        except ValueError:
            print("Invalid input. Usage sum <num1> <num2>")

    def do_multiply(self, args):
        """Multiplies two numbers"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 * num2
            print(f"The product is {result}")
        except ValueError:
            print("Invalid input. Usage multiply <num1> <num2>")

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
        print("Quit the command interpreter.")

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit the command interpreter on EOF (Ctrl+D).")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
