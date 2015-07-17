

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>



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
        indexFileHandle  = open( argv[2], O_RDONLY );
        if( indexFileHandle != -1 )
        {
            //
            //
            //
            uint32_t extractLineStart    = atoi( argv[3] );
            uint32_t extractLineEnd      = atoi( argv[4] );

            uint32_t    start   = 0;
            lseek( indexFileHandle, extractLineStart*sizeof(uint32_t), SEEK_SET );
            read( indexFileHandle, &start, sizeof(uint32_t) );

            uint32_t    end     = 0;
            lseek( indexFileHandle, extractLineEnd*sizeof(uint32_t), SEEK_SET );
            read( indexFileHandle, &end, sizeof(uint32_t) );

            //printf("%d = %d\n", extractLineStart, start );
            //printf("%d = %d\n", extractLineEnd, end );


            //
            //
            //
            #define BLOCK_SIZE  (1024*1024)
            ssize_t             offset                  = 0;
            static uint8_t      block[BLOCK_SIZE]       = {0};
            static uint32_t     lineOffsets[BLOCK_SIZE] = {0};
            uint32_t            total                   = 0;
            ssize_t             bytesRead               = 0;

            //
            // 
            //
            lseek( fileHandle, start, SEEK_SET );
            do
            {
                uint32_t    bytesToRead     = end - (start+total);
                if(bytesToRead > sizeof(block) )
                {
                    bytesToRead     = sizeof(block);
                }

                bytesRead   = read( fileHandle, &block[0], bytesToRead ); 
                write( 1, &block[0], bytesRead );
                total       += bytesRead;

            } while( total < (end-start) );

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



