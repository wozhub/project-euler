#include <stdio.h>

void main() {
    unsigned long suma,numero=1,x;
    int divisores;

    while ( 1 ) {

        suma=0;
        for (x=1;x<numero;x++) { suma+=x; }
        
        divisores=0;
        for (x=1;x<=suma;x++) { 
            if ( suma%x==0 ) {
                divisores++;
            } }
    
        printf("El numero %ld tiene %d divisores.\n",suma,divisores);
        if (divisores > 500) { break; }

        numero++;

    }
}
//    if divisores>500:
//        break
