# Glosario Patrones de Arquitectura

A continuación, se presentarán cinco patrones de aquitectura vistos en clase de los cuales se mostrará su concepto y un ejemplo sencillo para cada uno.

## Patrón por Capas

Este patrón estructura nuestro sistema dividiendolo capas, cada capa va a tener una reponsabilidad específica, donde el sistema se va a dividir por subtareas y cada una de estas capas se comunicará únicamente con las superiores a ella, las capas que se usan frecuentemente son cuantro y son las siguientes:

* Capa de presentación: toda la interfaz o la parte visual que se va a poder ver del sistema.
* Capa de lógica de negocios: realiza toda la lógica sobre alguna funcionalidad con la que interactúe en la capa de la presentación.
* Capa de acceso a datos: se comunica con la base de datos para poder hacer las transacciones sobre esta.
* Capa de base de datos: base de datos donde se almacena todo lo relacionado a los datos del sistema que finalmente serán información útil para la capa de la lógica de negocios y presentación.

![](https://i.imgur.com/gO3HGMi.png)

Este patrón facilita la separación de responsabilidades, con el objetivo de no tener que afectar elementos que no se requieran modificar al momento de tener que cambiar algo en específico, por ejemplo si se necesita cambiar un botón de la interfaz del usuario se va a hacer en la capa de presentación y no se va a tener que modificar otra y además va a ser mucho más sencillo. De esta manera nuestro sistema se vuelve mantenible y sostenible.

Dentro del repositorio se deja un ejemplo de una calculadora sencilla que usa este patrón arquitectónico guardando el historial de operaciones que se han realizado en esta.

## Patrón MVC

