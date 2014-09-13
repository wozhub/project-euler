# include <stdio.h>
# include "primos.h"

int cuentaConsecutivos(numero, inicio) {
    
    if (numero < primos[inicio]) { return 0; }

    int suma = 0;
    int i;
    for (i=inicio;;i++) {
        suma += primos[i];
        if (suma > numero) { return cuentaConsecutivos(numero, inicio+1); }
        else if (suma == numero) { return i-inicio+1; }
    }
}

void main() {
//    printf("%d\n", cuentaConsecutivos(41, 0));
//    printf("%d\n", cuentaConsecutivos(953, 0));

    int max_numero = 0;
    int max_cuenta = 0;
    int i, cuenta;

    for (i=0; primos[i] < 1000000; i++) {

        cuenta = cuentaConsecutivos(primos[i], 0);

        if ( cuenta > max_cuenta ) {
            max_cuenta = cuenta;
            max_numero = primos[i]; }
    }

    printf("%d: %d\n", max_numero, max_cuenta);
}
