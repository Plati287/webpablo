# Mòdul 6: Capa d'enllaç de dades

## Topologías físicas y lógicas:

Topología física: Muestra cómo los dispositivos están conectados físicamente.
Topología lógica: Define las conexiones virtuales entre dispositivos mediante interfaces y esquemas de direccionamiento IP.
## Topologías WAN:

Punto a punto: Enlace permanente entre dos puntos finales.
Hub and spoke: Nodo central que interconecta sitios de sucursal con enlaces punto a punto.
Malla: Alta disponibilidad con todos los sistemas conectados entre sí, requiere más enlaces.
## Topología WAN de punto a punto:

Conexión directa entre dos nodos, sin compartir medios con otros hosts, y protocolos simples.
## Topologías LAN:

Estrella y estrella extendida: Fáciles de instalar, escalables y simples de solucionar.
Bus: Sistemas conectados en cadena, terminando en ambos extremos.
Anillo: Sistemas conectados a sus vecinos formando un anillo.
## Comunicación dúplex:

Semidúplex: Solo un dispositivo envía o recibe a la vez, usado en WLAN y topologías de bus antiguas.
Dúplex completo: Ambos dispositivos pueden transmitir y recibir simultáneamente, usado en switches Ethernet.
## Métodos de control de acceso:

Acceso basado en contención:
CSMA/CD: Usado en LAN Ethernet de bus, detecta colisiones y retransmite.
CSMA/CA: Usado en WLAN, previene colisiones informando sobre la duración de la transmisión.
Acceso controlado: Cada nodo tiene un tiempo asignado en el medio, usado en redes como Token Ring y ARCNET.

## La trama:

La capa de enlace de datos encapsula los datos con un encabezado y un tráiler para formar una trama.
Las tramas tienen tres partes: encabezado, datos y tráiler, con variaciones según el protocolo de enlace.
## Camps de la trama:

Inicio y fin de trama: Marca el inicio y fin de la trama.
Dirección: Indica el nodo de origen y destino.
Tipo: Identifica el protocolo de Capa 3 encapsulado.
Control: Señala los servicios de control de flujo.
Datos: Contiene la carga útil.
Detección de errores: Permite verificar errores de transmisión.
## Direcciones de Capa 2:

También conocidas como direcciones físicas, se incluyen en el encabezado de la trama y se usan solo para la entrega local.
## Tramas LAN y WAN:

La topología lógica y los medios físicos determinan el protocolo de enlace de datos, que puede ser Ethernet, 802.11 (inalámbrico), PPP, HDLC o Frame Relay.