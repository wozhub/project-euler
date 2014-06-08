/*
 * Info I - Ing. Martin Marino
 * TP de la clase 2013/06/17
 * David Vinazza - Curso R1041 (Lunes 14:15, Medrano)
*/

#include <stdio.h>          //scanf y printf
#include "estructuras.h"    //los structs
#include "funciones.h"      //para manejar la lista, sus elementos y los structs ordenados

//#define TOPE 2000000
#define TOPE 10

int main() {
    t_elemento *e;
    unsigned i, suma=2;

    t_manipulador *primos = nuevoManipulador();
    agregarElemento(primos,nuevoElemento(2),-1);

    for (i=3;i<TOPE;i+=2) {
	if ( esPrimo(primos,i) ) {
	    agregarElemento(primos,nuevoElemento(i),-1);
        suma+=i;
        } 
    }
    
    printf("Primos: %d\n",primos->cantidad);
    printf("Suma: %d\n",suma);

//    verLista(primos);
//    borrarLista(lista);
};

int esPrimo(t_manipulador *l, unsigned long i) {
    t_elemento *aux=l->primero;

    while ( aux != NULL ) {
	if ( i%aux->numero==0 ) { return 0; }
	aux=aux->siguiente;
    }
    return 1;
}
