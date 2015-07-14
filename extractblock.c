

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>




//
//
//
void CopyBlock( int destinationFd, int sourceFd, uint32_t blockSize)
{
    static uint8_t      block[1024*1024*32] = {0};
    uint32_t            totalCopied         = 0;
    uint32_t            bytesRead           = 0;
    uint32_t            bytesToRead         = 0;


    do
    {
        bytesToRead         = sizeof(block);
        if( (totalCopied+bytesToRead) > blockSize )
        {
            bytesToRead     = blockSize - totalCopied;
        }

        bytesRead           = read( sourceFd, &block[0], bytesToRead );                
        if(bytesRead > 0)
        {
            write( destinationFd, &block[0], bytesRead );        
        }

        totalCopied     += bytesRead;

    } while(totalCopied < blockSize );
   
}


//
// extractblock inputFile outputFile extractStart extractEnd
//
int main( int argc, char* argv[] )
{
    int         exitCode            = -1;
    int         inputFileHandle     = -1;
    int         outputFileHandle    = -1;
    uint32_t    extractStart        = 0;
    uint32_t    extractEnd          = 0;

    //
    //
    //
    extractStart    = atoi( argv[3] );
    extractEnd      = atoi( argv[4] );

    //
    //
    //
    inputFileHandle  = open( argv[1], O_RDONLY );
    if( inputFileHandle != -1 )
    {
        outputFileHandle  = open( argv[2], O_CREAT|O_RDWR|O_TRUNC, 0666 );
        if( outputFileHandle != -1 )
        {
            printf("%d %d\n", extractStart, extractEnd );

            lseek( outputFileHandle, 0, SEEK_SET );
            lseek( inputFileHandle,  extractStart, SEEK_SET );
            CopyBlock( outputFileHandle, inputFileHandle, extractEnd-extractStart );

            exitCode    = 0;
            close( outputFileHandle );
        }

        close( inputFileHandle );
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



