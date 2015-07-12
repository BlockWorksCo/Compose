


import struct
import sys




def GetLineOffset( indexFileName, lineNumber ):
    """
    """
    f   = open( indexFileName )
    f.seek(lineNumber*4)
    indexData       = f.read(4)
    offset          = struct.unpack('I', indexData)

    return offset[0]

if __name__ == '__main__':
    """
    """
    for i in range(10):
        print( GetLineOffset( sys.argv[1],i ) )



