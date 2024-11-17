## Encapsulación Ethernet
Ethernet opera tanto en la capa de enlace de datos como en la capa física.
Es una familia de tecnologías de red definida en los estándares IEEE 802.2 y 802.3.
## Subcapas de la capa de enlace de datos
Subcapa LLC (IEEE 802.2): Identifica el protocolo de capa de red usado para la trama.
Subcapa MAC (IEEE 802.3, 802.11 o 802.15):
Encapsula los datos y controla el acceso a los medios.
Proporciona direccionamiento en la capa de enlace de datos.
# Responsabilidades de la subcapa MAC
Encapsulación de datos:
Incluye la estructura interna de la trama Ethernet.
Las direcciones MAC de origen y destino permiten la entrega en una LAN.
Incluye un tráiler FCS (Frame Check Sequence) para la detección de errores.
## Acceso a medios:
Define estándares para comunicación en medios como cobre y fibra.
## Los métodos de acceso varían:
Ethernet semidúplex utiliza CSMA/CD para detectar colisiones.
Ethernet dúplex completo elimina la necesidad de CSMA/CD.
## Especificaciones de tamaño de las tramas Ethernet
Tamaño mínimo: 64 bytes; tamaño máximo: 1518 bytes (sin incluir el preámbulo).
Las tramas menores de 64 bytes se consideran "fragmentos de colisión" y se descartan.
Las tramas mayores de 1500 bytes son "jumbos" o "tramas gigantes" y son compatibles con la mayoría de los switches y NIC modernos.

## Conceptos básicos sobre switches
Los switches Ethernet de capa 2 usan direcciones MAC para tomar decisiones de reenvío.
No tienen conocimiento de los datos transportados (protocolos) en la porción de datos de la trama.
Las decisiones de reenvío se basan únicamente en las direcciones MAC de capa 2.
Cuando un switch se enciende por primera vez, su tabla de direcciones MAC está vacía.
Nota: La tabla de direcciones MAC también se conoce como "tabla de memoria de contenido direccionable" (CAM).
 ## Aprendizaje del switch y reenvío
Aprender direcciones MAC de origen:

Cada trama entrante se revisa para obtener información nueva.
Se examina la dirección MAC de origen y el puerto de entrada:
Si la dirección MAC no está en la tabla, se agrega con el puerto correspondiente.
Si la dirección MAC ya existe, se actualiza el temporizador de la entrada (normalmente de 5 minutos).
Si la dirección MAC está asociada a un puerto diferente, se trata como una entrada nueva y se reemplaza.
Buscar direcciones MAC de destino (Reenvío):

Si la dirección MAC de destino es unidifusión y está en la tabla, el switch reenvía la trama por el puerto especificado.
Si no está en la tabla, la trama se reenvía por todos los puertos excepto el de entrada (flooding de unidifusión).
Para direcciones de difusión o multidifusión, la trama también se reenvía por todos los puertos excepto el de entrada.
## Filtrado de tramas
A medida que el switch recibe tramas, completa su tabla de direcciones MAC.
Si la tabla ya contiene la dirección MAC de destino, el switch puede filtrar la trama y reenviarla únicamente al puerto correspondiente.

# Métodos de reenvío de tramas en switches Cisco
## Commutació d’emmagatzematge i reexpedició (Store-and-Forward):

El switch recibe toda la trama antes de reenviarla.
Verifica la validez de la trama mediante el cálculo de la CRC (Cyclic Redundancy Check).
Si la CRC es válida, busca la dirección de destino y decide el puerto de salida.
Este método evita propagar tramas con errores y es fundamental para redes que necesitan QoS (Quality of Service).
## Commutació de tall (Cut-Through):

El switch comienza a reenviar la trama antes de recibirla completamente.
Solo almacena los datos necesarios para leer la dirección MAC de destino.
No verifica errores en la trama, lo que puede ocasionar la propagación de datos corruptos.
Variantes del método:
Avanç ràpid: Reenvía paquetes inmediatamente tras leer la dirección MAC de destino, ofreciendo la menor latencia.
Sense fragments: Verifica errores en los primeros 64 bytes para garantizar que no haya colisiones antes de reenviar.
# Memoria intermedia en switches
## Memoria basada en puerto:

Las tramas se almacenan en colas asociadas a puertos de entrada y salida específicos.
Una trama se transmite al puerto de salida solo cuando todas las tramas previas en la cola se han transmitido.
Puede generar demoras si hay tráfico en el puerto de destino.
## Memoria compartida:

Las tramas se almacenan en un buffer común compartido por todos los puertos del switch.
Permite asignar memoria dinámicamente según las necesidades del puerto.
Es útil para transmisiones asimétricas, donde algunos puertos necesitan más ancho de banda que otros.
# Configuración de velocidad y dúplex
## Configuraciones dúplex:

Full-duplex: Ambos extremos de la conexión pueden enviar y recibir simultáneamente.
Semidúplex: Solo un extremo puede transmitir a la vez.
## Autonegociación:

Permite que los dispositivos negocien automáticamente la mejor velocidad y configuración dúplex.
Es la configuración predeterminada en la mayoría de switches y NICs.
Nota: Los puertos Gigabit Ethernet funcionan exclusivamente en full-duplex.
## Problemas de desajuste de dúplex:

Ocurren cuando un puerto opera en semidúplex y el otro en full-duplex.
Puede causar problemas de rendimiento debido a colisiones.
## Función Auto-MDIX
Detecta automáticamente el tipo de cable conectado al puerto (directo o cruzado) y configura la interfaz en consecuencia.
Es una función habilitada por defecto en switches modernos con Cisco IOS 12.2(18) SE o posterior.
Nota: Aunque útil, se recomienda usar el tipo de cable correcto en entornos críticos.