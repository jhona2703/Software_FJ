from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)

from clientes import Cliente
from servicios import Servicio


# ==================================================
# CLASE RESERVA
# ==================================================

class Reserva:

    def __init__(self, codigo, cliente, servicio, cantidad):

        # VALIDAR CODIGO

        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaInvalidaError(
                "El codigo de la reserva es obligatorio."
            )

        # VALIDAR CLIENTE

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "La reserva debe tener un cliente valido."
            )

        # VALIDAR SERVICIO

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio valido."
            )

        # VALIDAR CANTIDAD

        if (
            not isinstance(cantidad, (int, float))
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ReservaInvalidaError(
                "La cantidad debe ser mayor que cero."
            )

        # ATRIBUTOS

        self.__codigo = codigo.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__cantidad = cantidad
        self.__estado = "Pendiente"

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def estado(self):
        return self.__estado

    # ==================================================
    # CALCULAR COSTO DE LA RESERVA
    # ==================================================

    def calcular_costo(self, impuesto=0.19, descuento=0.10):

        return self.__servicio.calcular_total(
            self.__cantidad,
            impuesto,
            descuento
        )

    # ==================================================
    # CONFIRMAR RESERVA
    # ==================================================

    def confirmar(self):

        if self.__estado != "Pendiente":

            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"

        return "Reserva confirmada correctamente."

    # ==================================================
    # CANCELAR RESERVA
    # ==================================================

    def cancelar(self):

        if self.__estado == "Cancelada":

            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"

        return "Reserva cancelada correctamente."

    # ==================================================
    # MOSTRAR INFORMACION DE LA RESERVA
    # ==================================================

    def mostrar_informacion(self):

        return (
            f"\n--- RESERVA {self.__codigo} ---\n"
            f"{self.__cliente.mostrar_informacion()}\n"
            f"Servicio: {self.__servicio.describir_servicio()}\n"
            f"Cantidad: {self.__cantidad}\n"
            f"Estado: {self.__estado}\n"
            f"Total: ${self.calcular_costo():,.2f}"
        )