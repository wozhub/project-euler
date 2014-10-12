# include <stdio.h>

char aux_c[16];

int cadena(int numero) {
    sprintf(aux_c,"%d\n",numero);
    int suma=0, digito;
    short i;
    for (i=0; aux_c[i+1] != '\0'; i++) {
        digito = aux_c[i] - '0';
        suma += digito*digito; }
    return suma;
}

void main() {
    int i, cuenta = 0, aux_n;
    for (i=1; i < 10000000; i++) {
        aux_n = cadena(i);
        while ( 1 ) {
            if (aux_n==89) { cuenta++; break; }
            else if (aux_n==1) { break; }
            else { aux_n = cadena(aux_n); }
        }
    }

    printf("%d\n", cuenta);
}
