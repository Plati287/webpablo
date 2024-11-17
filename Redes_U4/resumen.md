# Resumen del apartado 4.1

## 4.1 Propósito de la capa física

### Conexión física
#### Establecimiento de conexión
Para que pueda ocurrir cualquier comunicación de red, primero debe establecerse una conexión física a la red local. Esta conexión puede ser cableada o inalámbrica, dependiendo de la configuración de la red.

#### Tipos de conexiones
- Una oficina corporativa o un hogar requieren una conexión inicial a la red.
- Los dispositivos se conectan a la red mediante una tarjeta de interfaz de red (NIC).
- Algunos dispositivos poseen una única NIC, mientras que otros tienen múltiples (cableadas o inalámbricas).
- No todas las conexiones físicas ofrecen el mismo nivel de rendimiento.

### Funciones de la capa física
#### Transporte de bits
- La capa física se encarga de transportar bits individuales a través de los medios de red.
- Acepta una trama completa de la capa de enlace de datos y la codifica como una serie de señales que luego se transmiten a través del medio local.

#### Última etapa en el proceso de encapsulación
- Convierte los datos en señales físicas (eléctricas, ópticas o inalámbricas) y las envía a través del medio.
- En el dispositivo receptor, estas señales son decodificadas y reencapsuladas para decidir su procesamiento.
# 4.2 Características de la capa física

## Áreas funcionales
La capa física se define mediante estándares que abordan tres áreas funcionales principales:

### Componentes físicos
- Incluyen dispositivos de hardware, medios y conectores que transmiten las señales que representan los bits.
- **Ejemplos de componentes:**
  - Tarjetas de interfaz de red (NIC)
  - Interfaz y conectores
  - Materiales de cableado y diseños específicos según los estándares.

### Codificación
- Se refiere al proceso de convertir la secuencia de bits en un formato que pueda ser reconocido por el próximo dispositivo en la ruta de la red.
- La codificación proporciona patrones predecibles que facilitan la interpretación de los datos.
- **Ejemplos de métodos de codificación:**
  - Manchester
  - 4B/5B
  - 8B/10B

### Señalización
- Determina cómo se representan los valores de bits (1 y 0) en el medio físico.
- Varía según el tipo de medio utilizado:
  - **Cables de cobre:** usan señales eléctricas.
  - **Fibra óptica:** usan pulsos de luz.
  - **Medios inalámbricos:** usan señales de microondas.

---

## Características adicionales

### Ancho de banda
- Es la capacidad del medio para transportar datos.
- Medida como la cantidad de bits transmitidos por segundo (bps).
- **Ejemplos de unidades:**
  - bps (bits por segundo)
  - Kbps (kilobits por segundo, 10³ bps)
  - Mbps (megabits por segundo, 10⁶ bps)
  - Gbps (gigabits por segundo, 10⁹ bps)
  - Tbps (terabits por segundo, 10¹² bps)

### Terminología relacionada
- **Latencia:** tiempo que tardan los datos en viajar de un punto a otro.
- **Rendimiento:** cantidad de bits transferidos con éxito a través del medio en un tiempo dado.
- **Capacidad de transferencia útil (Goodput):**
  - Cantidad de datos útiles transferidos, excluyendo la sobrecarga del tráfico.
  - Se calcula como:
    ```math
    Goodput = Rendimiento − Sobrecarga \ de \ tráfico
    ```
# 4.3 Cablejat de coure

## Características del cableado de cobre
- Es el tipo de cable más comúnmente utilizado en redes debido a:
  - **Economía:** es barato en comparación con otros tipos de cableado.
  - **Facilidad de instalación.**
  - **Baja resistencia** al flujo de corriente eléctrica.

## Limitaciones
### Atenuación
- A medida que las señales eléctricas viajan más lejos, se debilitan.

### Interferencias
- Las señales eléctricas son susceptibles a:
  - **Interferencia Electromagnética (EMI).**
  - **Interferencia de Radiofrecuencia (RFI).**
  - **Diafonía (Crosstalk):** interferencia entre pares de cables cercanos.

## Medidas de mitigación
- Cumplimiento estricto con los límites de longitud del cableado para reducir la atenuación.
- Uso de:
  - **Blindaje metálico** y conexión a tierra para minimizar EMI y RFI.
  - **Cables trenzados** para reducir la diafonía entre pares.
# Tipos de cableado de cobre

## 1. Parell trenat sense blindatge (UTP)
- Es el cableado más común en redes Ethernet.
- **Conectores:** termina con conectores RJ-45.
- **Usos:** interconecta hosts con dispositivos de red intermediarios.

