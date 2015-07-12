

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <stdio.h>


int main( int argc, char* argv[] )
{
    int     exitCode    = -1;
    int     fileHandle  = -1;

    fileHandle  = open( argv[1], O_RDONLY );
    if( fileHandle != -1 )
    {
        close( fileHandle );
        exitCode    = 0;
    }
    else
    {
        printf( "Open failure.\n" );
    }

    return exitCode;
}



