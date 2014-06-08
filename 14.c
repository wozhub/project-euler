#include <stdio.h>

void main() {
    unsigned int empieza=1,n,cadena,maxn=1,maxc=1;
    
    while ( empieza < 1000000 ) {
        empieza++;

        n=empieza;
        cadena=1; //porque no cuento el 1

        while ( n>1 ) {
            if ( n%2 == 0 ) { n=n/2; }
            else { n=3*n+1; }
            cadena++;
        }
        
        if ( cadena > maxc ) {
            printf("%d produjo una cadena de %d numeros.\n",empieza,cadena);
            maxn=empieza;
            maxc=cadena;
        }

    }
}
