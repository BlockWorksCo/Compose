

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <fcntl.h>




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
// replaceblock inputFile outputFile fileToInsert replaceStart replaceEnd
//
int main( int argc, char* argv[] )
{
    int         exitCode            = -1;
    int         inputFileHandle     = -1;
    int         outputFileHandle    = -1;
    int         insertFileHandle    = 0;
    uint32_t    replaceStart        = 0;
    uint32_t    replaceEnd          = 0;
    uint32_t    insertSize          = 0;
    uint32_t    inputSize           = 0;

    //
    //
    //
    struct stat     fileData;
    stat( argv[3], &fileData );
    insertSize  = fileData.st_size;

    stat( argv[1], &fileData );
    inputSize  = fileData.st_size;

    //
    //
    //
    replaceStart    = atoi( argv[4] );
    replaceEnd      = atoi( argv[5] );

    //
    //
    //
    inputFileHandle  = open( argv[1], O_RDONLY );
    if( inputFileHandle != -1 )
    {
        outputFileHandle  = open( argv[2], O_CREAT|O_RDWR|O_TRUNC, 0666 );
        if( outputFileHandle != -1 )
        {
            insertFileHandle  = open( argv[3], O_RDONLY );
            if( insertFileHandle != -1 )
            {
                printf("%d %d %d\n", replaceStart, replaceEnd, insertSize );

                posix_fallocate( outputFileHandle, 0, 0, inputSize+insertSize );

                lseek( outputFileHandle, 0, SEEK_SET );
                lseek( inputFileHandle,  0, SEEK_SET );
                CopyBlock( outputFileHandle, inputFileHandle, replaceStart );

                lseek( outputFileHandle,  replaceStart, SEEK_SET );
                lseek( insertFileHandle,  0,            SEEK_SET );
                CopyBlock( outputFileHandle, insertFileHandle, insertSize );

                lseek( outputFileHandle, replaceStart+insertSize,   SEEK_SET );
                lseek( inputFileHandle,  replaceEnd,                SEEK_SET );
                CopyBlock( outputFileHandle, inputFileHandle, inputSize-replaceEnd );

                exitCode    = 0;
                close( insertFileHandle );
            }

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



