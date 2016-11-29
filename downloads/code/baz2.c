#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
 setuid( 1005 );
 system("/usr/bin/id");
 system( "/bin/sh -i" );
}
