#!user/bin/python3
"""console to operate on db"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command line interface class"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """quit the terminal"""
        exit()

    def do_help(self, args):
        """Quit command to exit the program"""
        if args:
            args = args.split(" ")
            if args[0] == "quit":
                print("Quit command to exit the program\n\n")

    def do_EOF(self, args):
        """quit the terminal"""
        exit()

    def emptyline(self):
        """handle an empty line command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
