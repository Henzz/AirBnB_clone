import cmd

class AddressBook(cmd.Cmd):
    intro = "Welcome to my Address Book. Type 'help' for commands"
    prompt = "(Address Book)> "

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """Adds a new contact to the address book. Usage: add <phone> <name>"""
        phone, name = args.split()
        if phone not in self.contacts:
            self.contacts[phone] = name
            print(f"Contact added: {phone} - {name}")
        else:
            print(f"Contact {phone} already exists. use 'update' to update contact.")

    def do_read(self, args):
        """Reads all contacts"""
        if not self.contacts:
            print("No contacts found.")
        else:
            for phone, name in self.contacts.items():
                print(f"{phone} - {name}")

    def do_update(self, args):
        """Updates a contact. Usage: update <phone> <new_name>"""
        phone, new_name = args.split()
        if phone in self.contacts:
            self.contacts[phone] = new_name
            print(f"Contact name updated: {phone} - {new_name}")
        else:
            print(f"{number} not found. Use add to create contact.")

    def do_delete(self, args):
        """Deletes a contact. Usage: delete <phone>"""
        phone = args
        if phone in self.contacts:
            del self.contacts[phone]
            print(f"Deleted contact: {phone}")
        else:
            print(f"{phone} not found")

    def do_exit(self, args):
        """Exits the console"""
        return True

if __name__ == "__main__":
    AddressBook().cmdloop()