### Características:
1. La funda externa protege los cables contra daños físicos.
2. Los pares trenzados minimizan interferencias.
3. Aislamiento plástico de colores para identificar pares.

---

## 2. Parell trenat blindat (STP)
- Proporciona mejor protección frente al ruido (EMI/RFI) que UTP.
- **Conectores:** termina con conectores RJ-45.
- **Usos:** interconecta hosts con dispositivos de red intermediarios.
- **Desventajas:** más caro y difícil de instalar.

### Características:
1. Funda exterior para evitar daños físicos.
2. Blindaje trenzado o de lámina metálica para proteger contra EMI/RFI.
3. Escudo de aluminio para cada par de cables.
4. Aislamiento plástico para identificar y aislar los pares.

---

## 3. Cable coaxial
### Estructura:
1. Funda externa para proteger de daños físicos menores.
2. Trenza metálica o lámina que actúa como escudo y segundo conductor.
3. Capa de aislamiento plástico.
4. Conductor central de cobre para transmitir señales.

### Usos:
1. Conexión de antenas a dispositivos inalámbricos.
2. Cableado para Internet en instalaciones de clientes.
# 4.4 Cablejat UTP

## Propiedades del cableado UTP

### Estructura
- Formado por cuatro pares de hilos de cobre codificados por colores.
- Encerrados en una funda de plástico flexible.
- **Características**:
  - No tiene blindaje, pero limita la diafonía (interferencia entre pares) mediante:
    - **Cancelación**: Los cables de cada par usan polaridades opuestas (uno positivo, otro negativo), lo que permite que los campos magnéticos se cancelen.
    - **Variación en los giros**: Cada par tiene un número diferente de giros por pie, lo que reduce la interferencia entre pares cercanos.

## Estándares y conectores del cableado UTP
- **Definidos por la TIA/EIA**, especifican:
  - Tipos de cables.
  - Longitudes máximas.
  - Conectores y métodos de terminación.
  - Métodos de prueba.
- **Características eléctricas y clasificación** (definidas por IEEE):
  - **Categoría 3**: Para redes básicas.
  - **Categorías 5 y 5e**: Para redes más rápidas.
  - **Categoría 6**: Para mayores velocidades.

### Conector RJ-45
- El conector estándar para cableado UTP.
- **Ejemplos de terminaciones**:
  - Cable UTP mal terminado.
  - Cable UTP correctamente terminado.

## Tipos de cables UTP

### Cable directo (Straight-through)
- Ambos extremos tienen la misma configuración (**T568A** o **T568B**).
- **Uso**: Conectar un host a un dispositivo de red, como un switch o router.

### Cable cruzado (Crossover)
- Un extremo tiene configuración **T568A** y el otro **T568B**.
- **Uso**: Conectar dispositivos similares, como switch a switch o router a router.
- **Nota**: Considerado obsoleto en gran medida debido a la función **Auto-MDIX**, que permite a los dispositivos detectar automáticamente el tipo de cable.

### Cable de consola
- **Uso**: Conectar un host al puerto de consola de un switch o router.
- **Características**:
  - Exclusivo de Cisco.
  - Incluye un adaptador de puerto serie.
### apartado 4.5 Cablejat de fibra òptica
# Propiedades del cableado de fibra óptica

## Propiedades generales
- **Costo**: No es tan común como el UTP debido a su coste.
- **Uso ideal**: Escenarios específicos de redes.
- **Ventajas**:
  - Menos susceptible a la atenuación.
  - Completamente inmune a EMI (Interferencia Electromagnética) y RFI (Interferencia de Radiofrecuencia).
- **Material**: Fabricado con fibras de vidrio muy puras y flexibles.
- **Transmisión**: Utiliza láseres o LEDs para codificar los bits como pulsos de luz.
- **Diseño**: Minimiza la pérdida de señal.

## Tipos de medios de fibra

### Fibra monomodo (SMF)
- **Características**:
  - Núcleo pequeño.
  - Usa láseres costosos.
- **Uso**: Aplicaciones de larga distancia.

### Fibra multimodo (MMF)
- **Características**:
  - Núcleo más grande.
  - Usa LEDs más económicos.
  - Distancia máxima: 550 metros con hasta 10 Gbps.
  - Mayor dispersión que la SMF, lo que puede disminuir la intensidad de señal.

## Usos del cableado de fibra óptica
- **Redes empresariales**: Backbone y conexión entre dispositivos de infraestructura.
- **FTTH (Fibra hasta el hogar)**: Banda ancha para viviendas y pequeñas empresas.
- **Redes de larga distancia**: Conexiones entre ciudades o países.
- **Redes submarinas**: Conexiones transoceánicas con alta fiabilidad.

