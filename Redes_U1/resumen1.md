# Roles de Host

Los hosts o dispositivos finales son computadoras conectadas a la red. 

## Servidores
Computadoras que proporcionan servicios como correo electrónico, web y almacenamiento de archivos. 

## Clientes
Equipos que solicitan información a los servidores, como acceder a una página web o descargar correos electrónicos. 

# Redes Punto a Punto

En una red punto a punto, los dispositivos pueden actuar tanto como clientes como servidores. Este tipo de red es adecuado solo para redes muy pequeñas. 

**Ventajas:** Fácil de configurar, menos costoso, y adecuado para tareas simples como compartir archivos o impresoras. 

**Desventajas:** Falta de seguridad, administración descentralizada, no es escalable y tiene un rendimiento limitado. 

# Dispositivos Finales

Los dispositivos finales son aquellos en los que los datos se originan o se reciben, como computadoras o teléfonos conectados a la red. 

# Dispositivos de Red Intermedios

Los dispositivos intermedios conectan los dispositivos finales y gestionan el tráfico de datos. Ejemplos: switches, puntos de acceso inalámbricos, routers y firewalls. 

**Funciones:** Transmitir y regenerar señales de datos, mantener información sobre las rutas de la red, y notificar fallos de comunicación. 

# Medios de Red

La comunicación en una red se realiza a través de diferentes tipos de medios: 

- **Cables metálicos:** Usan impulsos eléctricos. 
- **Fibra óptica:** Usa pulsos de luz. 
- **Transmisión inalámbrica:** Usa ondas electromagnéticas moduladas.


# Representaciones de Red

Los diagramas de red o diagramas de topología utilizan símbolos para representar los diferentes dispositivos que forman parte de una red.

## Términos importantes

- **Puerto físico:** Punto donde se conecta un dispositivo a la red.
- **Interfaz:** Conexión lógica entre el dispositivo y la red.
- **NIC (Tarjeta de interfaz de red):** Hardware que permite a un dispositivo conectarse a la red.

# Diagramas de Topología

- **Topología física:** Muestra la ubicación física de los dispositivos en la red y cómo están conectados con cables.
- **Topología lógica:** Representa los dispositivos, los puertos y el esquema de direccionamiento en la red, mostrando cómo fluye la información de un dispositivo a otro.

# Redes de muchos tamaños

- **Redes pequeñas (SOHO):** Conectan algunas computadoras en un hogar o pequeña oficina a Internet.
- **Redes medianas o grandes:** Conectan múltiples sitios con cientos o miles de computadoras.
- **Redes mundiales:** Interconectan millones de computadoras a nivel global, como ocurre con Internet.

# LANs y WANs

- **LAN (Local Area Network):** Red que cubre una pequeña área geográfica, como una oficina o un edificio. Se encarga de interconectar dispositivos finales en una área limitada.
- **WAN (Wide Area Network):** Red que cubre grandes áreas geográficas, interconectando varias LANs. Generalmente es administrada por uno o más proveedores de servicios y tiene enlaces de menor velocidad comparado con una LAN.

# Internet

- **Internet:** Una colección global de LANs y WANs interconectadas. Ninguna persona u organización es dueña de Internet, pero se mantienen estándares mediante organizaciones como el IETF, ICANN, y IAB.

# Intranet y Extranet

- **Intranet:** Red privada que conecta LANs y WANs internas de una organización, accesible solo para sus miembros o usuarios autorizados.
- **Extranet:** Proporciona acceso limitado y seguro a la red de una organización a usuarios externos o colaboradores, como socios comerciales.

# Tecnologías de acceso a Internet

Existen diversas formas de conectar usuarios y organizaciones a Internet:

- **Banda ancha por cable:** Proporcionada por proveedores de servicios de televisión por cable.
- **DSL (Línea de suscriptor digital):** Conexión de banda ancha que utiliza líneas telefónicas.
- **Redes WAN inalámbricas y servicios móviles:** Conexiones a través de redes celulares.
- **Satélite:** Ideal para áreas rurales sin otros proveedores de Internet.

