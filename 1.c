#include <stdio.h>

void main() {
    unsigned i;
    unsigned long suma=0;
    for (i=1;i<1000;i++) {
        if ( i%3 == 0 ) { printf("%d es multiplo de 3.\n",i,suma); suma+=i; }
        else if ( i%5 == 0 ) { printf("%d es multiplo de 5.\n",i,suma); suma+=i; } 
    }
    printf("%ld\n",suma);
}
