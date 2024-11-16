
## 2.1 – Accés a Cisco IOS

### Sistemes Operatius:

- **Shell**: Interfaz de usuario para solicitar tareas, a través de CLI (interfaz de línea de comandos) o GUI (interfaz gráfica).
- **Kernel**: Gestiona la comunicación entre el hardware y el software y administra los recursos del hardware.
- **Maquinari**: Parte física de una computadora (electrónica subyacente).

### GUI (Interfaz Gráfica de Usuario):

- Interfaz que permite interactuar con el sistema usando iconos, menús y ventanas.
- Es más fácil de usar y requiere menos conocimiento de comandos que la CLI.
- **Ejemplos**: Windows, macOS, Linux KDE, Apple iOS, Android.
- Las GUI pueden presentar fallos, y en dispositivos de red se prefiere el acceso por CLI.

### Cisco IOS:

- **Propósito**:
  - Facilita a los usuarios el uso de dispositivos mediante CLI o GUI, permitiendo la ejecución de programas, introducción de comandos y visualización de resultados.
- **Métodos de Acceso**:
  - **Consola**: Puerto físico para acceder y realizar configuraciones iniciales en dispositivos.
  - **SSH (Secure Shell)**: Conexión CLI remota segura a través de la red.
  - **Telnet**: Conexión CLI remota no segura (envía datos en texto claro).

### Programa de Emulación de Terminal:

- Software que permite la conexión a dispositivos de red mediante consola, SSH o Telnet.
- **Ejemplos**: PuTTY, Tera Term, SecureCRT.

## 2.2 – Navegació del IOS

### 1. Modos de Comando Principales en IOS:

- **Modo EXEC de Usuario**: Acceso a comandos básicos de monitoreo. Identificado por el símbolo `>`.
- **Modo EXEC Privilegiado**: Acceso a todos los comandos y funciones. Identificado por el símbolo `#`.

### 2. Modos de Configuración y Subconfiguración:

- **Modo de Configuración Global**: Acceso a opciones generales de configuración del dispositivo.
- **Modo de Configuración de Línea**: Configuración del acceso mediante consola, SSH, Telnet o AUX.
- **Modo de Configuración de Interfaz**: Configuración de un puerto de switch o una interfaz de enrutador.

### 3. Navegación entre Modos en IOS:

- **De EXEC de Usuario a EXEC Privilegiado**: Usar `enable`.
- **Para entrar y salir del Modo de Configuración Global**: Usar `configure terminal` y `exit`.
- **Para entrar y salir del Modo de Configuración de Línea**: Usar `line` seguido del tipo de línea, y `exit` para volver a Configuración Global.
- **Para salir de una subconfiguración y volver a Configuración Global**: Usar `exit`.
- **Para regresar a EXEC Privilegiado**: Usar `end` o `Ctrl + Z`.
- **Para cambiar entre subconfiguraciones directamente**: Usar el comando de la subconfiguración deseada (ejemplo: cambiar de `(config-line)#` a `(config-if)#`).

## 2.3 – Estructura dels comandos

### 1. Estructura Básica de los Comandos IOS:

- **Palabra Clave**: Parámetro específico predefinido en el sistema operativo, como `ip protocols`.
- **Argumento**: Valor o variable definida por el usuario, no predefinido, como `192.168.10.5`.

### 2. Sintaxis de los Comandos IOS:

- **Negrita**: Indica comandos y palabras clave que deben ingresarse literalmente.
- **Cursiva**: Representa argumentos donde el usuario proporciona el valor.
- **Convenciones de sintaxis**:
  - `[ ]`: Indica un elemento opcional (palabra clave o argumento).
  - `{ }`: Indica un elemento obligatorio.
  - `[x {i | z }]`: Una opción obligatoria dentro de un elemento opcional, con espacios que ayudan a delinear partes del comando.

### 3. Verificación de Sintaxis de Comandos:

- La sintaxis especifica el formato necesario para introducir comandos.
- **Ejemplos**:
  - `ping 10.10.10.5`: `ping` es el comando y `10.10.10.5` es el argumento (dirección IP del destino).
  - `traceroute 192.168.254.254`: `traceroute` es el comando y `192.168.254.254` es el argumento.

### 4. Funciones de Ayuda en IOS:

- **Ayuda contextual**: Proporciona asistencia para:
  - Ver comandos disponibles en cada modo.
  - Encontrar comandos que comienzan con ciertos caracteres.
  - Mostrar palabras clave y argumentos válidos para comandos específicos.
- **Verificación de sintaxis**: Asegura que el comando sea válido y muestra un mensaje de error si el intérprete no lo entiende.

### 5. Teclas de Acceso Rápido y Métodos Abreviados:

