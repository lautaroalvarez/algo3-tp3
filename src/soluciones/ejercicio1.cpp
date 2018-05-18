#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include "ejercicio.hpp"
#include <sys/time.h>

using namespace std;

// Backtracking

/**********************************************************/
/**********************************************************/
/****
/**** CONTIENE 4 VERSIONES:
/****
/****   Version 1:
/****     - guarda las instancias ya calculadas
/****     - trata de ir primero a gimnasios
/****     - no va a gimnasio si no hay pociones suficientes
/****     - no va a parada si tiene la mochila llena
/****     - no va a parada si no quedan gimnasios
/****
/****   Version 2:
/****     - todo lo de la version 1
/****     - chequea que la distancia de la instancia a calcular no sea mayor que la minima parcial ya calculada
/****     - chequea que la distancia de la instancia a calcular no sea mayor que la minima global ya calculada
/****
/****   Version 3:
/****     - todo lo de la version 2
/****     - ordena los gimnasios por distancia
/****     - ordena las paradas por distancia
/****
/****   Version 4:
/****     - todo lo de la version 3
/****     - utiliza una solucion golosa como primera cota superior
/****
/**********************************************************/
/**********************************************************/


class ejercicio1 : ejercicio{
  private:
    int cant_gimnasios = gimnasios.size();
    int cant_poke = pokeparadas.size();
    int cant_total = cant_poke+cant_gimnasios; // n+m
    vector<vector<vector<tuple<double, vector<int> > > > > instancias;
    int version_podas = 4;
    int num_rep = 0;


    /*------para experimentar-----*/
    double tiempo_total = 0;
    double tiempo_inicio, tiempo_fin;
    int cantidad_instancias_visitadas = 0;
    int cantidad_instancias_calculadas = 0;
    int cantidad_podas_1 = 0;
    int cantidad_podas_2 = 0;
    struct timeval time;
    /*----------------------------*/

  public:
    ejercicio1 () : ejercicio(){}
    void correr(){
      //int mejor_caso;
      //cin >> mejor_caso;
      //int parametro_extra;
      //cin >> parametro_extra;

      //-- lee la version de podas que se debe usar
      //----- si lee de un cat con pipe de un archivo va a leer eof y va a tomar la version por default
      //cin >> version_podas;
      //cin >> num_rep;

      //gettimeofday(&time, NULL);
      //tiempo_inicio = ((double)time.tv_sec * 1000000) + time.tv_usec;

      distanciaMinima = -1;

      //-- si ya nos dimos cuenta que la entrada no tenia solucion => ni corremos
      if (!entrada_invalida) {

        //--- calcula la cantidad de combinaciones de paradas y gimnasios necesarias (para las instancias)
        unsigned int cant_combinaciones_gimnasios_paradas = pow(2, cant_total)-1;

        //--- el formato de instancias es:
        //------ instancias[combinacion gimnasios paradas][pociones][nodo actual] = < distancia, camino >
        instancias = vector<vector<vector<tuple<double, vector<int> > > > >(cant_combinaciones_gimnasios_paradas + 1, vector<vector<tuple<double, vector<int> > > >(mochila + 1, vector<tuple<double, vector<int> > >(cant_total, tuple<double, vector<int> >(-2,vector<int>()))));
  
        //--arma un vector de gimnasios y otro de paradas
        vector<int> indices_gimnasios;
        for (int i = 0; i < cant_gimnasios; i++) {
          indices_gimnasios.push_back(i);
        }
        vector<int> indices_paradas;
        for (int i = 0; i < cant_poke; i++) {
          indices_paradas.push_back(cant_gimnasios + i);
        }

        //--setea la cantidad de pociones inicial (después de visitar la primer pokeparada)
        int pociones_inicial = sumaSaturada(0, 3);

        tuple < double, vector<int> > camino_minimo;

        //-- a partir de la version 4 hace un goloso previo para tomar como cota
        if (version_podas >= 4) {
          golosoDeterministico();
        }
  
        //--se toman cada una de las pokeparadas como iniciales 
        for (int i = 0; i < cant_poke; i++) {

          vector<int> indices_aux = indices_paradas;
          indices_aux.erase(indices_aux.begin()+i);

          vector<int> nuevo_camino;
          nuevo_camino.push_back(indices_paradas[i] + 1);
          camino_minimo = calcular_instancia(nuevo_camino, indices_aux, indices_gimnasios, pociones_inicial);
        }

      }

      imprimir();
      //gettimeofday(&time, NULL);
      //tiempo_fin = ((double)time.tv_sec * 1000000) + time.tv_usec;
      //tiempo_total += tiempo_fin - tiempo_inicio;
      //---------SALIDA DE EXPERIMENTACION---------
      //-- cantidad de gimnasios
      //-- cantidad de paradas
      //-- capacidad de la mochila
      //-- numero de repeticion
      //-- tiempo total
      //-- cantidad de instancias que visito
      //-- cantidad de instancias que calculo
      //-- tamaño del camino solucion
      //-- version de algoritmo (podas)
      //-- cantidad de podas 1 que entro
      //-- cantidad de podas 2 que entro
      //-- parametro extra (segun el caso)
      //cout << fixed;
//      cout << cant_gimnasios << ", " << cant_poke << ", " << mochila << ", " << num_rep << ", " << tiempo_total << ", " << cantidad_instancias_visitadas << ", " << cantidad_instancias_calculadas << ", " << solucion.size() << ", " << version_podas << ", " << cantidad_podas_1 << ", " << cantidad_podas_2 << ", " << parametro_extra;
      //cout << parametro_extra << ", " << gimnasios.size() << ", " << pokeparadas.size() << ", " << mochila << ", " << tiempo_total << ", " << distanciaMinima << ", 1";
      //cout << endl;
    }

