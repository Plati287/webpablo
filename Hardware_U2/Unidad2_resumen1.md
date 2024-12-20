# Definition of a Computer System

A computer system is a set of components designed to receive data (input), process it, and produce a meaningful result (output). It consists of:

1. **Hardware**: The physical, touchable components, like the keyboard, mouse, monitor, motherboard, and hard disk.
2. **Software**: The intangible, logical components, including the operating system, applications, and data.
3. **Human Component**: The people involved in the design, management, and use of computer systems, including IT staff and users.

The primary parts of a computer system are the CPU, memory, input/output devices, and storage devices, working together as a single unit to produce desired outputs. Examples include smartphones, tablets, PCs, servers, and supercomputers.

---

# The Five Generations of Computer Systems

Each generation of computers brought key advancements in technology, size, cost, and functionality.

### First Generation (1940s - 1950s)

- **Technology**: Used vacuum tubes for circuitry and magnetic drums for memory.
- **Programming**: Programs were written in machine language. Input was primarily through punch cards.
- **Characteristics**: Large, heavy, and consumed high amounts of power. Prone to overheating and frequent failures, requiring specialized cooling.
- **Example computers**: ENIAC (1945), UNIVAC (1951).

### Second Generation (1950s - 1960s)

- **Technology**: Transistors replaced vacuum tubes, making computers faster, smaller, and more energy-efficient.
- **Programming**: Programs were written in assembly language and high-level languages like COBOL and FORTRAN.
- **Memory**: Used magnetic core memory for faster data access.
- **Characteristics**: Reduced size, cost, and heat generation compared to first-generation computers. More reliable and required less power.
- **Example**: IBM 7094, UNIVAC 1108.

### Third Generation (1960s - 1970s)

- **Technology**: Integrated Circuits (ICs), which placed multiple transistors on a single silicon chip, replaced individual transistors.
- **Programming**: Supported high-level (COBOL, PASCAL or BASIC) languages and introduced Operating Systems that allowed multitasking and time-sharing.
- **Memory**: Magnetic disk storage became more common, providing greater data storage capacity and faster access (semiconductor memory and magnetic disks).
- **Characteristics**: Smaller, more powerful, and more reliable than previous generations. Significantly reduced cost.
- **Example**: IBM 370 and PDP-8

### Fourth Generation (1970s - 1980s)

- **Technology**: Microprocessors integrated thousands of ICs on a single chip, creating the first microcomputers (IBM personal computers).
- **Programming**: Supported advanced high-level languages and Graphical User Interfaces (GUIs) (C, C++ and DBASE)
- **Memory**: Introduced semiconductor memory (RAM and ROM), significantly increasing memory efficiency.
- **Characteristics**: Small, affordable, and accessible for businesses and individuals. Marked the rise of personal computing, GUI use operating system and floppy disks
- **Example**: IBM 4341 nad STAR 1000

### Fifth Generation (1980s - Present)

- **Technology**: Artificial Intelligence (AI), parallel processing, quantum computing research, and advanced microprocessors.
- **Programming**: Emphasizes AI technologies, machine learning, and natural language processing.
- **Memory**: High-speed, large-capacity storage, including solid-state drives (SSDs) and cloud storage.
- **Characteristics**: Compact, highly powerful, and able to perform complex tasks. Continuous advancements in AI, machine learning, voice recognition, and robotics. Designed for interconnectivity and networking, ULSI
- **Example**: Smartphones, Supercomputers like IBM Watson and Fujitsu’s Fugaku.


# Von Neumann Architecture: Essential Concepts

The Von Neumann architecture, introduced by John von Neumann in 1945, is based on the stored-program concept, where instructions and data are stored together in one memory unit. This innovation allows computers to run various programs by simply loading them from memory, unlike early machines (e.g., ENIAC), which needed manual rewiring to change tasks.

## Core Components of Von Neumann Architecture

1. **Central Processing Unit (CPU)**: Executes instructions and performs calculations.
2. **Memory Unit**: Stores both data and program instructions in the same space, enabling easy access and flexibility.
3. **Input/Output Devices**: Facilitate data exchange between the computer and external devices (e.g., keyboard, monitor).
4. **Buses**: Communication pathways that transfer data and instructions between the CPU, memory, and I/O devices.

This architecture is the foundation of most modern computers, enabling them to be general-purpose and versatile.

## Central Processing Unit (CPU)

