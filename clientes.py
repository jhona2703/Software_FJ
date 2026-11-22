
# clientes.py

# Importamos la clase para crear clases abstractas
from abc import ABC, abstractmethod

# Importamos nuestra excepcion personalizada
from excepciones import ClienteInvalidoError


# Clase abstracta que representa una entidad general
class Entidad(ABC):

    def __init__(self, identificador):
        # Validamos que el identificador exista
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador no puede estar vacio.")

        self._identificador = str(identificador).strip()

    # Metodo abstracto que las clases hijas deben implementar
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Validamos la identificacion
        if not identificacion or not str(identificacion).strip():
            raise ClienteInvalidoError(
                "La identificacion del cliente es obligatoria."
            )

        # Validamos el nombre
        if not nombre or not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacio."
            )

        # Validamos el correo
        if not correo or "@" not in correo or "." not in correo:
            raise ClienteInvalidoError(
                "El correo electronico no es valido."
            )

        # Validamos el telefono
        if not telefono or not str(telefono).isdigit():
            raise ClienteInvalidoError(
                "El telefono debe contener solamente numeros."
            )

        # Inicializamos la clase padre
        super().__init__(identificacion)

        # Encapsulamos los datos del cliente
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = str(telefono).strip()

    # Metodo para consultar el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Metodo para consultar el correo
    @property
    def correo(self):
        return self.__correo

    # Metodo para consultar el telefono
    @property
    def telefono(self):
        return self.__telefono

    # Metodo para consultar la identificacion
    @property
    def identificacion(self):
        return self._identificador

    # Metodo sobrescrito de la clase Entidad
    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Identificacion: {self._identificador} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )
