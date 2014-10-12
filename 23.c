#include <stdio.h>
#include "abundantes.h"

#define TOPE 2562

int noEsSumaAbundantes(int numero) {
    int i, j, suma;

    for (i=0; i<TOPE; i++) {
        if ( abundantes[i] > numero ) { break; }

        for (j=i; abundantes[j] < numero; j++) {
            suma = abundantes[i] + abundantes[j];

            if ( suma == numero ) {
                //printf("%d = %d + %d\n", numero, abundantes[i], abundantes[j]);
                return 0; }
            else if ( suma > numero ) { break; }
        }
    }

    //printf("%d!\n", numero);
    return 1;
}

void main() {

    int i, suma = 0;
    for (i=1; i<28125; i++) {
        if ( noEsSumaAbundantes(i) ) {
            printf("%d\n", i);
            suma += i; }
    }

    printf("\n\n%d\n", suma);
}
