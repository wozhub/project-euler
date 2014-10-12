#include <stdio.h>

/*
 raiz 2
         1          2         5         12        29
    1 + --- ;  1 + --- ; 1 + --- ; 1 + --- ; 1 + ---
         2          5         12        29        70
*/

int cuenta_digitos(unsigned long long n) {
    int c = 0;
    do { c++; n = n/10; } while (n != 0);
    return c;
}

// p = profundidad
unsigned long long int denominador(int p) {
    // Casos base para la recursividad
    if (p == 0) { return 1; }
    else if (p < 0) { return 0; }

    // El denominador es dos veces el anterior mas el anterior del anterior
    else { return 2 * denominador(p-1) + denominador(p-2); }
}

unsigned long long int numerador(int p) {
    return (denominador(p-1) + denominador(p));
}

void main() {
    int i, total=0;
    unsigned long long int num, den;

    for (i=0; i<1000; i++) {

        num = numerador(i);
        den = denominador(i);

        if (cuenta_digitos(num) > cuenta_digitos(den)) {
            printf("%lld / %lld\n", numerador(i), denominador(i));
            total++;
        }
    }
       
    printf("\n%d\n", total);
}
