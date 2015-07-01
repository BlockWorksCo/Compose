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

        self.width          = 500
        self.height         = 300
        self.textColour     = (255,255,255)
        #self.fontName       = "Comic Sans MS"
        self.fontName       = 'Calibri'
        self.fontSize       = 20
        self.lines          = []

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
        self.lines  = context.lines

        self.Display()


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
        myfont = pygame.font.SysFont( self.fontName, self.fontSize )
        #label   = myfont.render( "Some text!", 1, self.textColour )
        #self.screen.blit( label, (100, 100))


        lineNumber  = 0
        lineHeight  = self.fontSize
        for line in self.lines:

            lineText   = myfont.render( line, 1, self.textColour )
            self.screen.blit( lineText, (10, lineNumber*lineHeight))

            lineNumber  = lineNumber + 1


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


