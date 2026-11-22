# SOFTWARE FJ
## Sistema Integral de Gestion de Clientes, Servicios y Reservas

---

## Descripcion del proyecto

Software FJ es un sistema desarrollado en Python que permite gestionar clientes, servicios y reservas mediante el uso de programacion orientada a objetos.

El sistema permite registrar clientes, crear diferentes tipos de servicios, realizar reservas, calcular costos con impuestos y descuentos, confirmar y cancelar reservas, y controlar errores mediante excepciones personalizadas.

---

## Objetivo general

Desarrollar un sistema integral de gestion de clientes, servicios y reservas utilizando el lenguaje de programacion Python, aplicando conceptos de programacion orientada a objetos, validaciones, modularidad, manejo de excepciones y registro de eventos.

---

## Funcionalidades

- Registro y validacion de clientes.
- Gestion de clientes mediante clases y objetos.
- Creacion de servicios especializados.
- Reserva de salas de reuniones.
- Alquiler de equipos informaticos.
- Servicios de asesoria informatica.
- Creacion de reservas.
- Confirmacion y cancelacion de reservas.
- Calculo de costos de los servicios.
- Aplicacion de impuestos y descuentos.
- Validacion de datos ingresados.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de log.
- Continuidad de la ejecucion ante errores controlados.

---

## Estructura del proyecto

El proyecto se encuentra organizado en los siguientes archivos:

- `main.py`: archivo principal encargado de ejecutar e integrar el sistema.
- `clientes.py`: contiene la clase Entidad y la clase Cliente, con sus validaciones y atributos.
- `servicios.py`: contiene la clase abstracta Servicio y los servicios especializados.
- `reservas.py`: permite gestionar las reservas, sus estados, confirmaciones y cancelaciones.
- `excepciones.py`: contiene las excepciones personalizadas utilizadas por el sistema.
- `logs.txt`: almacena los eventos, operaciones y errores generados durante la ejecucion.

---

## Servicios disponibles

### Reserva de sala

Permite reservar una sala de reuniones por horas y establece la capacidad de personas permitidas.

### Alquiler de equipos

Permite gestionar el alquiler de equipos informaticos por dias.

### Asesoria informatica

Permite ofrecer servicios de asesoria especializada y calcular su costo de acuerdo con la cantidad de horas.

---

## Tecnologias utilizadas

- Python 3.14.
- Programacion orientada a objetos.
- Visual Studio Code.
- Manejo de archivos.
- Sistema de registro de eventos mediante logging.

---

## Conceptos de programacion aplicados

- Clases y objetos.
- Abstraccion.
- Encapsulamiento.
- Herencia.
- Polimorfismo.
- Metodos abstractos.
- Propiedades.
- Validacion de datos.
- Excepciones personalizadas.
- Manejo de errores.
- Modularidad.
- Parametros opcionales.
- Registro de eventos.

---

## Ejecucion del programa

Para ejecutar el sistema se deben seguir los siguientes pasos:

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Verificar que Python se encuentre instalado.
3. Abrir el archivo `main.py`.
4. Ejecutar el programa desde Visual Studio Code o desde la terminal.

El sistema ejecutara las operaciones de prueba, mostrara los resultados en consola y registrara los eventos y errores en el archivo `logs.txt`.

---

## Autor

**Jhonatan David Navarro Torrecilla**

Proyecto academico desarrollado para la asignatura de Programacion.

---

## Nombre del proyecto

Software FJ - Sistema Integral de Gestion de Clientes, Servicios y Reservas.