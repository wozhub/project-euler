#include <stdio.h>

int sumaDivisores(int numero) {
    int suma=0;
    unsigned int i;

    for (i=1;i<numero;i++) {
        if (numero%i ==0) {
            suma+=i;
        }
    }

    return suma;
}

void main() {

    unsigned int i,a1,a2;
    short salida;
    long suma=0;

    for (i=1;i<28123;i++) {
        if ( i%2==0 && i>30 ) { i++; }; // 24 + 6
        salida=0;

        for (a1=1; a1<i;a1++) { 
            if ( sumaDivisores(a1) > a1 ) { //a1 es abundante
                for (a2=2;a2<=a1;a2++) {
                    if ( sumaDivisores(a2) > a2 ) { //a2 es abundante
                        if ( a1+a2==i ) { 
                            printf("%d=%d+%d\n",i,a1,a2);
                            salida=1; break; }
                    }   
                
                if ( salida == 1) { break; }
                }   
            }
        }
        if ( salida == 0) { suma+=i; printf("%d\n",i);}
    }

    printf("!!!!!!!!!!!!!!!!!\n%d\n",suma);
}
