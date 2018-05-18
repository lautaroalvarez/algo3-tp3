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
/**** VERSION 1_0:
/****   - no guarda las instancias ya calculadas
/****   - trata de ir primero a gimnasios
/****   - no va a gimnasio si no hay pociones suficientes
/****   - no va a parada si tiene la mochila llena
/****   - no va a parada si no quedan gimnasios
/****
/**********************************************************/
/**********************************************************/

class ejercicio1 : ejercicio{
  private:
    int cant_gimnasios = gimnasios.size();
    int cant_poke = pokeparadas.size();
    int cant_total = cant_poke+cant_gimnasios; // n+m
    int version_podas = 0;

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

      gettimeofday(&time, NULL);
      tiempo_inicio = ((double)time.tv_sec * 1000000) + time.tv_usec;

      distanciaMinima = -1;

      //-- si ya nos dimos cuenta que la entrada no tenia solucion => ni corremos
      if (!entrada_invalida) {
        
        //--arma un vector de gimnasios y otro de paradas
        vector<int> indices_gimnasios;
        for (int i = 0; i < cant_gimnasios; i++) {          //O(n)
          indices_gimnasios.push_back(i);
        }
        vector<int> indices_paradas;
        for (int i = 0; i < cant_poke; i++) {               //O(m)
          indices_paradas.push_back(cant_gimnasios + i);
        }

        //--setea la cantidad de pociones inicial (después de visitar la primer pokeparada)
        int pociones_inicial = sumaSaturada(0, 3);

        tuple < double, vector<int> > camino_minimo;

        //--se toman cada una de las pokeparadas como iniciales 
        for (int i = 0; i < cant_poke; i++) {                                   //O(m)

          vector<int> indices_aux = indices_paradas;
          indices_aux.erase(indices_aux.begin()+i);

          vector<int> nuevo_camino;
          nuevo_camino.push_back(cant_gimnasios + i + 1);
          camino_minimo = calcular_instancia(nuevo_camino, indices_aux, indices_gimnasios, pociones_inicial);

        }

      }

      imprimir();
      gettimeofday(&time, NULL);
      tiempo_fin = ((double)time.tv_sec * 1000000) + time.tv_usec;
      tiempo_total += tiempo_fin - tiempo_inicio;
      //---------SALIDA---------
      //-- cantidad de gimnasios
      //-- cantidad de paradas
      //-- capacidad de la mochila
      //-- tiempo total
      //-- cantidad de instancias que visito
      //-- cantidad de instancias que calculo
      //-- tamaño del camino solucion
      //-- version de algoritmo (podas)
      //-- cantidad de podas 1 que entro
      //-- cantidad de podas 2 que entro
      //cout << cant_gimnasios << ", " << cant_poke << ", " << mochila << ", " << tiempo_total << ", " << cantidad_instancias_visitadas << ", " << cantidad_instancias_calculadas << ", " << solucion.size() << ", " << version_podas << ", " << cantidad_podas_1 << ", " << cantidad_podas_2;
      //cout << endl;
    }

    tuple< double, vector<int> > calcular_instancia(vector<int> camino_actual, vector<int> paradas_a_recorrer, vector<int> gimnasios_a_recorrer, int pociones) {

      double distancia_recorrida = calcularDistancia(camino_actual);

      int nodo_actual = camino_actual[camino_actual.size()-1] - 1;
      
      //--aumento la cantida de instancias visitadas
      cantidad_instancias_visitadas++;

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

        //-----------GIMNASIOS------------
        for (int i = 0; i < gimnasios_a_recorrer.size(); i++) {
          
          //-- si alcanzan las pociones
          if (get<2>(gimnasios[gimnasios_a_recorrer[i]]) <= pociones) {

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

          }

        }

        //-- se fija si ya tiene la mochila llena
        if (pociones < mochila) {
          
          //--calcula la nueva cantidad de pociones
          int nuevasPociones = sumaSaturada(pociones, 3);
          
          //-----------POKEPARADAS------------
          for (int i = 0; i < paradas_a_recorrer.size(); i++) {

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

          }

        } else {

          //-- aumento la cantidad de podas basicas
          cantidad_podas_1++;

        }
        
      }

      //-- se fija si con esta instancia se hizo un nuevo camino minimo
      if (get<0>(camino_minimo_parcial) >= 0 && (distanciaMinima < 0 || distanciaMinima > get<0>(camino_minimo_parcial) + distancia_recorrida)) {

        distanciaMinima = get<0>(camino_minimo_parcial) + distancia_recorrida;
        solucion = camino_actual;
        for (int i = 1; i < get<1>(camino_minimo_parcial).size(); i++) {
          solucion.push_back(get<1>(camino_minimo_parcial)[i]);
        }

      }

      return camino_minimo_parcial;
    }

    virtual ~ejercicio1 (){}

};


int main(int argc, char const *argv[]) {
  ejercicio1 nuevo = ejercicio1();
  nuevo.correr();
  return 0;
}