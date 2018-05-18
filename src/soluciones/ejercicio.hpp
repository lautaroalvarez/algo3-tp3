#ifndef _ejercicio_h__
#define __ejercicio_h__

#include <iostream>
#include <stdlib.h>
#include <tuple>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

class ejercicio {
protected:
  double distanciaMinima;
  vector<int> solucion;
  vector<tuple<int,int,int>> gimnasios;
  vector<tuple<int,int>> pokeparadas;
  vector<vector<double>> distancias;
  int mochila;
  int pocionesActuales;
  bool entrada_invalida = false;

  //--Parametros para experimentacion
  int cantidad_cambios;

public:
  //-------------------------------------------------------------------------------------------
  //----- CONSTRUCTOR: Recibe los datos de entrada y llena las estructuras
  //-------------------------------------------------------------------------------------------
  ejercicio (){
    // parseo
    int n, m; // mochila = k
    cin >> n >> m >> mochila;

    int posx, posy, pociones;

    //--vamos a calcular la minima cantidad de pociones necesarias para matar a todos los gimnasios
    int min_pociones_necesarias = 0;

    for (size_t i = 0; i < n; i++) {
      cin >> posx >> posy >> pociones;
      //--acumula la cantidad de pociones necesarias para matar a todos los gimnasios
      min_pociones_necesarias += pociones;
      //--si se necesitan mas pociones de las que entran en la mochila => no hay solucion
      if (pociones > mochila) {
        entrada_invalida = true;
      }
      gimnasios.push_back(make_tuple(posx,posy,pociones));
    }

    for (size_t i = 0; i < m; i++) {
      cin >> posx >> posy;
      pokeparadas.push_back(make_tuple(posx,posy));
    }

    for (size_t i = 0; i < n+m; i++) {
      vector<double> dummy;
      distancias.push_back(dummy);
      for (size_t j = 0; j < n+m; j++) {
        int difX = 0;
        int difY = 0;
        if(i<n){ // el i es un gimnasio o una pokeparada?
          difX = get<0>(gimnasios[i]);
          difY = get<1>(gimnasios[i]);
        }else{
          difX = get<0>(pokeparadas[i-n]);
          difY = get<1>(pokeparadas[i-n]);
        }
        if(j<n){
          difX -= get<0>(gimnasios[j]);
          difY -= get<1>(gimnasios[j]);
        }else{
          difX -= get<0>(pokeparadas[j-n]);
          difY -= get<1>(pokeparadas[j-n]);
        }
        distancias[i].push_back(sqrt(pow(difX,2)+pow(difY,2)));
      }
    }

    pocionesActuales = 0;
    distanciaMinima = -1;

    //-- si no alcanzan las pokeparadas para juntar las pociones necesarias para matar a todos => no hay solucion
    if (min_pociones_necesarias > pokeparadas.size()*3) {
      entrada_invalida = true;
    }
  }


  //-------------------------------------------------------------------------------------------
  //----- IMPLEMENTACIONES DE ALGORITMOS GOLOSOS
  //-------------------------------------------------------------------------------------------