# Conexiones para oficinas pequeñas y hogares (SOHO)

- **Cable:** Conexión de banda ancha permanente ofrecida por proveedores de televisión por cable.
- **DSL:** Conexión de banda ancha que siempre está disponible y funciona a través de una línea telefónica.
- **Red celular:** Conexión a través de redes de telefonía móvil.
- **Satélite:** Útil en áreas rurales donde no hay otros servicios de Internet disponibles.
- **Conexión por marcación telefónica:** Opción económica, pero con baja velocidad, que utiliza un módem.

# Conexiones empresariales

Las empresas requieren conexiones de mayor capacidad, como:

- **Líneas dedicadas arrendadas:** Circuitos reservados para conectar oficinas distantes.
- **WAN Ethernet:** Extiende la tecnología de red LAN hacia la WAN.
- **DSL empresarial:** Incluye formatos como DSL simétrico (SDSL).
- **Satélite:** Útil cuando no hay otras opciones de conexión.

# Red convergente

Las redes convergentes integran servicios de datos, voz y video en una única infraestructura, en lugar de tener redes separadas para cada servicio.

Esta convergencia permite transportar diferentes tipos de información por el mismo enlace de red, usando las mismas reglas y normas.

# Arquitectura de red

La arquitectura de red debe cumplir con cuatro características esenciales para garantizar su fiabilidad:

- **Tolerancia a fallos**
- **Escalabilidad**
- **Calidad de servicio (QoS)**
- **Seguridad**

## Tolerancia a fallos

Una red con tolerancia a fallos minimiza el impacto de las fallas limitando la cantidad de dispositivos afectados mediante rutas redundantes.

Utiliza conmutación por paquetes, donde los datos se dividen en pequeños paquetes que se enrutan por la red y pueden tomar diferentes caminos para llegar a su destino.

## Escalabilidad

Una red escalable puede expandirse rápidamente sin afectar el rendimiento de los servicios a los usuarios actuales.

Se logran redes escalables utilizando normas y protocolos aceptados que permiten agregar más usuarios o servicios sin pérdida de eficiencia.

## Calidad de servicio (QoS)

QoS garantiza una entrega confiable del tráfico en tiempo real, como voz y video, gestionando el flujo de datos de manera eficiente.

Esto es crucial cuando la demanda de ancho de banda supera la capacidad disponible, para evitar interrupciones y asegurar que los servicios críticos tengan prioridad.

## Seguridad de la red

La seguridad de la red aborda dos áreas principales:

- **Seguridad de la infraestructura:** Protección física de los dispositivos de red y prevención de accesos no autorizados.
- **Seguridad de la información:** Protección de los datos transmitidos para asegurar confidencialidad, integridad y disponibilidad.

  - **Confidencialidad:** Solo los destinatarios autorizados pueden leer los datos.
  - **Integridad:** Asegura que los datos no se modifiquen durante la transmisión.
  - **Disponibilidad:** Asegura que los datos estén accesibles para los usuarios autorizados cuando sea necesario.

# Tendencias recientes

Las redes están en constante evolución para adaptarse a nuevas tecnologías y dispositivos. Algunas de las tendencias más relevantes que afectan a organizaciones y consumidores son:

- **BYOD (Bring Your Own Device):** Permite a los usuarios utilizar sus propios dispositivos personales, como laptops, teléfonos inteligentes y tabletas, para acceder a la red de la empresa o institución. Proporciona más flexibilidad y libertad a los usuarios para comunicarse y acceder a la información desde cualquier lugar.

- **Colaboración en línea:** Facilita el trabajo conjunto de las personas a través de herramientas colaborativas como Cisco WebEx, permitiendo la interacción instantánea. La colaboración en línea es cada vez más importante para las empresas y la educación, ya que permite compartir archivos, enviar mensajes instantáneos y realizar videoconferencias.

- **Comunicaciones de video:** Las videollamadas y videoconferencias se han convertido en una herramienta esencial para la comunicación efectiva a nivel global. Cisco TelePresence permite realizar reuniones virtuales que brindan una experiencia colaborativa más interactiva.

