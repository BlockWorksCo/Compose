

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
    int     exitCode            = -1;
    int     fileHandle          = -1;
    int     indexFileHandle     = -1;


    fileHandle  = open( argv[1], O_RDONLY );
    if( fileHandle != -1 )
    {
        indexFileHandle  = open( argv[2], O_CREAT|O_RDWR|O_TRUNC, 0666 );
        if( indexFileHandle != -1 )
        {
            //
            //
            //
            #define BLOCK_SIZE                  (1024*128)
            ssize_t             offset                  = 0;
            static uint8_t      block[BLOCK_SIZE]       = {0};
            static uint32_t     lineOffsets[BLOCK_SIZE] = {0};
            uint32_t            numberOfLineOffsets     = 0;
            ssize_t             bytesRead               = 0;

            //
            // Write line 0
            //
            lineOffsets[numberOfLineOffsets++]  = 0;
            write( indexFileHandle, &lineOffsets[0], sizeof(uint32_t)*numberOfLineOffsets );

            //
            // Write all the other lines.
            //
            do
            {
                bytesRead           = read( fileHandle, &block[0], sizeof(block) );                
                if(bytesRead > 0)
                {
                    numberOfLineOffsets = 0;
                    for(uint32_t i=0; i<bytesRead; i++)
                    {
                        if( block[i] == '\n' )
                        {
                            lineOffsets[numberOfLineOffsets++]  = offset+i+1;
                        }
                    }

                    write( indexFileHandle, &lineOffsets[0], sizeof(uint32_t)*numberOfLineOffsets );
                }
                offset  += bytesRead;            

            } while( bytesRead > 0 );

            close(indexFileHandle);
        }
        else
        {
            printf("Creat failure.\n");            
        }

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



