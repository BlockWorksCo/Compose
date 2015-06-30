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




class EditingContext:
    """
    Cursor position
    """

    def __init__(self, backEnd,  x,y ):
        """
        """
        self.x          = x
        self.y          = y
        self.backEnd    = backEnd







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






if __name__ == "__main__":
    """
    """
    print('NiceText :o)')
    backEnd     = BackEnd( sys.argv[1] )
    context1    = EditingContext( backEnd, 0,0 )

    #for line in backEnd.GetLinesBetween( 100000,100005 ):
    #print(backEnd.GetByteOffsetsOfLines( 100000,100005 ))
    i = 0
    for line in backEnd.GetLinesBetween( 100000,100005 ):
        print( '%05d) %s'%(i,line) )
        i = i+1