- **Computación en la nube:** La computación en la nube permite a los usuarios almacenar archivos y acceder a aplicaciones a través de servidores en Internet, en lugar de tener infraestructura física local.

  - **Nubes públicas:** Disponibles para el público en general.
  - **Nubes privadas:** Dedicadas a una organización específica.
  - **Nubes híbridas:** Combinan nubes públicas y privadas.
  - **Nubes personalizadas:** Diseñadas para satisfacer las necesidades de una industria específica.

# Tendencias tecnológicas en el hogar

La tecnología de hogar inteligente está creciendo y permite que los dispositivos cotidianos, como electrodomésticos, se interconecten para facilitar la automatización de tareas y mejorar la vida diaria.

## Redes por línea eléctrica

Las redes Powerline permiten a los dispositivos conectarse a la red local (LAN) a través del cableado eléctrico, lo que resulta útil en áreas donde las comunicaciones inalámbricas o de red no son viables.

## Banda ancha inalámbrica

Además de DSL y cable, la banda ancha inalámbrica es una opción común en áreas rurales. Se conecta a través de proveedores de servicios inalámbricos (WISP) y utiliza la misma tecnología de las redes celulares.

# Objetivos de seguridad

La seguridad de la red debe garantizar que los datos sean:

- **Confidenciales:** Solo los usuarios autorizados deben poder acceder a la información.
- **Íntegros:** Los datos no deben ser modificados ni alterados durante su transmisión o almacenamiento.
- **Disponibles:** Los usuarios autorizados deben tener acceso a la información cuando la necesiten.

# Amenazas de seguridad

La seguridad de la red es crucial para proteger la integridad, confidencialidad y disponibilidad de los datos que circulan por ella. Las redes están expuestas a diversas amenazas, tanto internas como externas:

### Amenazas externas

Son ataques provenientes de fuera de la red y suelen ser intencionados. Algunos ejemplos son:

- **Virus, gusanos y troyanos:** Software malicioso que puede replicarse o ejecutarse sin el consentimiento del usuario, dañando sistemas y robando información.
- **Spyware y adware:** Programas que recopilan información de los usuarios sin su conocimiento o que muestran publicidad no deseada.
- **Ataques de día cero:** Vulnerabilidades explotadas antes de que haya una solución o parche disponible.
- **Ataques de denegación de servicio (DoS):** Sobrecargan los recursos de una red o sistema, impidiendo su funcionamiento normal.
- **Intercepción de datos:** El robo de información mientras está siendo transmitida.
- **Robo de identidad:** Uso no autorizado de la información personal de un usuario con fines fraudulentos.

### Amenazas internas

Pueden provenir de empleados o usuarios dentro de la organización. Pueden ser accidentales o malintencionadas:

- **Dispositivos perdidos o robados:** Acceso no autorizado a datos sensibles si un dispositivo cae en manos equivocadas.
- **Errores humanos:** Uso indebido o accidental de sistemas que puede comprometer la seguridad.
- **Empleados malintencionados:** Personas con acceso interno que deliberadamente dañan o roban información.

# Soluciones de seguridad

Para proteger la red contra estas amenazas, se implementan diversas capas de seguridad que trabajan conjuntamente para reforzar la protección:

### En redes pequeñas o domésticas

- **Antivirus y antispyware:** Software instalado en los dispositivos para detectar y eliminar software malicioso.
- **Firewalls:** Dispositivos o software que filtran el tráfico y bloquean accesos no autorizados a la red.

### En redes empresariales grandes

- **Firewalls dedicados:** Sistemas de seguridad más complejos que protegen grandes redes y gestionan el tráfico entre diferentes segmentos.
- **Listas de control de acceso (ACL):** Reglas que controlan qué tráfico tiene permitido o denegado el acceso a la red.
- **Sistemas de prevención de intrusiones (IPS):** Monitorean el tráfico en tiempo real y detienen cualquier intento de ataque.
- **Redes privadas virtuales (VPN):** Proveen conexiones seguras y cifradas para que los usuarios puedan acceder remotamente a la red sin comprometer su seguridad.
