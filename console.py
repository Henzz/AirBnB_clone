#!/usr/bin/env python3
"""Command line interpreter"""
import cmd

class MyCmd(cmd.Cmd):
    prompt = "(hbnh) " # prompt text
    intro = "Welcome to the console. Type 'help' for available commands." # Intro message

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

    def do_EOF(self, line):
        """Exits the console"""
        return True

    def do_quit(self, args):
        """Exits my cmd console"""
        return True


if __name__ == "__main__":
    MyCmd().cmdloop()
