#!user/bin/python3
"""console to operate on db"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command that exit the program"""
        return True

    def do_EOF(self, arg):
        """Command that exit the program"""
        return True

    def emptyline(self):
        """handle an empty line command"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
