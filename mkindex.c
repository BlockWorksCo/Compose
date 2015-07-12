

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>




//
//
//
int main( int argc, char* argv[] )
{
    int     exitCode    = -1;
    int     fileHandle  = -1;

    fileHandle  = open( argv[1], O_RDONLY );
    if( fileHandle != -1 )
    {
        //
        //
        //
        ssize_t     offset              = 0;
        uint8_t     block[1024*1024] = {0};
        ssize_t     bytesRead           = 0;

        printf("%09d\n", 0);
        do
        {
            bytesRead           = read( fileHandle, &block[0], sizeof(block) );
            if(bytesRead > 0)
            {
                for(uint32_t i=0; i<bytesRead; i++)
                {
                    if( block[i] == '\n' )
                    {
                        printf("%09zd\n", i+offset+1 );
                    }
                }
            }
            offset  += bytesRead;            

        } while( bytesRead > 0 );

        close( fileHandle );
        exitCode    = 0;
    }
    else
    {
        //
        //
        //
        printf( "Open failure.\n" );
    }

    return exitCode;
}



