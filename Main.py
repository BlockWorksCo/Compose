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
import re
#import VT100FrontEnd
import SimpleFrontEnd





class EditingContext:
    """
    Cursor position
    """

    def __init__(self, backEnd, frontEnd,  x,y, numberOfLines ):
        """
        """
        self.x              = 0
        self.y              = 0
        self.linesX         = x
        self.linesY         = y
        self.backEnd        = backEnd
        self.frontEnd       = frontEnd
        self.numberOfLines  = numberOfLines        

        self.Update()


    def Update(self):
        """
        """
        self.lines = backEnd.GetLinesBetween( self.linesY, self.linesY+self.numberOfLines ) 


    def Display(self):
        """
        """
        self.frontEnd.ShowEditingContext(self)
        self.frontEnd.SetCursorPosition( self.x, self.y )


    def Save(self):
        """
        """
        backEnd.ReplaceLines( self.linesY, self.linesY+self.numberOfLines, self.lines )






class BackEnd:
    """
    File handling.
    grep -b "^" big.txt | sed -n 100000,100005p
    sed -n 100000,100005p big.txt
    """


    def __init__(self, fileName):
        """
        """
        self.fileName           = fileName
        self.indexTimestamp     = None


    def GetLinesBetween( self, start, end ):
        """
        dd if=yourfile ibs=1 skip=200 count=100
        Get one extra line so we can work out the line length by subtracting the starts
        TODO: What about last line in file?
        """
        inFile      = open(self.fileName)
        lines       = []
        offsets     = backEnd.GetByteOffsetsOfLines( start,end+1 )
        for lineNumber in range(len(offsets)-1):

            offset      = offsets[lineNumber]
            lineLength  = offsets[lineNumber+1] - offset

            inFile.seek(offset)
            line    = inFile.read(lineLength-1)
            lines.append( line )

        return lines


    def BuildIndex( self, fileName ):
        """
        """
        fullText        = open(fileName).read()

        lineOffsets     = [0]

        i  = fullText.find('\n')
        while i >= 0:
            lineOffsets.append(i+1)
            i = fullText.find( '\n', i+1 )

        lineOffsets.append( len(fullText) )
        return lineOffsets


    def Log( self, text):
        """
        """
        print(text)


    def GetByteOffsetsOfLines( self,  start, end ):
        """
        """
        modifiedTime    = os.path.getmtime(self.fileName)

        if self.indexTimestamp == None or self.indexTimestamp<modifiedTime:

            self.Log('<Index rebuild>')
            self.indexTimestamp     = modifiedTime
            self.offsetForLine      = self.BuildIndex( self.fileName )

        return self.offsetForLine[start:end]



    def ReplaceLines(self, start,end, lines ):
        """
        """
        offsets     = backEnd.GetByteOffsetsOfLines( start,end+1 )
        startOffset = offsets[0]
        endOffset   = offsets[-1]
        newFile     = self.fileName + '.new'

        #
        # Write the pre-start block
        # dd if=big.txt of=big.txt.new count=1 obs=5302843 skip=0 ibs=5302843
        #
        skip    = 0
        count   = startOffset
        #print(['dd','if='+self.fileName,'of='+newFile,'ibs=%d'%count,'obs=%d'%count,'skip=0','count=1'])
        subprocess.check_output( ['dd','if='+self.fileName,'of='+newFile,'ibs=%d'%count,'obs=%d'%count,'skip=0','count=1'] , stderr=subprocess.PIPE )

        #
        # Write the replaced lines.
        #
        outFile     = open(newFile, 'a+')
        outFile.seek( startOffset )
        for lineNumber in range(len(offsets)-1):

            offset      = offsets[lineNumber]
            lineLength  = offsets[lineNumber+1] - offset

            outFile.write( lines[lineNumber]+os.linesep )

        fileLength  = outFile.tell()
        outFile.close()

        #
        # Write the post-end block.
        #
        fileLength  = os.stat(newFile).st_size
        skip        = endOffset
        count       = self.offsetForLine[-1] - endOffset
        cmd         = 'tail --bytes=+%d %s >> %s'%(endOffset,self.fileName, newFile) 
        #print(cmd)
        output      = subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE )
        #cmd         = ['tail','--bytes=%d'count]
        #print(cmd)
        #subprocess.check_output( cmd )



if __name__ == "__main__":
    """
    """
    print('NiceText :o)')
    backEnd     = BackEnd( sys.argv[1] )
    #frontEnd    = VT100FrontEnd.VT100FrontEnd()
    frontEnd    = SimpleFrontEnd.SimpleFrontEnd()
    context1    = EditingContext( backEnd, frontEnd ,0,100000, 10 )

    context1.Display()
    context1.Update()
    context1.lines[0] = 'X'+context1.lines[0]
    context1.lines[9] = 'X'+context1.lines[9]
    context1.Save()
    #while True:
    #    frontEnd.GetUserInput()