## Conectores de fibra óptica
- **Tipos destacados**:
  - **ST (Straight Tip)**.
  - **SC (Subscriber Connector)**.
  - **LC simplex**.
  - **LC multimode dúplex**.

## Cordones de conexión de fibra óptica
- **Ejemplos**:
  - Cables SC-SC multimode.
  - LC-LC monomode.
  - ST-LC multimode.
  - ST-SC monomode.
- **Codificación de colores**:
  - Amarillo: Fibra monomodo.
  - Naranja (o aqua): Fibra multimodo.
# Comparativa entre cableado de cobre y fibra óptica

## Ancho de banda soportado
- **Cableado de cobre (UTP)**: Soporta entre **10 Mbps y 10 Gbps**.
- **Fibra óptica**: Maneja velocidades más altas, de hasta **100 Gbps**.

## Distancia máxima
- **Cobre**: Ideal para distancias cortas, generalmente entre **1 y 100 metros**.
- **Fibra óptica**: Cubre distancias mucho mayores, de **1 a 100 kilómetros**.

## Inmunidad a interferencias electromagnéticas y de radiofrecuencia (EMI/RFI)
- **Cobre**: Baja inmunidad, susceptible a interferencias.
- **Fibra óptica**: Completamente inmune a EMI y RFI, lo que la hace más confiable en entornos con muchas fuentes de interferencia.

## Inmunidad a peligros eléctricos
- **Cobre**: Baja resistencia a peligros eléctricos, como picos de tensión.
- **Fibra óptica**: Totalmente inmune, ya que no depende de señales eléctricas.

## Costes de medios y conectores
- **Cobre**: Materiales y conectores más económicos.
- **Fibra óptica**: Coste significativamente más alto.

## Habilidades necesarias para la instalación
- **Cobre**: Fácil de instalar, requiere habilidades básicas.
- **Fibra óptica**: Instalación más compleja, requiere herramientas especializadas y habilidades avanzadas.

## Precauciones de seguridad
- **Cobre**: Requiere pocas precauciones.
- **Fibra óptica**: Materiales frágiles y uso de láseres para transmitir señales exigen mayores precauciones durante su manipulación.
### 4.6 Mitjans sense fils
# Propiedades de los medios inalámbricos

## Características
- Transportan señales electromagnéticas que representan dígitos binarios mediante frecuencias de radio o microondas.
- **Ventajas**:
  - Ofrecen **movilidad** y **flexibilidad** en la conexión de dispositivos.
  - Su uso sigue creciendo debido a su conveniencia.

## Limitaciones de la tecnología inalámbrica

### Cobertura limitada
- La cobertura efectiva varía según las características físicas del lugar de implementación.

### Interferencias
- Las señales inalámbricas son vulnerables a interferencias por:
  - Dispositivos electrónicos comunes.
  - Otros sistemas inalámbricos.

### Seguridad
- Las señales, al no requerir un medio físico, pueden ser captadas fácilmente, incrementando el riesgo de acceso no autorizado.

### Medio compartido
- Las redes inalámbricas suelen operar en semidúplex:
  - Solo un dispositivo puede transmitir o recibir a la vez.
  - Esto puede reducir el ancho de banda disponible si hay muchos dispositivos conectados.

## Tipos de medios inalámbricos
- **Aspectos clave de la capa física**:
  - Métodos de codificación de datos en señales de radio.
  - Frecuencia e intensidad de transmisión.
  - Requisitos de recepción y descodificación.
  - Diseño y construcción de antenas.

## Principales estándares inalámbricos
- **Wi-Fi (IEEE 802.11)**: Redes de área local inalámbricas (WLAN).
- **Bluetooth (IEEE 802.15)**: Redes de área personal inalámbricas (WPAN).
- **WiMAX (IEEE 802.16)**: Acceso inalámbrico de banda ancha en topología punto a multipunto.
- **Zigbee (IEEE 802.15.4)**: Aplicaciones de bajo consumo y baja velocidad, como el **Internet de las cosas (IoT)**.

## Dispositivos de una LAN inalámbrica
- **Puntos de acceso inalámbricos (AP)**:
  - Concentran señales inalámbricas de los usuarios.
  - Las conectan a una red de infraestructura basada en cobre.
- **Adaptadores NIC inalámbricos**:
  - Proveen capacidad de comunicación inalámbrica a los dispositivos de red.

## Consideraciones adicionales
- Es fundamental garantizar que los equipos WLAN sean compatibles e interoperables.
- Los administradores de red deben aplicar políticas y procesos estrictos para proteger las redes inalámbricas de accesos no autorizados y daños.
