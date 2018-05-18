#include <iostream>
#include <stdlib.h>
#include <tuple>
#include <vector>
#include "ejercicio.hpp"
#include <sys/time.h>

using namespace std;

// Tabu/GRASP

class ejercicio4 : ejercicio{
private:
  int cant_gimnasios;
  int cant_paradas;
  struct timeval time;
  double tiempo_total = 0;
  double tiempo_inicio, tiempo_fin;
  string codigo_vecindad = "1111";


public:
  ejercicio4 () : ejercicio(){}
  void correr(){
    //string codigo_caso;
    //cin >> codigo_caso;

    
    //gettimeofday(&time, NULL);
    //tiempo_inicio = ((double)time.tv_sec * 1000000) + time.tv_usec;
    
    //clock_t inicio = clock();
    cant_gimnasios = gimnasios.size();
    cant_paradas = pokeparadas.size();

    //-- si ya nos dimos cuenta que la entrada no tenia solucion => ni corremos
    if (!entrada_invalida) {

      // se toma una solucion auxiliar para ir almacenando un minimo
      vector<int> solucion_parcial;
      double dist_parcial = -1;

        //-- vamos a iniciar un goloso desde cada parada
        for (int p = 0; p < cant_paradas; p++) {

          //-- vamos a iniciar un goloso con cada criterio de eleccion de gimnasios
          //-- 0 -> mas cercano primero
          //-- 1 -> mas lejano primero
          //-- 2 -> mas pociones necesarias primero
          //-- 3 -> menos pociones necesarias primero
          for (int c = 0; c < 4; c++) {

            //----SOLUCION INICIAL -> un goloso que arranca en la parada p con el criterio de eleccion de gimnasios c
            int ranking;
            if(gimnasios.size() < 2){
              ranking = 1;
            }else{
              ranking = (int)gimnasios.size()*0.5;
            }
            calculaGoloso(cant_gimnasios + p, c, ranking);

            if (distanciaMinima > 0) {
              //----HEURISTICA
              busquedaLocal(codigo_vecindad);

              double dist_sol = calcularDistancia(solucion);

              if(dist_parcial < 0 || dist_sol < dist_parcial) {
                solucion_parcial = solucion;
                dist_parcial = dist_sol;
              }
            }
            
            if (clock() - inicio > 10000000) {
              // si estoy tardando mucho me salteo pokeparadas iniciales
              p += (int) cant_paradas*0.4;
              break;
            }

          }

        }
      solucion = solucion_parcial;
      distanciaMinima = calcularDistancia(solucion);
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
    //-- ejercicio
    //cout << fixed;
    //cout << codigo_caso << ", " << gimnasios.size() << ", " << pokeparadas.size() << ", " << mochila << ", " << tiempo_total << ", " << distanciaMinima << ", 4";
    //cout << endl;
  }

};

int main(int argc, char const *argv[]) {
  ejercicio4 nuevo = ejercicio4();
  nuevo.correr();
  return 0;
}
