#!user/bin/python3
"""console to operate on db"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command line interface class"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """quit the terminal"""
        exit()

    def do_EOF(self, args):
        """quit the terminal"""
        exit()

    def emptyline(self):
        """handle an empty line command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