  //--GOLOSO BASICO:
  //--Trata de ir primero a los nodos mas cercanos. Sino va a una parada cercana.
  void golosoDeterministico(){
    // este goloso agarra el gimnasio mas cercano que puede matar
    int cant_gimnasios = gimnasios.size();
    int cant_poke = pokeparadas.size();
    int total = cant_poke+cant_gimnasios; // n+m

    // agarro el primer gimnasio y me voy a la poke parada mas cercana para arrancar
    int pokeCercano = pokeparadaMasCercana(0);

    pocionesActuales = sumaSaturada(pocionesActuales, 3);
    int gimnasios_recorridos = 0;
    int nodoActual = pokeCercano+cant_gimnasios;
    solucion.push_back(nodoActual+1);

    while (gimnasios_recorridos < cant_gimnasios) {
      int gimnasiocercano = -1;
      int distGim = -1;
      for (size_t i = 0; i < cant_gimnasios; i++) { // busco el mas cercano que puedo matar
        if ((distGim > distancias[i][nodoActual] || distGim == -1)// la distancia es menor
          && pocionesActuales >= get<2>(gimnasios[i]) // y me alcanzan las pociones
          && !yaLoRecorri(i)) // y no recorri este gimnasio
        {
          distGim = distancias[i][nodoActual];
          gimnasiocercano = i;
        }
      }
      if(gimnasiocercano == -1){ // no encontre gimnasio para matar, busco una pokeparada cerca
        pokeCercano = pokeparadaMasCercana(nodoActual);
        if (pokeCercano < 0) { // no quedan paradas => no puedo matar los gimnasios restantes
          break;
        } else {
          pocionesActuales = sumaSaturada(pocionesActuales,3);
          nodoActual = pokeCercano+cant_gimnasios;
        }
      } else { // mato el gimnasio!
        ++gimnasios_recorridos;
        nodoActual = gimnasiocercano;
        pocionesActuales -= get<2>(gimnasios[nodoActual]);
      }
      solucion.push_back(nodoActual+1);
    }

    if (gimnasios_recorridos < cant_gimnasios) {
      //-distancia invalida
      distanciaMinima = -1;
    } else {
      //-distancia
      distanciaMinima = 0;
      for(int i = 0; i < solucion.size()-1; ++i){
        distanciaMinima += distancias[solucion[i]-1][solucion[i+1]-1];
      }
    }

    return;
  }

  //--GOLOSO RANDOM:
  //--Recibe los siguientes parametros:
  //----nodo_inicial -> si quiere arrancar por una parada en particular
  //----orden_preferencia:
  //------0 va al mas cercano primero
  //------1 va al mas lejano primero
  //------2 va al que mas pociones necesite para matar
  //------3 va al que menos pociones necesite para matar
  //----cant_random -> la cantidad de nodos entre los que se va a tomar un random
  void calculaGoloso(int nodo_inicial = -1, int orden_preferencia = 0, int cant_random = 1) {

    int cant_gimnasios = gimnasios.size();
    int cant_poke = pokeparadas.size();
    int total = cant_poke+cant_gimnasios; // n+m

    int pocionesAct = 3;
    int gimnasios_recorridos = 0;

    int nodoActual = nodo_inicial;
    int pokeCercano;

    //--si no se paso un nodo de inicio como parametro
    if (nodo_inicial < 0) {
      // agarro una parada random
      if (cant_poke == 0) {
        nodoActual = 0;
        ++gimnasios_recorridos;
      } else {
        nodoActual = cant_gimnasios + rand() % cant_poke;
        pocionesAct = sumaSaturada(pocionesAct,3);
      }
    }
    solucion.clear();
    solucion.push_back(nodoActual + 1);

    while (gimnasios_recorridos < cant_gimnasios) {
      vector<tuple<int,float,int>> gimnasios_posibles; // vector<id,distancia,pociones>
      int gimnasiocercano = -1;
      for (size_t i = 0; i < cant_gimnasios; i++) { // busco los gimnasios que puedo matar
        if (pocionesAct >= get<2>(gimnasios[i]) // y me alcanzan las pociones
          && !yaLoRecorri(i)) // y no recorri este gimnasio
        {
            gimnasios_posibles.push_back(make_tuple(i,distancias[i][nodoActual],get<2>(gimnasios[i])));
        }
      }
      if(gimnasios_posibles.size() != 0){

        // actualizo cant random para que no haga randomen un cjto mayor
        int tope_random = cant_random > gimnasios_posibles.size() ? gimnasios_posibles.size() : cant_random;
        int random = rand()%tope_random;
        switch (orden_preferencia) {
          case 0:
            // busco los mas cercanos que pueda matar
            sort(gimnasios_posibles.begin(), gimnasios_posibles.end(), [](const tuple<int,float,int>& a,
            const tuple<int,float,int>& b) -> bool
            {
              return std::get<1>(a) > std::get<1>(b);
            });
            gimnasiocercano = get<0>(gimnasios_posibles[random]);
            break;

          case 1:
            // busco los mas lejanos que pueda matar
            sort(gimnasios_posibles.begin(), gimnasios_posibles.end(), [](const tuple<int,float,int>& a,
            const tuple<int,float,int>& b) -> bool
            {
              return std::get<1>(a) > std::get<1>(b);
            });
            gimnasiocercano = get<0>(gimnasios_posibles[gimnasios_posibles.size()-1-random]);
            break;

          case 2:
            // busco los que mas pociones necesite para matar y que pueda matar
            sort(gimnasios_posibles.begin(), gimnasios_posibles.end(), [](const tuple<int,float,int>& a,
            const tuple<int,float,int>& b) -> bool
            {
              return std::get<2>(a) > std::get<2>(b);
            });
            gimnasiocercano = get<0>(gimnasios_posibles[random]);
            break;

          case 3:
            // busco los que menos pociones necesite para matar y que pueda matar
            sort(gimnasios_posibles.begin(), gimnasios_posibles.end(), [](const tuple<int,float,int>& a,
            const tuple<int,float,int>& b) -> bool
            {
              return std::get<2>(a) > std::get<2>(b);
            });
            gimnasiocercano = get<0>(gimnasios_posibles[gimnasios_posibles.size()-1-random]);
            break;
        }
      }
      if (gimnasiocercano == -1) { // no encontre gimnasio para matar, busco una pokeparada cerca
        pokeCercano = pokeparadaMasCercana(nodoActual);
        if (pokeCercano < 0) { // no quedan paradas => no puedo matar los gimnasios restantes
          break;
        } else {
          pocionesAct = sumaSaturada(pocionesAct,3);
          nodoActual = pokeCercano+cant_gimnasios;
        }
      } else { // mato el gimnasio!
        ++gimnasios_recorridos;
        nodoActual = gimnasiocercano;
        pocionesAct -= get<2>(gimnasios[nodoActual]);
      }
      solucion.push_back(nodoActual+1);
    }

    //--si faltaron gimnasios por recorrer
    if (gimnasios_recorridos < cant_gimnasios) {
      //-distancia invalida
      distanciaMinima = -1;
    } else {
      //-distancia
      distanciaMinima = 0;
      for(int i = 0; i < solucion.size()-1; ++i){
        distanciaMinima += distancias[solucion[i]-1][solucion[i+1]-1];
      }
    }

    return;
  }


