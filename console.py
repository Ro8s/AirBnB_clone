#!/usr/bin/python3
''' The console '''

import cmd


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




if __name__ == '__main__':
    HBNBCommand().cmdloop()
