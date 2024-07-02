CREATE DATABASE IF NOT EXISTS tareas;
USE tareas;
CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_limite DATE
);

-- select * from tareas;