  //-------------------------------------------------------------------------------------------
  //----- IMPLEMENTACION DE BUSQUEDA LOCAL
  //-------------------------------------------------------------------------------------------

  //--Recibe el parametro:
  //----codigo_vecindades -> binario indicando cuales vecindades que se quieren usar y cuales no
  void busquedaLocal(string codigo_vecindades = "1111") {
    //--se usa esta variable para ver si se mejoró al solución en el última iteración
    bool cambio = true;

    //--un contador de iteraciones (para experimentar)
    cantidad_cambios = 0;

    int cant_nodos = gimnasios.size() + pokeparadas.size();
    int repeticiones = 0;

    //--mientras se mejore
    while(cambio && repeticiones < cant_nodos){

      cambio = false;

      vector<vector<int> > vecindad;

      //--pide las vecindades de la solución actual
      for (int i = 0; i < 3; i++) {

        //--si la función de vecindad i está marcada para ser usada
        if (codigo_vecindades[i] == '1') {

          vector<vector<int> > vecindad_nueva;

          //--llama a cada vecindad distinta
          switch (i) {

            case 0:
              //--cambia una parada del camino por una de afuera
              vecindad_nueva = vecinosConLosDeAfuera();
              break;

            case 1:
              //--cambia entre dos nodos adyacentes del camino (sin importar el tipo)
              vecindad_nueva = vecinosConLosAdyacentes();
              break;

            case 2:
              //--cambia entre dos paradas del camino
              vecindad_nueva = vecinosConLosDeAdentro();
              break;

            case 3:
              //--cambia entre dos gimnasios del camino
              vecindad_nueva = vecinosConLosGim();
              break;

          }

          //--si se tiene una nueva vecindad
          if (vecindad_nueva.size() > 0) {
            //--se agregan estos vecinos al final
            vecindad.insert(vecindad.begin(), vecindad_nueva.begin(), vecindad_nueva.end());
          }

        }

      }

      //--si la vecindad no está vacía
      if(vecindad.size() > 0) {

        //--busca el mejor vecino
        vector<int> mejor_vecino = minimoVecino(vecindad);

        double dist_mejor_vecino = calcularDistancia(mejor_vecino);
        double dist_solucion = calcularDistancia(solucion);

        //--si el vecino es mejor que la solución actual
        if (dist_mejor_vecino < dist_solucion) {

          //--cambia la solución
          cambio = true;

          solucion = mejor_vecino;
          distanciaMinima = dist_mejor_vecino;

          //--para experimentar
          //cout << cantidad_cambios << ", " << dist_mejor_vecino << ", " << abs(dist_solucion - dist_mejor_vecino) << ", " << vecindad.size() << endl;
        }
      }

      //--aumenta el contador
      cantidad_cambios++;

      //--aumenta el contador de repeticiones
      repeticiones++;
    }

    return;
  }



