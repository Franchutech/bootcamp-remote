-- Crear tabla estudiantes
CREATE TABLE estudiantes (
    id_estudiante SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear tabla cursos
CREATE TABLE cursos (
    id_curso SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear tabla inscripciones (relación muchos a muchos)
CREATE TABLE inscripciones (
    id_estudiante INT REFERENCES estudiantes(id_estudiante),
    id_curso INT REFERENCES cursos(id_curso),
    PRIMARY KEY (id_estudiante, id_curso)
);

-- Insertar datos
INSERT INTO estudiantes (nombre) VALUES ('Ana'), ('Juan'), ('María');
INSERT INTO cursos (nombre) VALUES ('Python'), ('SQL'), ('Power BI');
INSERT INTO inscripciones (id_estudiante, id_curso) VALUES
(1,1),(1,2),(2,2),(3,3);
