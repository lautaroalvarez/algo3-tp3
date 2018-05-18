#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include <math.h>
#include "ejercicio.hpp"
//#include "ejercicio2.cpp"
#include <sys/time.h>

using namespace std;

// Busqueda local

class ejercicio3 : ejercicio{
private:
  /* data */
  //struct timeval time;
  //double tiempo_total = 0;
  //double tiempo_inicio, tiempo_fin;

public:
  ejercicio3 () : ejercicio(){}

  void correr(){
    //string codigo_caso;
    string codigo_vecindades = "1111";
    
    //cin >> codigo_caso;
    
    //gettimeofday(&time, NULL);
    //tiempo_inicio = ((double)time.tv_sec * 1000000) + time.tv_usec;

    if (!entrada_invalida) {
      //--parámetro que indica que vecindades se usan
      //cin >> codigo_vecindades;

      //--calcula una solución inicial (goloso)
      golosoDeterministico();

      if (distanciaMinima > 0) {
        busquedaLocal(codigo_vecindades);
      }

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
    //-- cantidad de cambios que se hicieron
    //-- codigo de vecindades
    //cout << fixed;
//    cout << codigo_caso << ", " << gimnasios.size() << ", " << pokeparadas.size() << ", " << mochila << ", " << tiempo_total << ", " << distanciaMinima << ", " << cantidad_cambios << ", '" << codigo_vecindades << "'";
    //cout << codigo_caso << ", " << gimnasios.size() << ", " << pokeparadas.size() << ", " << mochila << ", " << tiempo_total << ", " << distanciaMinima << ", 3";
    //cout << endl;
  }

  virtual ~ejercicio3 (){};

};

int main(int argc, char const *argv[]) {
    ejercicio3 nuevo = ejercicio3();
    nuevo.correr();
  return 0;
}
