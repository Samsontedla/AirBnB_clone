#!/usr/bin/python3
"""
File: console.py

Authors:
        Samson Tedla <samitedla23@gmail.com>
        Elnatan Samuel <krosection999@gmail.com>

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = models.storage


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand - a console class for the the airbnb clone
        project
    """

    prompt = '(hbnb) '
    __class_lst = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]

    def parse(arg, id=" "):
        """
        Returns a list conatning the parsed arguments from the string
        """

        arg_list = arg.split(id)
        narg_list = []

        for x in arg_list:
            if x != '':
                narg_list.append(x)
        return narg_list

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def help_quit(self):
        """Prints help for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id.
        """
        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
            return False

        if len(arg_lst) > 1:
            print("** to many arguments **")
            return False

        if (arg_lst[0] in HBNBCommand.__class_lst.keys()):
            new_obj = HBNBCommand.__class_lst[arg_lst[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
           prints help info for the create function
        """
        print("""Creats a new instance of the first argument
              stores it in the JSON file and prints its id""")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        arg_lst = HBNBCommand.parse(arg)
        db = storage.all()
        if not len(arg_lst):
            print("** class name missing **")
        elif (arg_lst[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        elif len(arg_lst) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(arg_lst[0], arg_lst[1])])

        # Extra case
        # elif len(arg_lst) > 2:
        #    print("** to many arguments **")

    def help_show(self):
        """
            Prints help for for the creat function
        """
        print("""Prints the string representation of an instance based
            on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234
            """)

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """
            Prints help for the destroy function
        """
        print("""Deletes an instance based on the class name and id
              (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234""")

    def do_all(self, arg):
        """
            Prints all string representation of all instances based or
            not on the class name.
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_list) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """
            prints help for the all function
        """
        print("""Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all""")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234 email
                      "aibnb@mail.com"
        """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] is '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """
            prints help for the update function
        """
        print(
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234
                      email "aibnb@mail.com""")

    def emptyline(self):
        """
            Does nothing if Empty line + enter is inserted.
            Used for overriding the emptyline function
        """
        pass

    def do_count(self, arg):
        """
            Prnits the number of elements inside the FileStorage that
            are of instances of cls
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_list) == 0:
                    objl.append(obj.__str__())
            print(len(objl))

    def show(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls.
        """
        pass

    def destroy(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls.
        """
        pass

    def update(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls.
        """
        pass

    def default(self, line):
        """
            Handles the case where the the command has no equivlaent
            do_ method.
        """
        line_p = HBNBCommand.parse(line, '.')
        if line_p[0] in HBNBCommand.__class_lst.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.__class_funcs:
                func = line_p[1][:-2]
                cls = HBNBCommand.__class_lst[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
