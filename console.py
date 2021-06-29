#!/usr/bin/python3
''' The console '''

import cmd
import models
from models.base_model import BaseModel
from shlex import split


classes = {"BaseModel": BaseModel}


''' global function to validate objects ids '''


def id_validator(id):
    ''' takes id (string) and checks for it in __objects '''
    arr = []
    for key in models.storage.all():
        aux = key.split('.')
        arr.append(aux[1])
    if id in arr:
        return True
    return False


''' function to check if string represents float '''


def is_float(s):
    '''true if float, otherwise false'''
    try:
        float(s)
        return True and '.' in s
    except:
        return False


''' function to check if string represents int '''


def is_int(s):
    try:
        int(s)
        return True
    except:
        return False


class HBNBCommand(cmd.Cmd):
    ''' El console '''

    prompt = '(hbnb) '

    ''' quit xd '''

    def do_quit(self, line):
        ''' exit console '''
        return True

    '''  EOF '''

    def do_EOF(self, line):
        ''' exit console '''
        return True

    ''' Create '''

    def do_create(self, line):
        '''  Creates a new instance of BaseModel '''
        s = split(line)
        if len(s) < 1:
            print("** class name missing **")
        elif s[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            insta = BaseModel()
            insta.save()
            print(insta.id)

    ''' Show '''
    def do_show(self, line):
        ''' string representation of instance based on the class name & id'''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if s[0] not in classes:
                print("** class doesn't exist **")
            else:
                aux = s[0] + '.' + s[1]
                if str(aux) in models.storage.all():
                    print(models.storage.all()[aux])
                else:
                    print("** no instance found **")

    ''' destroy '''
    def do_destroy(self, line):
        '''' Deletes an instance based on the class name and id '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if s[0] not in classes:
                print("** class doesn't exist **")
            else:
                aux = s[0] + '.' + s[1]
                if str(aux) in models.storage.all():
                    models.storage.all().pop(aux)
                else:
                    print("** no instance found **")

    ''' show all objects '''

    def do_all(self, line):
        ''' string representation of all instances based or not on the class'''
        s = split(line)
        aux = []
        if len(s) == 0:
            for values in models.storage.all().values():
                aux.append(values.__str__())
        elif len(s) == 1:
            if s[0] not in classes:
                print("** class doesn't exist **")
                return
            for key, values in models.storage.all().items():
                temp = key.split('.')
                if temp[0] == s[0]:
                    aux.append(values.__str__())
        print(aux)

    ''' Update '''
    def do_update(self, line):
        ''' Updates instance based on class name & id by adding or upd att'''
        s = split(line)

        if len(s) == 0:
            print("** class name missing **")
            return
        if len(s) == 1:
            if s[0] not in classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return
        if len(s) == 2:
            if s[0] in classes and id_validator(s[1]):
                print("** attribute name missing **")
            elif s[0] in classes and id_validator(s[1]) is False:
                print("** no instance found **")
            elif s[0] not in classes:
                print("** class doesn't exist **")
            return
        if len(s) == 3:
            if s[0] in classes and id_validator(s[1]):
                print("** value missing **")
            elif s[0] in classes and id_validator(s[1]) is False:
                print("** no instance found **")
            elif s[0] not in classes:
                print("** class doesn't exist **")
            return
        if len(s) >= 4:
            if s[0] not in classes:
                print("** class doesn't exist **")
                return
            elif s[0] in classes and id_validator(s[1]) is False:
                print("** no instance found **")
                return
            elif s[0] in classes and id_validator(s[1]):
                aux = s[0] + "." + s[1]
                cpy = s[3]
                if is_float(s[3]):
                    cpy = float(s[3])
                if is_int(s[3]):
                    cpy = int(s[3])
                setattr(models.storage.all()[aux], s[2], cpy)
                models.storage.save()

    ''' Empty line '''

    def emptyline(self):
        ''' empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
