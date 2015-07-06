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
import PyGameFrontEnd
import BackEnd



if __name__ == "__main__":
    """
    """
    print('Compose! :o)')
    
    backEnd     = BackEnd.BackEnd( sys.argv[1] )
    frontEnd    = PyGameFrontEnd.PyGameFrontEnd( backEnd )

    while True:
        frontEnd.GetUserInput()








