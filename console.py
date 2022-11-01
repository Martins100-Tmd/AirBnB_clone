#!user/bin/python3
"""console to operate on db"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel
            }

    def do_quit(self, arg):
        """Command that exit the program"""
        return True

    def do_EOF(self, arg):
        """Command that exit the program"""
        return True

    def emptyline(self):
        """handle an empty line command"""
        return False

    def do_create(self, arg):
        """creates a self object from a class"""
        if arg:
            arg = arg.split(" ")
            if arg[0] in HBNBCommand.classes:
                Mole = HBNBCommand.classes[arg[0]]()
                if Mole:
                    print(Mole.to_dict()['id'])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints the string repr of an instance if it exists"""
        if arg:
            arg = arg.split(" ")
            res = {}
            flag_ = False
            if len(arg) == 1:
                print("** instance id missing **")
                return
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                objname = k.split(".")[0]
                objid = k.split(".")[1]
                modtodict = v.to_dict()
                if arg[1] == objid:
                    flag_ = True
                    print("[{}] ({}) {}".format(objname, objid, modtodict))
            if flag_ == False:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """deletes an instance baseed on class name and id"""
        if arg:
            arg = arg.split(" ")
            flag = False
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            if len(arg) == 1:
                print("** instance id missing **")
                return
            for k, v in models.storage.all().items():
                obj_id = k.split(".")[1]
                if arg[1] == obj_id:
                    flag = True
            if flag:
                del models.storage.all()[str(arg[0] + "." + arg[1])]
                models.storage.save()
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

    def do_all(self, arg):
        """prints all the str repr of instances"""
        if arg:
            all_list = []
            arg = arg.split(" ")
            if arg[0] not in HBNBCommand.classes and arg[0] != ".":
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes or arg[0] == ".":
                print(models.storage.all())
                for k, v in models.storage.all().items():
                    obj_name = k.split(".")[0]
                    obj_id = k.split(".")[1]
                    obj_dict = v.to_dict()
                    all_list.append("[{}] ({}) {}".format(obj_name, obj_id, obj_dict))
                print(all_list)

    def do_update(self, arg):
        """updates an instance based on class name and id"""
        if arg:
            arg = arg.split(" ")
            if len(arg) > 4:
                arg = arg[:4]
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            if len(arg) == 1:
                print("** instance id missing **")
                return
            if len(arg) == 2:
                print("** attribute name missing **")
                return
            if len(arg) == 3:
                print("** value missing **")
                return
            flag = False
            for k, v in models.storage.all().items():
                obj_id = k.split(".")[1]
                if arg[1] == obj_id:
                    flag = True
                    models.storage.all()[k].to_dict().update({arg[2]: arg[3]})
                    print(models.storage.all()[k].to_dict())
                    models.storage.all()[k].save()
            if flag == False:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