The CPU is the main electronic circuit responsible for executing a computer program’s instructions and managing the overall system operations. Programs are sets of instructions written in programming languages (e.g., C#, Java) that need to be loaded into main memory (RAM) to be executed. The operating system translates these instructions into machine instructions that the CPU can interpret, performing tasks like addition, subtraction, or data loading. The set of machine instructions a CPU can handle is known as its instruction set and is unique to each processor.

### Key Components within the CPU

- **Arithmetic and Logic Unit (ALU)**: Executes arithmetic operations (e.g., add, subtract) and logical operations (e.g., and, or, not).
- **Control Unit (CU)**: Manages the operations of the ALU, memory, and I/O devices, directing them based on program instructions. It interprets program instructions, controls data movement between main memory and registers, and commands the ALU to perform specific operations.
- **Registers**: Small storage units within the CPU that temporarily hold data needed to execute instructions.

Modern CPUs may also include additional components, like cache memory and sometimes even a Graphics Processing Unit (GPU), which will be covered in further detail later.

### 3.1 Control Unit (CU)

- **Contador de Programa (PC)**: Registro que contiene la dirección de la siguiente instrucción a ejecutar.
- **Registro de Instrucción (IR)**: Registro que contiene la instrucción actual, con el código de operación y los datos involucrados.
- **Decodificador**: Extrae y analiza el código de operación de la instrucción actual y envía señales de control para su ejecución.
- **CPU Clock**: Genera pulsos regulares que marcan el ritmo para ejecutar instrucciones; su velocidad se mide en hercios (Hz).
- **Secuenciador**: Ejecuta instrucciones de la máquina creando microórdenes básicas en cada ciclo de reloj.

### 3.1.2 Arithmetic and Logic Unit (ALU)

- **ALU**: Performs logical, arithmetic, and bit-shifting operations on data received from the control unit.
- **Accumulator (AC)**: Special register that stores intermediate results of logical and arithmetic operations.
- **Status Register**: Indicates special conditions like negative results or overflow.
- **Floating Point Unit (FPU)**: Specialized circuit for performing mathematical operations with floating-point numbers, following the IEEE 754 standard for precision.

### 3.1.3 Registers

**Registers**: High-speed memory cells inside the CPU for storing temporary data, faster than conventional memory. Their size is based on the number of bits they handle (e.g., 8, 16, 32, 64 bits).

#### Types of Registers

1. **User Accessible Registers**: Can be accessed by the user to optimize resource usage.
   - **Address Registers**: Hold memory addresses for data or instructions.
   - **Data Registers**: Hold data.
   - **Flag Registers**: Indicate conditions such as positive, negative, null results, or overflow.

2. **Internal Registers**: Used for CPU internal operations, not user-accessible.
   - **Program Counter (PC)**: Holds the address of the next instruction to execute.
   - **Instruction Register (IR)**: Holds the current instruction.
   - **Memory Address Register (MAR)**: Contiene la direccion para leer o guardar la informacion
   - **Memory Buffer Register (MBR)**: Extrae los datos y los guarda en la RAM

## 3.2 Buses

**Buses**: Electrical or optical lines transmitting data between components like the CPU and memory, carrying groups of bits for communication.

### Types of Buses

- **Data Bus**: Permite cambiar datos entre CPU, RAM I/0 y se mide MHz o GHz
- **Address Bus**: Permite guardar las direcciones de los datos entre CPU y RAM. 
- **Control Bus**: Controla todas las actividades del ordenador

## 3.2 Memory Unit

The **Memory Unit** mainly consists of RAM (Random Access Memory) and ROM (Read-Only Memory). RAM stores data and instructions for active programs, enabling quick CPU access.

### Characteristics of RAM

- **Volatile**: Loses data when the computer is turned off.
- **Memory Cells**: Stores one word of data each, with unique memory addresses. Word size varies (e.g., 8, 16, 32, 64 bits) based on the microprocessor.
- **Random Access**: Data can be read/written without sequential order.

### Memory Operations

- **Memory Address Register (MAR)**: Contiene la direccion para leer o guardar la informacion
- **Memory Buffer Register (MBR)**: Extrae los datos y los guarda en la RAM
- **Control Unit**: Manages read/write operations by moving data between MAR and MBR.

## 3.25 Input and Output Unit (I/O Unit)

**I/O Unit**: Facilitates the exchange of information between the computer and external devices.

### Types of Peripherals

- **Input Peripherals**: Devices sending data to the computer (e.g., keyboard, mouse, webcam).
- **Output Peripherals**: Devices receiving data from the computer (e.g., monitor, printer).
- **Input/Output Peripherals**: Devices that send and receive data (e.g., touch screen).
- **Storage Peripherals**: Store data (e.g., hard drives, DVD drives, USB sticks).
- **Communication Peripherals**: Enable communication (e.g., network cards, Bluetooth cards).

### I/O Unit Function

The I/O unit interfaces between the CPU and peripherals, addressing speed and data format differences to ensure effective communication.

### I/O Modules

- **Peripheral Controllers**: Manage communication with the CPU.
- **I/O Ports**: Connect peripherals to the computer’s buses.

# CPU Features

- **Clock Speed**: Measures how many cycles the CPU executes per second, typically in gigahertz (GHz).
- **Instruction Set**: The collection of machine instructions a CPU can process. Some CPUs feature simpler instruction sets for basic operations, while others can handle both simple and complex operations, with complex operations often being slower.
- **Word, Data Bus, and Address Bus Size**: The size of these components determines how much data or address information the CPU can handle simultaneously.

## Memory Hierarchy

Memory in a computer system is organized in a hierarchy based on capacity, access speed, and cost per bit:

1. **CPU Registers**: Small, high-speed memory integrated into the CPU, used during instruction execution. They offer low capacity but very high speed.
2. **Cache Memory**: A fast memory that stores frequently accessed data and instructions, serving as a buffer between RAM and the CPU. This helps reduce data access time by avoiding slower RAM reads.
3. **Main Memory (RAM)**: Stores active program instructions and data. It has a larger capacity than cache but operates at a slower speed.
4. **Secondary Memory**: Provides permanent storage for data and programs. It has much greater capacity than main memory and is non-volatile, though slower. Examples include hard drives (HDD), solid-state drives (SSD), and optical media (CD/DVD).

# Cálculo del Tamaño Máximo de Memoria para Procesadores Intel Core i5-600

Los procesadores Intel Core i5-600 usan un bus de direcciones de 36 bits. Asumiendo que cada celda de memoria almacena 1 byte, calculamos el tamaño máximo de memoria en GiB.

## Explicación
Cada bit en el bus de direcciones se usa para referenciar un byte en la memoria.

### Paso 1: Calcular el total de bytes accesibles
- Total de bytes: 2^36

### Paso 2: Convertir a unidades superiores
- 2^36 bytes = 2^26 KiB
- 2^26 KiB = 2^16 MiB
- 2^16 MiB = 2^6 GiB

## Resultado
El máximo tamaño de memoria que puede manejar es **64 GiB**.

**La respuesta correcta es: 64**
