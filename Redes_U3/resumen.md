# 3.1 Les règles (Las reglas)

## Aspectos básicos de la comunicación:

Para que la comunicación sea efectiva, deben cumplirse tres elementos fundamentales:

- **Una fuente** (remitente).
- **Un destino** (receptor).
- **Un canal** (medio) que proporciona la ruta de la comunicación.

## Protocolos de comunicación:

- Todas las comunicaciones están gobernadas por **protocolos**, que son las reglas que regulan el proceso de comunicación.
- Estas reglas varían según el protocolo utilizado.

## Establecimiento de reglas:

Los protocolos deben cumplir con los siguientes requisitos:

1. **Identificación del emisor y receptor**.
2. **Lenguaje y gramática comunes**.
3. **Velocidad y momento de entrega**.
4. **Confirmación o justificación de recepción**.

## Requisitos de los protocolos de red:

Incluyen aspectos como:

### Codificación de mensajes:
- Transformar información a una forma adecuada para la transmisión.

### Formato y encapsulación:
- Aplicar una estructura específica al mensaje según el tipo y canal.

### Tamaño del mensaje:
- Convertir los datos en bits adecuados para el medio de transmisión.

### Sincronización del mensaje:
1. **Control de flujo**: Regula la velocidad y cantidad de datos transmitidos.
2. **Tiempo de espera de respuesta**: Administra cuánto tiempo espera un dispositivo para recibir respuesta.
3. **Método de acceso**: Define cuándo un dispositivo puede enviar datos, gestionando posibles colisiones.

## Opciones de entrega de mensajes:

1. **Unidifusión**: Comunicación de uno a uno.
2. **Multidifusión**: Comunicación de uno a muchos (pero no todos).
3. **Difusión**: Comunicación de uno a todos (IPv4 lo permite, pero no IPv6, que utiliza Anycast como alternativa).

## Notas adicionales:

- Se utiliza el ícono de nodo (normalmente un círculo) para representar dispositivos en diagramas.
# 3.2 Protocols (Protocolos)

## Descripción general del protocolo de red:

Los protocolos de red definen un conjunto de reglas comunes que los dispositivos utilizan para comunicarse.  
Pueden implementarse en:

- **Software**
- **Hardware**
- **Ambos**

Cada protocolo tiene:

- Su propia función.
- Un formato específico.
- Métodos de medición.

## Tipos de protocolos y sus descripciones:

1. **Comunicaciones de red**:  
   Permiten la comunicación entre dos o más dispositivos a través de una o más redes.

2. **Seguridad de red**:  
   Aseguran los datos mediante autenticación, integridad y cifrado.

3. **Encaminamiento**:  
   Permiten que los routers intercambien información de rutas y seleccionen la mejor.

4. **Detección de servicios**:  
   Facilitan la detección automática de dispositivos o servicios.

## Funciones de los protocolos de red:

Los dispositivos utilizan protocolos acordados para comunicarse. Estos pueden cumplir una o varias funciones, como:

- **Adreçament (Direccionamiento)**: Identificar un emisor y un receptor.
- **Confiança (Confiabilidad)**: Garantizar la entrega.
- **Control de flux (Control de flujo)**: Asegurar que los datos fluyan a una velocidad eficiente.
- **Seqüenciació (Secuenciación)**: Etiquetar de manera única cada segmento de datos transmitido.
- **Detecció d'errors (Detección de errores)**: Comprobar si los datos se dañaron durante la transmisión.
- **Interfície de l'aplicació (Interfaz de aplicación)**: Facilitar las comunicaciones entre procesos en aplicaciones de red.

## Interacción de protocolos:

Las redes requieren múltiples protocolos, cada uno con su propia función y formato.

### Ejemplo de interacción de protocolos:

- **HTTP**:  
  Regula la interacción entre un cliente y un servidor web, definiendo el formato y el contenido.

- **TCP**:  
  Administra las conversaciones individuales, garantiza la entrega y controla el flujo.

- **IP**:  
  Encargado de la entrega de mensajes de forma global desde el remitente hasta el receptor.

- **Ethernet**:  
  Proporciona la entrega de mensajes entre interfaces de red (NICs) dentro de una red local (LAN).
  # Puntos importantes del apartado 3.3
# Suites de Protocolos

## ¿Qué es una suite de protocolos?

Una suite de protocolos es un grupo de protocolos interrelacionados que trabajan en conjunto para realizar funciones de comunicación. Están organizados en:

- **Capas superiores**: Encargadas de la gestión de datos.
- **Capas inferiores**: Responsables del movimiento de datos y de ofrecer servicios a las capas superiores.

---

## Evolución de las suites de protocolos

### **TCP/IP**
- Es la suite de protocolos más común.
- Mantenida por el **IETF** (Internet Engineering Task Force).

