#include <stdio.h>

int factorial(int x) {
//d    printf("factorial(%d)\n", x);
    int factorial=1;
    int contador;

    for (contador=1; contador<=x; contador++) {   
        factorial=factorial*contador; }

    return factorial;
}

int suma_factorial_digitos(int x) {
//d    printf("suma_factorial_digitos(%d)\n", x);

    char aux[32];
    int suma = 0;

    sprintf(aux, "%d\n", x);

    short i;
    int digito;
    for (i=0; aux[i+1] != '\0'; i++) {
        digito = aux[i] - '0';
        suma += factorial(digito); 
    }
    
    return suma;
}

void main() {   
    // printf("%d\n", suma_factorial_digitos(145));
    
    int x = 2;

    while ( 1 ) {
        x += 1;

        if ( x == suma_factorial_digitos(x) ) {
            printf("%d\n",x); }
    }
}