  //-------------------------------------------------------------------------------------------
  //----- IMPLEMENTACION DE VECINDADES
  //-------------------------------------------------------------------------------------------

  //--Vecindad 1: cambia paradas que esten en el camino por paradas que no esten en el camino
  vector <vector<int>> vecinosConLosDeAfuera() {
    int pokeNueva = 0;
    int pokeVieja = 0;
    vector<vector<int>> resultado;
    vector<int> solucionAMejorar = solucion;
    vector<tuple<int,int> > pokeswaps = pokeparadas;
    for( int i = 0; i< solucionAMejorar.size(); i++) {
      if (esPokeParada(solucionAMejorar[i])) {
        for (int j = 0; j < pokeswaps.size(); j ++) {
          if (NoEstaEnLaSolucion(j + gimnasios.size(), solucionAMejorar)) {
            pokeNueva = j + gimnasios.size()+1;
            pokeVieja = solucionAMejorar[i];
            solucionAMejorar[i] = pokeNueva;
            resultado.push_back(solucionAMejorar);
            solucionAMejorar[i] = pokeVieja; // vuelvo todo como estaba...
          }
        }
      }
    }
    return resultado;
  }
  //--Vecindad 2: cambia nodos por los adyacentes, sin importar el tipo
  vector<vector<int>> vecinosConLosAdyacentes() {
      vector<vector<int>> resultado;
      vector<int> solucionAMejorar = this->solucion;
      double distanciaNueva = calcularDistancia(solucionAMejorar);
      double distanciaParcial = distanciaNueva;
      for( int i = 0; i < solucionAMejorar.size() - 1 ; i++) {
        swap(solucionAMejorar[i], solucionAMejorar[i+1]);
        if (esValido(solucionAMejorar)) {
            resultado.push_back(solucionAMejorar);
        }
          swap(solucionAMejorar[i+1], solucionAMejorar[i]);
      }
      return resultado;
  }

  //--Vecindad 3: cambia de lugar paradas del camino
  vector<vector<int>> vecinosConLosDeAdentro() {
    int pokeNueva = 0;
    int pokeVieja = 0;
    vector<vector<int>> resultado;
    vector<int> solucionAMejorar = this->solucion;
    for( int i = 0; i< solucionAMejorar.size(); i++) {
      if (esPokeParada(solucionAMejorar[i])) {
        for (int j = i+1; j < solucionAMejorar.size(); j ++) {
          if (esPokeParada(solucionAMejorar[j])) {
             swap (solucionAMejorar[i], solucionAMejorar[j]);
             if (esValido(solucionAMejorar)) {
                resultado.push_back(solucionAMejorar);
            }
            swap (solucionAMejorar[j], solucionAMejorar[i]); // dejo todo como estaba.
          }
        }
      }
    }

    return resultado;
  }

  //--Vecindad 3: cambia de lugar gimnasios del camino
  vector<vector<int>> vecinosConLosGim() {
    int pokeNueva = 0;
    int pokeVieja = 0;
    vector<vector<int>> resultado;
    vector<int> solucionAMejorar = this->solucion;
    for( int i = 0; i< solucionAMejorar.size(); i++) {
      if (!esPokeParada(solucionAMejorar[i])) {
        for (int j = i+1; j < solucionAMejorar.size(); j ++) {
            if (!esPokeParada(solucionAMejorar[j])) {
               swap (solucionAMejorar[i], solucionAMejorar[j]);
               if (esValido(solucionAMejorar)) {
                  resultado.push_back(solucionAMejorar);
              }
              swap (solucionAMejorar[j], solucionAMejorar[i]); // dejo todo como estaba.
            }
         }
      }
    }
    return resultado;
  }




