# Glosario Patrones de Arquitectura

A continuación, se presentarán cinco patrones de aquitectura vistos en clase de los cuales se mostrará su concepto y un ejemplo sencillo para cada uno.

## Patrón por Capas

Este patrón estructura nuestro sistema dividiendolo capas, cada capa va a tener una reponsabilidad específica, donde el sistema se va a dividir por subtareas y cada una de estas capas se comunicará únicamente con las superiores a ella, las capas que se usan frecuentemente son cuantro y son las siguientes:

* Capa de presentación: toda la interfaz o la parte visual que se va a poder ver del sistema.
* Capa de lógica de negocios: realiza toda la lógica sobre alguna funcionalidad con la que interactúe en la capa de la presentación.
* Capa de acceso a datos: se comunica con la base de datos para poder hacer las transacciones sobre esta.
* Capa de base de datos: base de datos donde se almacena todo lo relacionado a los datos del sistema que finalmente serán información útil para la capa de la lógica de negocios y presentación.

![](https://i.imgur.com/jvrDDll.png)

Este patrón facilita la separación de responsabilidades, con el objetivo de no tener que afectar elementos que no se requieran modificar al momento de tener que cambiar algo en específico, por ejemplo si se necesita cambiar un botón de la interfaz del usuario se va a hacer en la capa de presentación y no se va a tener que modificar otra y además va a ser mucho más sencillo. De esta manera nuestro sistema se vuelve mantenible y sostenible.

Dentro del repositorio se deja un ejemplo de una calculadora sencilla que usa este patrón arquitectónico guardando el historial de operaciones que se han realizado en esta.

## Patrón MVC

Este patrón estructura nuestro sistema en tres partes, el modelo, la vista y el controlador, de esta manera podemos organizar el código de manera sencilla y más organizada, cada una se basa en lo siguiente:

* Modelo: aquí se procesan todos los datos, si se necesita realizar alguna operación o similar va a ser aquí, donde se encuentra la lógica de negocio.
* Vista: presenta todo lo visual de nuestro sistema, es aquí donde se interactúa y se presentan los datos que vienen del modelo por medio del controlador.
* Controlador: aquí se hace una comunicación entre el modelo y la vista, básicamente decide qué hacer con las entradas del usuario (interacciones) y decide qué hacer, si a la vista que actualice información para mostrar en la interfaz o al modelo que actualice datos.

![](https://i.imgur.com/JWP1U9N.png)

En pocas palabras, el usuario lo que hace es interactuar con la vista, luego esta envía la interacción al controlador, luego el controlador toma esa interacción, la procesa y si es necesario actualiza el modelo, luego el modelo actualiza los datos y notifica a la vista si los datos cambiaron, finalmente se actualiza la vista y la vista se actualiza para reflejar los cambios.

Este patrón también tiene el beneficio de separar responsabilidades, lo que hace que nuestró código sea mantenible y el sistema sostenible.

Dentro del repositorio se deja un ejemplo de una sistema de tareas sencillo que usa este patrón arquitectónico.