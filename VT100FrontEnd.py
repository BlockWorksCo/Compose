#
# Copyright (C) BlockWorks Consulting Ltd - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# Written by Steve Tickle <Steve@BlockWorks.co>, June 2015.
#

import sys
import re
import subprocess
import os
import tty
import re



class VT100FrontEnd:
    """
    """

    def __init__(self, context):
        """
        """

        self.context                = context

        tty.setraw( sys.stdin.fileno() )

        r,c     = self.GetScreenSize()
        self.rows       = r
        self.columns    = c


    def Clear(self):
        """
        """
        sys.stdout.write('\033[2J')
        sys.stdout.write('\033[H')



    def SetCursorPosition(self, x,y):
        """
        """
        sys.stdout.write( '\033[%d;%dH'%(y+1,x+1) )


    def ShowEditingContext(self, context):
        """
        """
        self.Clear()

        lineNumber  = 0
        for line in context.lines:

            self.SetCursorPosition( 3,lineNumber )
            print(line)
            lineNumber  = lineNumber + 1


    def GetScreenSize(self):
        """
        """        
        sys.stdout.write('\033[19t')
        #sys.stdout.flush()

        byte    = ''
        result  = ''

        while byte != 't':
            byte    = sys.stdin.read(1)
            print('-%s-'%result)
            result  = result + byte


        rowsText,columnsText    = re.compile('9;([0-9]+);([0-9]+)').findall(result)[0]
        rows    = int(rowsText)
        columns = int(columnsText)

        return rows,columns


    def GetUserInput(self):
        """
        """
        key     = ord(sys.stdin.read(1))
        self.SetCursorPosition(0, self.rows-1)
        sys.stdout.write('> %02x  '%(key) )

        if key == 0x1b:
            sys.exit(0)