  //-------------------------------------------------------------------------------------------
  //----- FUNCIONES AUXILIARES
  //-------------------------------------------------------------------------------------------

  //--Verifica si el camino pasado por parametro es valido
  bool esValido(vector<int> camino){
    int pociones = 0;
    for (size_t i = 0; i < camino.size(); i++) {
      if (camino[i] > gimnasios.size()) {
        pociones = sumaSaturada(pociones,3);
      }else{
        if (get<2>(gimnasios[camino[i]-1]) > pociones) {
          return false;
        }
        pociones = pociones - get<2>(gimnasios[camino[i]-1]);
      }
    }
    return true;
  }

  //--Busca la pokeparada mas cercana al nodo pasado como parametro
  int pokeparadaMasCercana(int nodo){
    int pokeCercano = -1;
    int distPoke = -1;
    for (size_t i = 0; i < pokeparadas.size(); i++) {
      if((distPoke > distancias[i+gimnasios.size()][nodo] || distPoke == -1) && !yaLoRecorri(i+gimnasios.size())){
        distPoke = distancias[i+gimnasios.size()][nodo];
        pokeCercano = i;
      }
    }
    return pokeCercano;
  }

  //--Imprime la solucion en el formato pedido (si no es valida imprime -1)
  void imprimir(){
    if (distanciaMinima < 0) {
      std::cout << distanciaMinima << endl;
    } else {
      std::cout << distanciaMinima << " " <<  solucion.size();
      for (size_t i = 0; i < solucion.size(); i++) {
        std::cout << " " << solucion[i];
      }
      std::cout << std::endl;
    }
  }

  //--Realiza la suma saturada de pociones sin exceder el tamano la mochila
  int sumaSaturada(int pocionesActuales, int pocionesNuevas){
    int suma = pocionesActuales+pocionesNuevas;
    if (suma > mochila) {
      return mochila;
    }else{
      return suma;
    }
  }

  //--Verifica si el nodo pasado por parametro ya se encuentra en la solucion actual
  bool yaLoRecorri(int nodo){
    int i = 0;
    while (i<solucion.size() && solucion[i] != nodo+1) {
      ++i;
    }
    return i<solucion.size();
  }

  //--Calcula la distancia del camino pasado por parametro
  double calcularDistancia(vector<int> camino){
    double distancia = 0;
    for(int i = 1; i < camino.size(); ++i){
        distancia += distancias[camino[i-1]-1][camino[i]-1];
    }
    return distancia;
  }

  //--Verifica si el nodo pasado por parametro es una pokeparada
  bool esPokeParada(int nodo) {
    return nodo > gimnasios.size();
  }

  //--Verifica si el nodo pasado por parametro no esta en la solucion
  bool NoEstaEnLaSolucion( int pokePos, vector<int> solu){
    bool result = true;
    for (int i = 0; i < solu.size(); i++){
        if (pokePos == solu[i]-1) {result = false;}
    }
    return result;
  }

  //--Verifica si la distancia nueva pasdad por parametro mejora a la distancia original pasada por parametro
  bool MejoraSolucion(int distanciaNueva, int distanciaOriginal) {
    return distanciaNueva < distanciaOriginal;
  }

  //--Calcula el minimo entre un vector de vecindades pasado por parametro
  vector<int> minimoVecino(vector<vector<int> > vecinos) {
    double minimo = calcularDistancia(vecinos[0]);
    vector<int> mejor_vecino = vecinos[0];

    for (int i = 1; i < vecinos.size(); i++) {
      if (minimo > calcularDistancia(vecinos[i])) {
        minimo = calcularDistancia(vecinos[i]);
        mejor_vecino = vecinos[i];
      }
    }

    return mejor_vecino;
  }

  virtual ~ejercicio (){};
};

#endif
