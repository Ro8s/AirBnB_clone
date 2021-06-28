#!/usr/bin/python3
''' The console '''

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from shlex import split


class HBNBCommand(cmd.Cmd):
    ''' El console '''

    prompt = '(hbnb) '
    storage = FileStorage()
    objects = storage.all()
    classes = {"BaseModel": BaseModel}

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
        ''' Prints the string representation of an instance based on the class name and id '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in HBNBCommand.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            aux = s[0] + '.' + s[1]
            if str(aux) in HBNBCommand.objects:
                print(HBNBCommand.objects[aux])
            else:
                print("** no instance found **")

    ''' destroy '''
    def do_destroy(self, line):
        '''' Deletes an instance based on the class name and id '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in HBNBCommand.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            aux = s[0] + '.' + s[1]
            if str(aux) in HBNBCommand.objects:
                del HBNBCommand.objects[aux]
                
    ''' Empty line '''

    def emptyline(self):
        ''' empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