### **OSI**
- Desarrollada por **ISO** (Organización Internacional de Normalización) y **UIT** (Unión Internacional de Telecomunicaciones).
- Menos utilizada en la práctica.

### **Suites propietarias**
- Ejemplos:
  - **AppleTalk** (Apple).
  - **Novell NetWare** (Novell).

---

## Protocolos en TCP/IP

- Operan en las capas de **Aplicación**, **Transporte** e **Internet**.
- Protocolos LAN más comunes: **Ethernet** y **WLAN**.

---

## Características del TCP/IP

1. Es un conjunto de estándares **abiertos**, disponibles para cualquier proveedor.
2. Ha sido aprobado por organizaciones de **estandarización del sector**.

---

## Proceso de comunicación TCP/IP

- El **servidor** encapsula los datos antes de enviarlos.
- El **cliente** desencapsula los datos para su uso.
# Puntos importantes del apartado 3.4: **Organizaciones estándar**

## Propósito de los estándares abiertos

- **Fomentar**:
  - La interoperabilidad.
  - La competencia.
  - La innovación.
- Las organizaciones encargadas son **neutrales** y **sin ánimo de lucro**.

---

## Principales organizaciones de estándares de Internet

1. **ISOC** (Sociedad de Internet):  
   - Promueve el desarrollo abierto de Internet.
2. **IAB** (Consejo de Arquitectura de Internet):  
   - Administra y desarrolla los estándares de Internet.
3. **IETF** (Grupo de Trabajo de Ingeniería de Internet):  
   - Desarrolla y mantiene las tecnologías TCP/IP.
4. **IRTF** (Grupo de Trabajo de Investigación de Internet):  
   - Investiga protocolos a largo plazo.

---

## Organizaciones de soporte de TCP/IP

1. **ICANN**:  
   - Coordina direcciones IP, nombres de dominio y protocolos.
2. **IANA**:  
   - Administra la asignación de direcciones IP y otros identificadores para ICANN.

---

## Organizaciones de estándares de comunicaciones y electrónica

1. **IEEE**:  
   - Establece estándares en telecomunicaciones, redes y más.
2. **EIA** y **TIA**:  
   - Desarrollan estándares en cableado eléctrico, radio y VoIP.
3. **ITU-T**:  
   - Crea estándares para IPTV, compresión de videos y banda ancha.
# Resumen del apartado 3.5: **Modelos de referencia**

## Importancia de los modelos en capas

Los modelos en capas facilitan la comprensión y diseño de redes al dividir sus funciones en niveles específicos.

---

## Beneficios de los modelos en capas

1. Simplifican la comprensión de conceptos complejos.  
2. Ayudan en el diseño de protocolos, definiendo funciones específicas para cada capa.  
3. Fomentan la **interoperabilidad** entre productos de diferentes proveedores.  
4. Aíslan los cambios tecnológicos, evitando que afecten otras capas.  
5. Proporcionan un lenguaje común para describir redes.  

---

## Modelos más utilizados

1. **Modelo OSI** (Interconexión de Sistemas Abiertos):  
   - Compuesto por **7 capas**.  
2. **Modelo TCP/IP**:  
   - Tiene **4 capas**, utilizadas principalmente en Internet.  

---

## Capas del modelo OSI

1. **Física**: Manejo de conexiones físicas.  
2. **Enlace de datos**: Intercambio de tramas entre dispositivos.  
3. **Red**: Dirección y enrutamiento de datos.  
4. **Transporte**: Segmentación y transferencia de datos.  
5. **Sesión**: Gestión del intercambio de datos.  
6. **Presentación**: Formateo y codificación de datos.  
7. **Aplicación**: Interacción directa con el usuario final.  

---

## Capas del modelo TCP/IP

1. **Acceso a red**: Manejo de hardware y medios de red.  
2. **Internet**: Enrutamiento y direccionamiento.  
3. **Transporte**: Comunicación entre dispositivos.  
4. **Aplicación**: Interacción con el usuario y control de diálogos.  
## Comparación entre las estructuras de capas OSI y TCP/IP

### **Estructura de capas**

- **Modelo OSI**:  
  - Tiene **7 capas**.
  - Proporciona más detalle al desglosar en subcapas las funciones de acceso a red y aplicación presentes en TCP/IP.

- **Modelo TCP/IP**:  
  - Consta de **4 capas**.
  - Agrupa funcionalidades en menos niveles, simplificando su estructura.

---

### **Flexibilidad de TCP/IP**

- TCP/IP no especifica protocolos para la transmisión en medios físicos.  
- Esto permite mayor diversidad en las implementaciones.

---

### **Capas inferiores en OSI**

- **Física**:  
  - Detalla el acceso a medios físicos para establecer y mantener conexiones.  
- **Enlace de datos**:  
  - Enfocada en el envío de datos en la red mediante tramas.
