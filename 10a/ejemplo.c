/*
 * Info I - Ing. Martin Marino
 * TP de la clase 2013/06/17
 * David Vinazza - Curso R1041 (Lunes 14:15, Medrano)
*/

#include <stdio.h>          //scanf y printf
#include "estructuras.h"    //los structs
#include "funciones.h"      //para manejar la lista, sus elementos y los structs ordenados

#define TOPE 100000

int main() {
    t_elemento *e;
    int numero,contador;

    t_manipulador *naturales = nuevoManipulador();

    t_manipulador *primos = nuevoManipulador();
    agregarElemento(primos,nuevoElemento(2),-1);

    unsigned long i; //me armo una lista con los naturales impares
    for (i=3;i<=TOPE;i+=2) { agregarElemento(naturales,nuevoElemento(i),-1); }

    printf("Naturales: %d\n",naturales->cantidad);
    printf("Primos: %d\n",primos->cantidad);

    while ( naturales->cantidad > 0 ) {
        e=listaPop(naturales);
     
        agregarElemento(primos,e,-1);
    
        numero=e->numero;    
        contador=0;
        if ( numero*2<TOPE ) {
            for (i=2; numero<TOPE; i++) {
                numero=e->numero*i;
                borrarNumero(naturales,numero);
                contador++;
            }
            printf("Borre los %d multiplos de %d debajo de %d\n",contador,e->numero,TOPE);
        }
    }
    printf("\n");
    
    printf("Naturales: %d\n",naturales->cantidad);
    printf("Primos: %d\n",primos->cantidad);

//    verLista(primos);
//    borrarLista(lista);
};

borrarNumero(t_manipulador *l, int n) {
    t_elemento *e=l->primero;
    int pos=0;

    while ( e != NULL ) {
        if ( e->numero==n ) {
            borrarElemento(l,pos);
            break;
        }
        pos+=1;
        e=e->siguiente;
    }
}
