from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError


# ==================================================
# CLASE ABSTRACTA SERVICIO
# ==================================================

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ServicioInvalidoError(
                "El nombre del servicio es obligatorio."
            )

        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or precio_base <= 0
        ):
            raise ServicioInvalidoError(
                "El precio base debe ser mayor que cero."
            )

        self.__nombre = nombre.strip()
        self.__precio_base = float(precio_base)

    # PROPIEDADES

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    # VALIDAR CANTIDAD

    @staticmethod
    def validar_cantidad(cantidad):

        if (
            not isinstance(cantidad, (int, float))
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ServicioInvalidoError(
                "La cantidad debe ser un numero mayor que cero."
            )

    # METODOS ABSTRACTOS

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    # CALCULAR TOTAL CON IMPUESTO Y DESCUENTO

    def calcular_total(self, cantidad, impuesto=0.19, descuento=0):

        self.validar_cantidad(cantidad)

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 1
        ):
            raise ServicioInvalidoError(
                "El impuesto debe estar entre 0 y 1."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 1
        ):
            raise ServicioInvalidoError(
                "El descuento debe estar entre 0 y 1."
            )

        subtotal = self.calcular_costo(cantidad)

        valor_impuesto = subtotal * impuesto
        valor_descuento = subtotal * descuento

        total = subtotal + valor_impuesto - valor_descuento

        return round(total, 2)


# ==================================================
# SERVICIO: RESERVA DE SALA
# ==================================================

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):

        super().__init__(nombre, precio_base)

        if (
            not isinstance(capacidad, int)
            or isinstance(capacidad, bool)
            or capacidad <= 0
        ):
            raise ServicioInvalidoError(
                "La capacidad debe ser un entero positivo."
            )

        self.__capacidad = capacidad

    def calcular_costo(self, horas):

        self.validar_cantidad(horas)

        return self.precio_base * horas

    def describir_servicio(self):

        return (
            f"{self.nombre}: reserva de sala por horas. "
            f"Capacidad: {self.__capacidad} personas."
        )


# ==================================================
# SERVICIO: ALQUILER DE EQUIPO
# ==================================================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, equipo):

        super().__init__(nombre, precio_base)

        if not isinstance(equipo, str) or not equipo.strip():
            raise ServicioInvalidoError(
                "Debe especificar el equipo que se alquila."
            )

        self.__equipo = equipo.strip()

    def calcular_costo(self, dias):

        self.validar_cantidad(dias)

        return self.precio_base * dias

    def describir_servicio(self):

        return (
            f"{self.nombre}: alquiler de equipo "
            f"{self.__equipo} por dias."
        )


# ==================================================
# SERVICIO: ASESORIA
# ==================================================

class Asesoria(Servicio):

    def __init__(self, nombre, precio_base, especialidad):

        super().__init__(nombre, precio_base)

        if (
            not isinstance(especialidad, str)
            or not especialidad.strip()
        ):
            raise ServicioInvalidoError(
                "Debe especificar la especialidad de la asesoria."
            )

        self.__especialidad = especialidad.strip()

    def calcular_costo(self, horas):

        self.validar_cantidad(horas)

        return self.precio_base * horas

    def describir_servicio(self):

        return (
            f"{self.nombre}: asesoria especializada "
            f"en {self.__especialidad}."
        )