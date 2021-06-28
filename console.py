#!/usr/bin/python3
''' The console '''

import cmd
from models.base_model import BaseModel
from sys import argv
from shlex import split

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
        ''' Prints the string representation of an instance based on the class name and id '''
        
    ''' Empty line '''

    def emptyline(self):
        ''' empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
