
# excepciones.py

# Excepcion general para el sistema Software FJ
class SoftwareFJError(Exception):
    """Excepcion base para los errores del sistema."""
    pass


# Error cuando los datos de un cliente son incorrectos
class ClienteInvalidoError(SoftwareFJError):
    """Se genera cuando un cliente tiene datos invalidos."""
    pass


# Error cuando un servicio no cumple con las condiciones necesarias
class ServicioInvalidoError(SoftwareFJError):
    """Se genera cuando un servicio tiene datos incorrectos."""
    pass


# Error cuando una reserva no se puede realizar
class ReservaInvalidaError(SoftwareFJError):
    """Se genera cuando una reserva no es valida."""
    pass


# Error cuando se intenta realizar una operacion no permitida
class OperacionNoPermitidaError(SoftwareFJError):
    """Se genera cuando una operacion no esta permitida."""
    pass