    tuple< double, vector<int> > calcular_instancia(vector<int> camino_actual, vector<int> paradas_a_recorrer, vector<int> gimnasios_a_recorrer, int pociones) {

      double distancia_recorrida = calcularDistancia(camino_actual);

      int nodo_actual = camino_actual[camino_actual.size()-1] - 1;

      //--calcula el número de instancia actual
      unsigned int comb_instancia = calcular_num_combinacion(paradas_a_recorrer, gimnasios_a_recorrer);
      
      //--aumento la cantida de instancias visitadas
      cantidad_instancias_visitadas++;

      //--se fija si ya calculó la instancia actual
      if (get<0>(instancias[comb_instancia][pociones][nodo_actual]) == -2) {
        //--no tiene calculada esta instancia

        //--aumento la cantida de instancias calculadas
        cantidad_instancias_calculadas++;

        //-- crea el camino parcial y lo setea como invalido
        tuple < double, vector<int> > camino_minimo_parcial;
        get<0>(camino_minimo_parcial) = -1;

        //--- se fija si quedan gimnasios por recorrer
        if (gimnasios_a_recorrer.size() == 0) {

          //-- aumento la cantidad de podas basicas
          cantidad_podas_1++;

          //-- si no quedan gimnasios termino
          get<0>(camino_minimo_parcial) = 0;
          get<1>(camino_minimo_parcial).insert(get<1>(camino_minimo_parcial).begin(), nodo_actual+1);
        
        } else {

          tuple < double, vector<int> > camino_minimo_aux;

          //--a partir de la version 3 ordena los vecinos
          if (version_podas >= 3) {

            //--ordena los gimnasios y paradas por distancia
            ordernar_por_distancia(nodo_actual, gimnasios_a_recorrer);
            ordernar_por_distancia(nodo_actual, paradas_a_recorrer);

          }

          //-----------GIMNASIOS------------
          for (int i = 0; i < gimnasios_a_recorrer.size(); i++) {
            
            //-- si alcanzan las pociones
            if (get<2>(gimnasios[gimnasios_a_recorrer[i]]) <= pociones) {
              //-- a partir de la version 2 se fija
              //-- si la distancia al gimnasio es menor que el minimo parcial de la instancia actual
              //-- y si la distancia al gimnasio es menor que el minimo parcial global
              if (version_podas <= 1 || ( get<0>(camino_minimo_parcial) < 0 || get<0>(camino_minimo_parcial) > distancias[nodo_actual][gimnasios_a_recorrer[i]] ) && ( distanciaMinima < 0 || distanciaMinima > distancias[nodo_actual][gimnasios_a_recorrer[i]] ) ) {

                //-- saca el gimnasio de los "a recorrer"
                vector<int> gimnasios_aux = gimnasios_a_recorrer;
                gimnasios_aux.erase(gimnasios_aux.begin() + i);

                //-- crea un vector de camino para pasar como parametro a la nueva instancia
                vector<int> camino_actual_aux = camino_actual;

                camino_actual_aux.push_back(gimnasios_a_recorrer[i] + 1);
                
                //--calcula la nueva distancia
                double nuevaDistancia = calcularDistancia(camino_actual_aux);

                //-- llama a calcular la instancia siguiente
                camino_minimo_aux = calcular_instancia(camino_actual_aux, paradas_a_recorrer, gimnasios_aux, pociones - get<2>(gimnasios[gimnasios_a_recorrer[i]]));

                if (get<0>(camino_minimo_aux) >= 0) {
                  get<1>(camino_minimo_aux).insert(get<1>(camino_minimo_aux).begin(), nodo_actual + 1);
                  get<0>(camino_minimo_aux) = calcularDistancia(get<1>(camino_minimo_aux));

                  //-- si el camino parcial no fue seteado ó el camino actual es menor que el parcial
                  if (get<0>(camino_minimo_parcial) < 0 || get<0>(camino_minimo_aux) < get<0>(camino_minimo_parcial)) {
                  
                    //-- tenemos un nuevo mínimo
                    camino_minimo_parcial = camino_minimo_aux;
                  
                  }
                }

              } else {

                //-- aumenta la cantidad de podas 2
                cantidad_podas_2++;

              }

            }

          }

          //-- se fija si ya tiene la mochila llena
          if (pociones < mochila) {
            
            //--calcula la nueva cantidad de pociones
            int nuevasPociones = sumaSaturada(pociones, 3);
            
            //-----------POKEPARADAS------------
            for (int i = 0; i < paradas_a_recorrer.size(); i++) {

              //-- a partir de la version 2 se fija
              //-- si la distancia a la parada es menor que el minimo parcial de la instancia actual
              //-- y si la distancia a la parada es menor que el minimo parcial global
              if ( version_podas <= 1 || ( ( get<0>(camino_minimo_parcial) < 0 || get<0>(camino_minimo_parcial) > distancias[nodo_actual][paradas_a_recorrer[i]] ) && ( distanciaMinima < 0 || distanciaMinima > distancias[nodo_actual][paradas_a_recorrer[i]] ) ) ) {

                //-- saca la parada de las "a recorrer"
                vector<int> paradas_aux = paradas_a_recorrer;
                paradas_aux.erase(paradas_aux.begin() + i);

                //-- crea un vector de camino para pasar como parametro a la nueva instancia
                vector<int> camino_actual_aux = camino_actual;
                camino_actual_aux.push_back(paradas_a_recorrer[i] + 1);

                //-- llama a calcular la instancia siguiente
                camino_minimo_aux = calcular_instancia(camino_actual_aux, paradas_aux, gimnasios_a_recorrer, nuevasPociones);

                if (get<0>(camino_minimo_aux) >= 0) {
                  get<1>(camino_minimo_aux).insert(get<1>(camino_minimo_aux).begin(), nodo_actual + 1);
                  get<0>(camino_minimo_aux) = calcularDistancia(get<1>(camino_minimo_aux));

                  //-- si el camino parcial no fue seteado ó el camino actual es menor que el parcial
                  if (get<0>(camino_minimo_parcial) < 0 || get<0>(camino_minimo_aux) < get<0>(camino_minimo_parcial)) {
                    
                    //-- tenemos un nuevo mínimo
                    camino_minimo_parcial = camino_minimo_aux;
                  
                  }

                }

              } else {

                //-- aumenta la cantidad de podas 2
                cantidad_podas_2++;

              }

            }

          } else {

            //-- aumenta la cantidad de podas 1
            cantidad_podas_1++;

          }
          
        }

        instancias[comb_instancia][pociones][nodo_actual] = camino_minimo_parcial;
      
      }

      //-- se fija si con esta instancia se hizo un nuevo camino minimo
      if (get<0>(instancias[comb_instancia][pociones][nodo_actual]) >= 0 && (distanciaMinima < 0 || distanciaMinima > get<0>(instancias[comb_instancia][pociones][nodo_actual]) + distancia_recorrida)) {

        distanciaMinima = get<0>(instancias[comb_instancia][pociones][nodo_actual]) + distancia_recorrida;
        solucion = camino_actual;
        for (int i = 1; i < get<1>(instancias[comb_instancia][pociones][nodo_actual]).size(); i++) {
          solucion.push_back(get<1>(instancias[comb_instancia][pociones][nodo_actual])[i]);
        }

      }

      return instancias[comb_instancia][pociones][nodo_actual];
    }

    int calcular_num_combinacion(vector<int> pards, vector<int> gims) {
      //-- calcula el número de combinación de nodos
      int num_combinacion = 0;
      for (int i = 0; i < gims.size(); i++) {
        num_combinacion += pow(2, gims[i]);
      }
      for (int i = 0; i < pards.size(); i++) {
        num_combinacion += pow(2, pards[i]);
      }
      
      return num_combinacion;
    }

    void ordernar_por_distancia(int nodo_actual, vector<int> & vecinos) {
      //--ordena solo por distancia
      for (int i = 1; i < vecinos.size(); i++) {
        int j = i;
        while (j > 0 && distancias[nodo_actual][vecinos[j]] < distancias[nodo_actual][vecinos[j-1]]) {
          int aux = vecinos[j-1];
          vecinos[j-1] = vecinos[j];
          vecinos[j] = aux;
          j--;
        }
      }
    }

    virtual ~ejercicio1 (){}

};


int main(int argc, char const *argv[]) {
  ejercicio1 nuevo = ejercicio1();
  nuevo.correr();
  return 0;
}