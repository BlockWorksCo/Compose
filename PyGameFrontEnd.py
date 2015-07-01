#
# Copyright (C) BlockWorks Consulting Ltd - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# Written by Steve Tickle <Steve@BlockWorks.co>, June 2015.
#

import sys
import pygame



class PyGameFrontEnd:
    """
    """

    def __init__(self):
        """
        """
        pygame.init()

        self.width      = 500
        self.height     = 300
        self.screen = pygame.display.set_mode( (self.width,self.height), pygame.RESIZABLE )

        self.Display()



    def Clear(self):
        """
        """
        pass



    def SetCursorPosition(self, x,y):
        """
        """
        pass


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


    def Display( self ):
        """
        """
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        label   = myfont.render("Some text!", 1, (255,255,0))
        self.screen.blit( label, (100, 100))

        pygame.display.set_caption("NiceText :o)")
        pygame.display.flip()


    def GetUserInput(self):
        """
        """
        pygame.event.pump()
        event   = pygame.event.wait()

        if event.type == pygame.QUIT: 
            pygame.display.quit()

        elif event.type == pygame.VIDEORESIZE:

            width,height    = event.dict['size']
            self.width      = width
            self.height     = height
            self.screen = pygame.display.set_mode( (self.width,self.height), pygame.RESIZABLE )

            self.Display()


