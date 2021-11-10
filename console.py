#!/usr/bin/python3


import cmd




class HBNBCommand(cmd.Cmd):
   "

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

    @staticmethod
    def parse(arg, id=" "):
        

        arg_list = arg.split(id)
        narg_list = []

        for x in arg_list:
            if x != '':
                narg_list.append(x)
        return narg_list

    def do_quit(self, arg):
       
        return True

    def help_quit(self):
        

    def do_EOF(self, arg):
     

        print("")
        return True

    def do_create(self, arg):
       

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
       
        print("""Creats a new instance of the first argument
              stores it in the JSON file and prints its id""")

    def do_show(self, arg):
        
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
       
        print("""Prints the string representation of an instance based
            on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234
            """)

    def do_destroy(self, arg):
        
        arg_lst = HBNBCommand.parse(arg)
        storage.reload()
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
            # print(storage.__class__.__name__.__objects)
            del db["{}.{}".format(arg_lst[0], arg_lst[1])]
            storage.save()

    def help_destroy(self):
         
        print("""Deletes an instance based on the class name and id
              (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234""")

    def do_all(self, arg):
        
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
        
        print("""Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all""")

    def do_update(self, arg):
       
        arg_list = HBNBCommand.parse(arg)
        objdict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def help_update(self):
      
        print(
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234
                      email "aibnb@mail.com""")

    def emptyline(self):
        
        pass

    def do_count(self, arg):
       
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
       
        pass

    def destroy(self, cls):
       
        pass

    def update(self, cls):
        
        pass

    def default(self, line):
       

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
