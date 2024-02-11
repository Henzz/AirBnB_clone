#!/usr/bin/env python3
# console.py
"""Command line interpreter"""
import cmd
import readline


class HBNBCommand(cmd.Cmd):
    # Show a prompt
    prompt = "(hbnh) "

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
        Called when an empty line is entered in reponse to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def default(self, line):
        return cmd.Cmd.default(self, line)

    def do_EOF(self, line):
        """Exits the console"""
        return True

    def do_quit(self, args):
        """Exits my cmd console"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