- **Tab**: Completa automáticamente una entrada parcial de comando.
- **Retroceso**: Borra el carácter a la izquierda del cursor.
- **Flechas**:
  - **Izquierda** (`Ctrl+B`): Mueve el cursor un carácter a la izquierda.
  - **Derecha** (`Ctrl+F`): Mueve el cursor un carácter a la derecha.
  - **Arriba** (`Ctrl+P`): Muestra comandos anteriores del historial.
- **Ctrl+C** y **Ctrl+Z**: Salen de cualquier modo de configuración y regresan al modo EXEC privilegiado.
- **Ctrl+Shift+6**: Interrumpe búsquedas DNS, traceroutes, y pings.
- **Tecla Enter**: Muestra la siguiente línea en salidas largas.
- **Barra Espaciadora**: Muestra la siguiente pantalla completa en salidas largas.

## 2.4 Configuració bàsica de dispositius

### 1. Asignación de Nombre de Dispositivo:

- Cada dispositivo debe tener un nombre único, comenzando y terminando con una letra o dígito, sin espacios y con un máximo de 64 caracteres.
- Para restaurar el nombre predeterminado, usa `no hostname`.

### 2. Configuración de Contraseñas:

- Las contraseñas deben ser seguras: de al menos 8 caracteres, mezclando mayúsculas, minúsculas, números y caracteres especiales.
- **Accesos configurables**:
  - **EXEC de usuario**: `line console 0`, luego `password` y `login`.
  - **EXEC privilegiado**: `enable secret password`.
  - **VTY (acceso remoto)**: `line vty 0 15`, seguido de `password` y `login`.

### 3. Encriptación de Contraseñas:

- Para evitar que las contraseñas se muestren en texto plano, utiliza `service password-encryption`.
- Verifica la encriptación con `show running-config`.

### 4. Mensajes de Banner:

- Configura un mensaje de advertencia (MOTD) con `banner motd #mensaje#`, donde `#` es un delimitador.
## 2.5 Guardar les configuracions

### Archivos de Configuración:

- **startup-config**: Configuración guardada en NVRAM, se carga al inicio del dispositivo.
- **running-config**: Configuración activa en RAM, se pierde al reiniciar.

### Guardar Cambios:

- Copiar la configuración actual (`running-config`) a la de inicio (`startup-config`) con:
  
  - shell
  - copy running-config
  - startup-config
### Restauración de Configuración:

- Si los cambios no son los deseados: eliminar comandos específicos o usar `reload` para restaurar la configuración guardada.
- Para borrar toda la configuración guardada, usa `erase startup-config` y reinicia.

### Guardar Configuración en un Archivo de Texto:

- Captura la configuración usando un programa de terminal (ej. PuTTY) y el comando `show running-config` o `show startup-config`.
## 2.6 Ports i direccions

### 1. Direcciones IP:

- **IPv4**: Usada para identificar dispositivos y establecer comunicación. Se expresa en notación decimal con puntos (ej., `192.168.1.1`) y usa una máscara de subred de 32 bits para distinguir entre red y host.
- **IPv6**: Tiene 128 bits, expresados en hexadecimales separados por dos puntos (ej., `2001:0db8:85a3::8a2e:0370:7334`). IPv6 permite más direcciones y es insensible a mayúsculas o minúsculas.

### 2. Puerta de Enlace Predeterminada:

- Es la IP del router que permite al host acceder a redes externas, incluyendo Internet.

### 3. Interfaces y Puertos:

- Las comunicaciones de red dependen de interfaces físicas (ej., puertos de red) y de los cables que conectan los dispositivos, como cables de cobre trenzado, fibra óptica, coaxiales y redes inalámbricas.

### 4. Medios de Red:

- Cada medio tiene características y usos específicos:
  - **Distancia**: Máxima distancia de transmisión sin pérdida de señal.
  - **Ambiente**: Condiciones de instalación adecuadas.
  - **Velocidad**: Capacidad de datos y velocidad de transmisión.
  - **Coste**: Precio del material y su instalación.
## 2.7 Configuració d'adreces d'IP

### Configuración Manual de IP en Dispositivos Finales:

- Cada dispositivo necesita una dirección IP para comunicarse en la red.
- **Para asignar una dirección IPv4 manualmente en Windows**:
  - Abrir **Centro de redes y recursos compartidos**, seleccionar el adaptador de red, luego **Propiedades**, y establecer la IP y la máscara de subred en **Propiedades del protocolo TCP/IPv4**.

### Configuración Automática de IP mediante DHCP:

- **DHCP** permite la asignación automática de direcciones IPv4.
- En Windows, activa la opción de **obtener la dirección IP automáticamente** en las propiedades de TCP/IPv4.
- Para **IPv6**, se usa **DHCPv6** o **SLAAC** para una configuración dinámica.

### Configuración de IP en una Interfaz Virtual de Switch (SVI):

- Para habilitar la administración remota de un switch, se configura una IP en la interfaz VLAN.
- **Pasos básicos en CLI**:

  ```shell
  interface vlan 1
  ip address <dirección-ip> <máscara>
  no shutdown
