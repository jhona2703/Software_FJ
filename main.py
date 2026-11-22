import logging

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)

# ==================================================
# CONFIGURACION DEL REGISTRO DE EVENTOS
# ==================================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# ==================================================
# LISTAS DEL SISTEMA
# ==================================================

clientes = []
servicios = []
reservas = []


# ==================================================
# REGISTRAR CLIENTES
# ==================================================

def registrar_cliente(cliente):

    try:

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "El objeto no corresponde a un cliente valido."
            )

        clientes.append(cliente)

        print(f"Cliente {cliente.nombre} registrado correctamente.")

        logging.info(f"Cliente registrado: {cliente.nombre}")

    except ClienteInvalidoError as error:

        print(f"Error controlado de cliente: {error}")

        logging.error(f"Error al registrar cliente: {error}")


# ==================================================
# REGISTRAR SERVICIOS
# ==================================================

def registrar_servicio(servicio):

    try:

        servicios.append(servicio)

        print(f"Servicio {servicio.nombre} registrado correctamente.")

        logging.info(f"Servicio registrado: {servicio.nombre}")

    except Exception as error:

        print(f"Error al registrar servicio: {error}")

        logging.error(f"Error al registrar servicio: {error}")


# ==================================================
# CREAR RESERVAS
# ==================================================

def crear_reserva(codigo, cliente, servicio, cantidad):

    try:

        reserva = Reserva(
            codigo,
            cliente,
            servicio,
            cantidad
        )

        reservas.append(reserva)

    except ReservaInvalidaError as error:

        logging.error(f"Error al crear reserva: {error}")

        raise ReservaInvalidaError(
            "No fue posible completar la creacion de la reserva."
        ) from error

    else:

        print(f"Reserva {codigo} creada correctamente.")

        logging.info(f"Reserva creada: {codigo}")

        return reserva


# ==================================================
# MOSTRAR CLIENTES
# ==================================================

def mostrar_clientes():

    print("\n--- CLIENTES REGISTRADOS ---")

    for cliente in clientes:

        print(cliente.mostrar_informacion())


# ==================================================
# MOSTRAR SERVICIOS
# ==================================================

def mostrar_servicios():

    print("\n--- SERVICIOS DISPONIBLES ---")

    for servicio in servicios:

        print(servicio.describir_servicio())


# ==================================================
# MOSTRAR RESERVAS
# ==================================================

def mostrar_reservas():

    print("\n--- RESERVAS REGISTRADAS ---")

    for reserva in reservas:

        print(reserva.mostrar_informacion())


# ==================================================
# DEMOSTRACION DE POLIMORFISMO
# ==================================================

def demostrar_polimorfismo():

    print("\n--- DEMOSTRACION DE POLIMORFISMO ---")

    for servicio in servicios:

        costo = servicio.calcular_costo(2)

        print(f"\nServicio: {servicio.nombre}")

        print(f"Descripcion: {servicio.describir_servicio()}")

        print(f"Costo por 2 unidades: ${costo:,.2f}")

        logging.info(
            f"Polimorfismo aplicado al servicio: {servicio.nombre}"
        )


# ==================================================
# DEMOSTRACION DE PARAMETROS OPCIONALES
# ==================================================

def demostrar_sobrecarga(sala):

    print("\n--- DEMOSTRACION DE PARAMETROS OPCIONALES ---")

    # Forma 1: valores predeterminados

    total1 = sala.calcular_total(2)

    print(
        f"Total con valores predeterminados: "
        f"${total1:,.2f}"
    )

    # Forma 2: impuesto personalizado

    total2 = sala.calcular_total(2, 0.10)

    print(
        f"Total con impuesto del 10%: "
        f"${total2:,.2f}"
    )

    # Forma 3: impuesto y descuento

    total3 = sala.calcular_total(2, 0.19, 0.10)

    print(
        f"Total con impuesto y descuento: "
        f"${total3:,.2f}"
    )

    logging.info(
        "Demostracion de parametros opcionales realizada."
    )


# ==================================================
# PRUEBAS DE OPERACIONES INVALIDAS
# ==================================================

def probar_operaciones(reserva, sala):

    print("\n--- PRUEBAS DE VALIDACIONES Y EXCEPCIONES ---")

    # ----------------------------------------------
    # PRUEBA 1: CONFIRMAR UNA RESERVA NO PENDIENTE
    # ----------------------------------------------

    try:

        reserva.confirmar()

    except OperacionNoPermitidaError as error:

        print(f"Confirmacion no permitida: {error}")

        logging.error(
            f"Prueba de confirmacion repetida: {error}"
        )

    # ----------------------------------------------
    # PRUEBA 2: CANCELAR UNA RESERVA YA CANCELADA
    # ----------------------------------------------

    try:

        reserva.cancelar()

    except OperacionNoPermitidaError as error:

        print(f"Cancelacion no permitida: {error}")

        logging.error(
            f"Prueba de cancelacion repetida: {error}"
        )

    # ----------------------------------------------
    # PRUEBA 3: CALCULAR COSTO CON CANTIDAD INVALIDA
    # ----------------------------------------------

    try:

        sala.calcular_costo(0)

    except ServicioInvalidoError as error:

        print(f"Cantidad invalida detectada: {error}")

        logging.error(
            f"Prueba de cantidad invalida: {error}"
        )

    # ----------------------------------------------
    # PRUEBA 4: IMPUESTO FUERA DEL RANGO
    # ----------------------------------------------

    try:

        sala.calcular_total(2, 1.5)

    except ServicioInvalidoError as error:

        print(f"Impuesto invalido detectado: {error}")

        logging.error(
            f"Prueba de impuesto invalido: {error}"
        )

    # ----------------------------------------------
    # PRUEBA 5: DESCUENTO FUERA DEL RANGO
    # ----------------------------------------------

    try:

        sala.calcular_total(2, 0.19, 1.5)

    except ServicioInvalidoError as error:

        print(f"Descuento invalido detectado: {error}")

        logging.error(
            f"Prueba de descuento invalido: {error}"
        )

    print("\nPruebas de validaciones finalizadas.")

    logging.info(
        "Pruebas adicionales de validaciones finalizadas."
    )


