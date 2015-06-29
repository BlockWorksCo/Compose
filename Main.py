#
# Copyright (C) BlockWorks Consulting Ltd - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# Written by Steve Tickle <Steve@BlockWorks.co>, September 2014.
#

import sys
import re
import subprocess




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
    """


    def __init__(self, fileName):
        """
        """
        self.fileName   = fileName


    def GetLinesBetween( self, start, end ):
        """
        """
        output  = subprocess.check_output( ['sed','-n','%d,%dp'%(start,end),self.fileName] )
        return output






if __name__ == "__main__":
    """
    """
    print('NiceText :o)')
    backEnd     = BackEnd( sys.argv[1] )
    context1    = EditingContext( backEnd, 0,0 )

    print( backEnd.GetLinesBetween( 100000,100005 ) )












