
INSERT INTO hrairline.departamento(nombre, gerente, descripcion, fecha_inicial)
VALUES ('ventas', 'maria ester', 'departamento de ventas de tickets y cargos de equipaje', '2000-01-01'),
       ('operaciones', 'carlos puerto', 'manejo de aviones y de tripulacion', '2000-01-01'), 
       ('marketing', 'brian walsh', 'departamento de estrategia comercial y de ventas', '2000-01-01'),
       ('finanzas', 'christian swager', 'departamento de finanzas y control de ingresos y gastos', '2000-01-01'),
       ('mantenimiento', 'oscar mendez', 'departamento de mantenimiento y reparacion de aviones', '2000-01-01');
   
INSERT INTO hrairline.profesion(nombre, descripcion, dotacion_vestido, requiere_experiencia, nivel, tipo, fecha_inicial)
VALUES ('vendedor', 'encargado de la atencion al cliente en ventanilla', TRUE, True, 1, 'estacional', '2000-01-01'),
       ('azafata', 'encargado de la atencion al cliente en el avion', TRUE, TRUE, 1, 'fijo', '2000-01-01'), 
       ('piloto', 'encargado de manejar el avion', TRUE, TRUE, 'fijo', 3, '2000-01-01'),
       ('gerente', 'encargado del control de la empresa', FALSE, TRUE, 'servicios', 5, '2000-01-01'),
       ('supervisor en tierra', 'encargado del control de la operacion de tierra', TRUE, TRUE, 'fijo', 3, '2000-01-01');
   
INSERT INTO hrairline.expediente(id_empleado, tipo, descripcion, documento_realizado, nivel, afecta_cv, fecha_reporte)
VALUES (0, 'contratacion', 'Se realiza firma de contrato', 'contrato', 'alto', TRUE, '2024-10-01'),
       (1, 'aumento de salario', 'se ajusta el salario del trabajador', 'contrato', 'alto', TRUE, '2024-11-01'), 
       (2, 'vacaciones', 'se brindan las vacaciones al trabajador', 'reporte', 'bajo', FALSE, '2023-05-01'),
       (3, 'incapacidad', 'Se genera el reporte de incapacidad', 'reporte', 'medio', FALSE, '2023-10-01'),
       (4, 'renuncia', 'se genera el reporte de renuncia', 'paz y salvo', 'medio', TRUE, '2024-11-03');
   
INSERT INTO hrairline.aviones(nombre, descripcion, tipo, marca, estado)
VALUES ('747 – 400 ERF', 'avion de pasajeros y de carga', 'comercial', 'boeing', 'operativo'),
        ('320', 'avion de pasajeros y de carga', 'comercial', 'airbus', 'operativo'),
        ('737', 'avion de pasajeros y de carga', 'comercial', 'boeing', 'operativo'),
        ('777', 'avion de pasajeros y de alta carga', 'comercial', 'boeing', 'mantenimiento'),
        ('170-100LR', 'avion de pasajeros', 'comercial', 'embraer', 'operativo');

INSERT INTO hrairline.sedes(nombre, descripcion, activo, ciudad, nombre_calle, n_calle_av, n_casa, fecha_inicial)
VALUES ('ali-bogota', 'sede bogota', TRUE, 'bogota', 'mercedes', '100', '32-95', '2000-01-01'),
        ('ali-phonix', 'sede phoenix-Arizona', TRUE, 'phoenix', 'atlanta', 'atlanta', '22215 e 325', '2000-01-01'),
        ('ali-madrid', 'sede madrid-españa', TRUE, 'madrid', 'coruña', 'montes', '2587 e 325' , '2000-01-01'),
        ('ali-monterrey', 'sede monterrey-mexico', FALSE, 'monterrey', 'valle verde', 'el valle', '15a 256', '2000-01-01'),
        ('ali-medellin', 'sede medellin-colombia', TRUE, 'medellin', 'los cerezos', 'la puerta', '187a 23-98', '2000-01-01');

INSERT INTO hrairline.empleados(nombres, apellidos, numero_identidad, fecha_de_nacimiento, nacionalidad, estado_civil, genero, ciudad_residencia, direccion, telefono, fecha_contrato, jefe_inmediato, id_sede, id_profesion, id_departamento, id_avion)
VALUES ('christian camilo', 'gualteros forero', 12345, '1993-01-30', 'colombiana', 'soltero', 'M', 'bogota', 'calle 142 c 128 - 32', 3133776598, '2024-11-13', 'carlos puerto', 5, 5, 5, 5),
        ('juan carlos', 'carreño', 23587, '1980-05-15', 'colombiana', 'casado', 'M', 'cali', 'calle 72 c 28 - 32', 3125676598, '2024-11-12', 'carlos puerto', 1, 1, 1, 1),
        ('laura camila', 'puerto meneses', 69782, '1970-01-25', 'española', 'casado', 'F', 'madrid', 'coruña 2587 32', 3129876598, '2024-11-10', 'maria ester', 2, 2, 2, 2),
        ('jhon fredy', 'nieto cardenas', 69782, '1970-01-25', 'estadounidense', 'soltero', 'M', 'phoenix', 'atlanta 22215 e 32', 9169876598, '2024-11-09', 'brian walsh', 3, 3, 3, 3),
        ('isabel andrea', 'mahecha', 23568, '1960-01-25', 'italiana', 'casado', 'F', 'Atlanta', 'atlanta 30030 w 32 s 125', 91692536598, '2024-11-01', 'brian walsh', 4, 4, 4, 4);