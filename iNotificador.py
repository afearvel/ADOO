from abc import ABC, abstractmethod

class iNotificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificadorEmail(iNotificador):
        def enviar(self, mensaje):
            print(f"Enviando email: {mensaje}")

class NotificadorSMS(iNotificador):
        def enviar(self, mensaje):
            print(f"Enviando SMS: {mensaje}")

class NotificadorWhatsApp(iNotificador):
        def enviar(self, mensaje):
            print(f"Enviando WhatsApp: {mensaje}")

# 1. Creamos la abstracción (Interfaz)
# - INotificador
# 2. Implementaciones concretas
# - NotificadorEmail
# - NotificadorSMS
# 3. Nueva funcionalida
# - NotificadorWhatsApp
class GestorNotificaciones:
    def __init__(self, notificador: iNotificador):
        self.notificador = notificador

    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
gestor = GestorNotificaciones(NotificadorWhatsApp())
gestor.notificar_usuario("Hola, tu pedido ha sido enviado.")
# Resultado : Enviando WhatsApp: Hola, tu pedido ha sido enviado.