# ==================================================
# FUNCION PRINCIPAL
# ==================================================

def ejecutar_sistema():

    print("=" * 50)

    print(" SISTEMA INTEGRAL SOFTWARE FJ")

    print("=" * 50)

    try:

        # ==========================================
        # REGISTRO DE CLIENTES
        # ==========================================

        cliente1 = Cliente(
            "1001",
            "Laura Gomez",
            "laura@gmail.com",
            "3001234567"
        )

        cliente2 = Cliente(
            "1002",
            "Carlos Perez",
            "carlos@gmail.com",
            "3109876543"
        )

        registrar_cliente(cliente1)

        registrar_cliente(cliente2)

        # ==========================================
        # PRUEBA DE CLIENTE INVALIDO
        # ==========================================

        try:

            cliente_invalido = Cliente(
                "1003",
                "",
                "correo@gmail.com",
                "3001234567"
            )

            registrar_cliente(cliente_invalido)

        except ClienteInvalidoError as error:

            print(
                f"\nError controlado de cliente: {error}"
            )

            logging.error(
                f"Cliente invalido detectado: {error}"
            )

        # ==========================================
        # REGISTRO DE SERVICIOS
        # ==========================================

        sala = ReservaSala(
            "Sala de reuniones",
            50000,
            10
        )

        computador = AlquilerEquipo(
            "Alquiler de computador",
            30000,
            "Portatil"
        )

        asesoria = Asesoria(
            "Asesoria informatica",
            80000,
            "Software"
        )

        registrar_servicio(sala)

        registrar_servicio(computador)

        registrar_servicio(asesoria)

        # ==========================================
        # PRUEBA DE SERVICIO INVALIDO
        # ==========================================

        try:

            servicio_invalido = ReservaSala(
                "Sala incorrecta",
                -50000,
                10
            )

            registrar_servicio(servicio_invalido)

        except ServicioInvalidoError as error:

            print(
                f"\nError controlado de servicio: {error}"
            )

            logging.error(
                f"Servicio invalido detectado: {error}"
            )

        # ==========================================
        # CREAR Y CONFIRMAR RESERVA
        # ==========================================

        reserva1 = crear_reserva(
            "R001",
            cliente1,
            sala,
            2
        )

        print(reserva1.confirmar())

        logging.info("Reserva R001 confirmada.")

        # ==========================================
        # PRUEBA DE RESERVA INVALIDA
        # ==========================================

        try:

            crear_reserva(
                "R002",
                cliente2,
                computador,
                0
            )

        except ReservaInvalidaError as error:

            print(
                f"\nError controlado de reserva: {error}"
            )

            logging.error(
                f"Reserva invalida detectada: {error}"
            )

        # ==========================================
        # CALCULO DE COSTO
        # ==========================================

        total = sala.calcular_total(
            2,
            0.19,
            0.10
        )

        print(
            f"\nTotal de sala con impuesto y descuento: "
            f"${total:,.2f}"
        )

        logging.info(
            f"Total calculado para sala: ${total:,.2f}"
        )

        # ==========================================
        # PARAMETROS OPCIONALES
        # ==========================================

        demostrar_sobrecarga(sala)

        # ==========================================
        # CANCELAR RESERVA
        # ==========================================

        print(reserva1.cancelar())

        logging.info("Reserva R001 cancelada.")

        # ==========================================
        # PRUEBAS ADICIONALES
        # ==========================================

        probar_operaciones(reserva1, sala)

        # ==========================================
        # MOSTRAR CLIENTES
        # ==========================================

        mostrar_clientes()

        # ==========================================
        # MOSTRAR SERVICIOS
        # ==========================================

        mostrar_servicios()

        # ==========================================
        # POLIMORFISMO
        # ==========================================

        demostrar_polimorfismo()

        # ==========================================
        # MOSTRAR RESERVAS
        # ==========================================

        mostrar_reservas()

    except Exception as error:

        print(f"\nError inesperado en el sistema: {error}")

        logging.exception(
            "Se produjo un error inesperado en el sistema."
        )

    finally:

        print(
            "\nEjecucion del sistema Software FJ finalizada."
        )

        logging.info(
            "Ejecucion del sistema Software FJ finalizada."
        )


# ==================================================
# INICIO DEL PROGRAMA
# ==================================================

if __name__ == "__main__":

    ejecutar_sistema()