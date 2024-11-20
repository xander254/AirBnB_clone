#!/usr/bin/python3
"""Entry point of the command interpreter."""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


valid_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Command interpreter for the HBNB."""

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program with EOF"""
        print("")
        return True

    def emptyline(self):
        """Do notthing on empyline input"""
        pass

    def do_create(self, arg):
        """Create a new class instance, save it, and print the id."""
        argument = shlex.split(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return
        class_name = argument[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = valid_classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints string representation of an instance(class name & id)
        """
        argument = shlex.split(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return
        if argument[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(argument[0], argument[1])
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
        else:
            print(obj[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        argument = shlex.split(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return
        if argument[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(argument[0], argument[1])
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
        else:
            del obj[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances.
        Supports syntax like User.all()
        """
        argument = shlex.split(arg)

        objects = storage.all()

        if len(argument) == 0:
            for obj in objects.values():
                print(str(obj))
        elif argument[0] not in valid_classes:
            print("** class doesn't exist**")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == argument[0]:
                    print(str(obj))

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        argument = shlex.split(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return
        if argument[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        key = f"{argument[0]}.{argument[1]}"
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
            return
        if len(argument) < 3:
            print("** attribute name missing **")
            return
        if len(argument) < 4:
            print("** value missing **")
            return

        objct = obj[key]
        attr_name = argument[2]
        attr_value = argument[3].strip('"')

        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        setattr(objct, attr_name, attr_value)
        objct.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
