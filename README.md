# Gestor de Tareas

Aplicación web para gestionar tareas desarrollada con Flask y MySQL.  
Permite crear, visualizar, editar y eliminar tareas mediante una interfaz web integrada con un backend en Python.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- HTML
- Bootstrap

## Requerimientos del proyecto

Este proyecto fue desarrollado como trabajo práctico del programa Codo a Codo Full Stack Python y cumple con los siguientes requerimientos:

    - La base de datos debe desarrollarse en lenguaje SQL
    - A través del front se debe poder realizar al menos un tipo de alta. (POST)
    - De la misma forma se debe poder realizar modificaciones de los registros
    - Se debe poder acceder a los registros de la tabla (GET)
    - Se debe poder realizar borrado físico de los datos. (DELETE)
    - El trabajo práctico deberá compartirse mediante un repositorio de Github
    - El backend debe estar integrado con un frontend

## Funcionalidades

- Crear nuevas tareas
- Visualizar lista de tareas
- Editar tareas existentes
- Eliminar tareas
- Registrar fecha límite de cada tarea

## Estructura del proyecto

```text
src/
│
├── app.py
│
├── static/
│   └── styles.css
│
├── templates/
│   ├── header.html
│   ├── footer.html
│   └── tareas/
│       ├── index.html
│       ├── create.html
│       └── edit.html
│
├── .gitignore
├── db-definition.sql
├── README.md
└── requirements.txt
```

## Instrucciones para Ejecutar el Proyecto

1. Clonar el repositorio:

```bash
   git clone https://github.com/giseladevicente/Gestor-de-Tareas.git
```

2. Crear y activar entorno virtual:

```bash
python -m venv venv

# En Windows:
source venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:

Copiar el archivo de ejemplo y crear tu configuración local

```bash
cp src/config_example.py src/config.py
```

Luego, abrir src/config.py y completar con los datos de tu instalación de MySQL/XAMPP.

5. Ejecutar la aplicación:

```bash
python src/app.py
```
