# Examen de Conmutación Ethernet

## Preguntas

### 1. ¿Cuál es la longitud estándar de una dirección MAC en Ethernet?
* A) 6 bytes
* B) 8 bytes
* C) 12 bytes
* D) 4 bytes

### 2. ¿Qué protocolo se utiliza para determinar la dirección MAC asociada a una dirección IPv4?
* A) ARP
* B) ICMP
* C) TCP
* D) UDP

### 3. ¿Qué indica una dirección MAC de destino FF-FF-FF-FF-FF-FF?
* A) Dirección de difusión
* B) Dirección de unidifusión
* C) Dirección de multidifusión
* D) Ninguna de las anteriores

### 4. ¿Qué subcapa de Ethernet es responsable del control de acceso a los medios?
* A) MAC
* B) LLC
* C) FCS
* D) TCP

### 5. ¿Cuál es el rango válido en hexadecimal para una dirección MAC?
* A) 00 a FF
* B) 00 a EE
* C) 01 a FE
* D) 00 a AB

### 6. ¿Qué ocurre si una trama Ethernet tiene menos de 64 bytes?
* A) Se considera un "fragmento de colisión"
* B) Se reenvía automáticamente
* C) Se clasifica como "jumbo"
* D) Se almacena en el switch

### 7. ¿Cuál es el tamaño máximo de una trama Ethernet estándar?
* A) 1518 bytes
* B) 1024 bytes
* C) 2048 bytes
* D) 64 bytes

### 8. ¿Qué dirección MAC se utiliza en una transmisión de multidifusión en IPv4?
* A) 01-00-5E
* B) FF-FF-FF-FF-FF-FF
* C) 00-00-00-00-00-00
* D) 33-33

### 9. ¿Qué método de switching se caracteriza por reenviar la trama antes de recibirla completamente?
* A) Cut-through
* B) Store-and-forward
* C) Switching por memoria compartida
* D) Switching asimétrico

### 10. ¿Qué tipo de switching permite la detección de errores en la trama antes de reenviarla?
* A) Store-and-forward
* B) Cut-through
* C) Fast switching
* D) Switching sin fragmentos

### 11. ¿En qué subcapa de Ethernet se encuentra el control de acceso a los medios?
* A) MAC
* B) LLC
* C) FCS
* D) IP

### 12. ¿Qué tecnología permite negociar automáticamente la mejor velocidad y modo dúplex?
* A) Autonegociación
* B) CSMA/CD
* C) VLAN
* D) Spanning Tree

### 13. ¿Qué ocurre si un switch recibe una trama con una dirección MAC de destino desconocida?
* A) Reenvía la trama por todos los puertos excepto el de entrada
* B) Descartar la trama
* C) La envía al puerto específico
* D) La guarda en un buffer

### 14. ¿Cuál es el propósito de la subcapa LLC en Ethernet?
* A) Identificar el protocolo de capa de red
* B) Controlar el acceso a los medios
* C) Definir las direcciones físicas
* D) Realizar la detección de errores

### 15. ¿Qué ocurre si hay una discrepancia en la configuración de dúplex entre dos dispositivos?
* A) Pueden ocurrir problemas de rendimiento
* B) No hay problema, se ajustan automáticamente
* C) Se activa el modo de baja latencia
* D) Ambos funcionan en dúplex completo

### 16. ¿Qué estándar corresponde a la capa física en Ethernet?
* A) IEEE 802.3
* B) IEEE 802.2
* C) IEEE 802.11
* D) IEEE 802.1Q

### 17. ¿Qué tipo de memoria se utiliza para almacenar tramas antes de reenviarlas en un switch?
* A) Buffer
* B) RAM
* C) ROM
* D) EEPROM

### 18. ¿Qué dirección MAC es válida para unidifusión?
* A) 00:1A:2B:3C:4D:5E
* B) FF:FF:FF:FF:FF:FF
* C) 01:00:5E:00:00:01
* D) 33:33:00:00:00:01

### 19. ¿Cuál es el intervalo de tiempo predeterminado en el que un switch mantiene una entrada en la tabla de direcciones MAC?
* A) 5 minutos
* B) 1 minuto
* C) 10 minutos
* D) 15 minutos

### 20. ¿Qué componente verifica la integridad de una trama Ethernet?
* A) FCS (Frame Check Sequence)
* B) LLC
* C) MAC
* D) IP

### 21. ¿Qué indica una configuración de dúplex completo?
* A) Ambos extremos pueden enviar y recibir simultáneamente
* B) Solo un extremo puede enviar a la vez
* C) Ninguno puede recibir al mismo tiempo
* D) Solo puede funcionar a 10 Mbps

### 22. ¿Cuál es el nombre alternativo de la tabla de direcciones MAC en un switch?
* A) Tabla CAM
* B) Buffer de memoria
* C) Tabla LLC
* D) Mapa de red

### 23. ¿Qué método de switching es recomendado para redes convergentes que requieren calidad de servicio?
* A) Store-and-forward
* B) Cut-through
* C) Fast switching
* D) Switching basado en puerto

### 24. ¿Qué hace el comando "mdix auto" en un switch?
* A) Habilita la detección automática del tipo de cable
* B) Desactiva la detección de colisiones
* C) Establece la velocidad de transmisión
* D) Configura el switch en modo dúplex completo

### 25. ¿Qué longitud tiene una dirección MAC expresada en hexadecimal?
* A) 12 dígitos hexadecimales
* B) 8 dígitos hexadecimales
* C) 16 dígitos hexadecimales
* D) 6 dígitos hexadecimales

### 26. ¿Cuál es el propósito del campo EtherType en una trama Ethernet?
* A) Identificar el protocolo de capa superior
* B) Especificar la dirección MAC de destino
* C) Indicar la longitud de la trama
* D) Detectar errores en la transmisión

### 27. ¿Qué ocurre si una trama tiene errores detectados por la CRC?
* A) Se descarta automáticamente
* B) Se reenvía al origen
* C) Se guarda en el buffer
* D) Se envía a todos los puertos

### 28. ¿Qué estándar describe la encapsulación de datos en la subcapa MAC?
* A) IEEE 802.3
* B) IEEE 802.1X
* C) IEEE 802.11
* D) IEEE 802.15

### 29. ¿Qué tipo de dispositivo se utiliza para segmentar una red en dominios de colisión?
* A) Switch
* B) Hub
* C) NIC
* D) Repetidor

### 30. ¿Qué característica ofrece la conmutación sin fragmentos?
* A) Reduce colisiones al verificar los primeros 64 bytes de la trama
* B) Reenvía tramas antes de recibirlas por completo
* C) Garantiza la máxima latencia en la red
* D) Evita la detección de errores en la trama