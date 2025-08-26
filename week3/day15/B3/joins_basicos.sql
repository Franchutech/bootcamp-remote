-- INNER JOIN para ver estudiantes y cursos inscritos
SELECT e.nombre AS estudiante, c.nombre AS curso
FROM inscripciones i
INNER JOIN estudiantes e ON i.id_estudiante = e.id_estudiante
INNER JOIN cursos c ON i.id_curso = c.id_curso;
