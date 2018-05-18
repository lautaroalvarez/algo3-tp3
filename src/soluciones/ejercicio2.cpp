#include <iostream>
#include <tuple>
#include <vector>
#include "ejercicio.hpp"
#include <sys/time.h>

using namespace std;

// Goloso

class ejercicio2 : ejercicio{
private:
  /* data */
  //struct timeval time;
  //double tiempo_total = 0;
  //double tiempo_inicio, tiempo_fin;

public:
  ejercicio2 () : ejercicio(){}

  void correr() {
    //int codigo_caso;
    //cin >> codigo_caso;

    //gettimeofday(&time, NULL);
    //tiempo_inicio = ((double)time.tv_sec * 1000000) + time.tv_usec;

    if (!entrada_invalida) {
      golosoDeterministico();
    }
    imprimir();
    //gettimeofday(&time, NULL);
    //tiempo_fin = ((double)time.tv_sec * 1000000) + time.tv_usec;
    //tiempo_total += tiempo_fin - tiempo_inicio;
    //---------SALIDA---------
    //-- codigo de caso
    //-- cantidad de gimnasios
    //-- cantidad de paradas
    //-- capacidad de la mochila
    //-- tiempo total
    //-- distancia del camino solucion
    //-- ejericio
    //cout << fixed;
    //cout << codigo_caso << ", " << gimnasios.size() << ", " << pokeparadas.size() << ", " << mochila << ", " << tiempo_total << ", " << distanciaMinima << ", 2";
    //cout << endl;
    //cout << tiempo_total << endl;
    return;
  }

  virtual ~ejercicio2 (){};

};

int main(int argc, char const *argv[]) {
  ejercicio2 nuevo = ejercicio2();
  nuevo.correr();

  return 0;
}
