#!/usr/bin/python3
''' The console '''

import cmd
import models
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


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
        print("")
        return True

    ''' Create '''

    def do_create(self, line):
        '''  Creates a new instance of BaseModel '''
        s = split(line)
        if len(s) < 1:
            print("** class name missing **")
        elif s[0] not in classes:
            print("** class doesn't exist **")
        else:
            insta = classes[s[0]]()
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
                    models.storage.save()
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

    ''' Advanced tasks baby shark '''

    def default(self, line):
        '''default method overriden '''
        s = line.split('.')
        if s[0] not in classes or len(s) != 2:
            print("*** unkown syntax: {}". format(s[0]))
            return
        if s[1] == 'all()':
            aux = []
            for key, values in models.storage.all().items():
                cls = key.split('.')
                if cls[0] == s[0]:
                    aux.append(values.__str__())
            print(aux)
            return
        if s[1] == 'count()':
            count = 0
            for key in models.storage.all():
                cls = key.split('.')
                if cls[0] == s[0]:
                    count += 1
            print(count)
            return
        if s[1][0:5] == "show(" and s[1][-1] == ')':
            new = s[1].split('(')
            obj_id = new[1][:-2]
            obj_id = obj_id[1:]
            if id_validator(obj_id):
                obj_key = s[0] + '.' + obj_id
                if obj_key in models.storage.all():
                    print(models.storage.all()[obj_key])
                else:
                    print("** no instance found **")
            else:
                print("** no instance found **")
            return
        if s[1][0:8] == "destroy(" and s[1][-1] == ')':
            des = s[1].split('(')
            des_id = des[1][:-2]
            des_id = des_id[1:]
            if id_validator(des_id):
                des_key = s[0] + '.' + des_id
                if des_key in models.storage.all():
                    models.storage.all().pop(des_key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** no instance found **")
            return
        if s[1][0:7] == 'update(' and s[1][-1] == ')':
            if s[1][-2] == '}': #Caso id, {diccionario} (ej 16)
                t = s[1].split('"', 2)
                dic = eval(t[2][2:-1])
                for key, values in dic.items():
                    parse = s[0] + " " + t[1] + " " + str(key) + " " + str(values)
                    self.do_update(parse)
                return
            else: #Corte ejercicio 15 sacas
                h = s[1].split('"')
                linea = s[0] + " " + h[1] + " " + str(h[3]) + " " + str(h[5])
                self.do_update(linea)
                return

    ''' Empty line '''

    def emptyline(self):
        ''' empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
