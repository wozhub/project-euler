#include <stdio.h>

void main() {
    unsigned x=0,y=1,z=0;
    unsigned long suma=0;

    while ( (x+y) < 4000000 ) {
        z=x+y; x=y; y=z;

        if ( z%2==0 ) { 
            printf("%d ",z);
            suma+=z; }
    }
    printf("\n%ld\n",suma);
}
