#!user/bin/python3
"""console to operate on db"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command line interface class"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """quit the terminal"""
        return True

    def do_EOF(self, arg):
        """quit the terminal"""
        return True

    def emptyline(self):
        """handle an empty line command"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
