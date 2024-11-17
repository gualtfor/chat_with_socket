CREATE SCHEMA IF NOT EXISTS hrAirline;

DROP TABLE IF EXISTS hrAirline.departamento CASCADE;
CREATE TABLE hrAirline.departamento (
    id_departamento INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    gerente VARCHAR(100),
    descripcion VARCHAR(100),
    fecha_inicial DATE,
    fecha_final DATE DEFAULT '9999-01-01'
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_departamento ON hrAirline.departamento (id_departamento);

DROP TABLE IF EXISTS hrAirline.profesion CASCADE;
CREATE TABLE hrAirline.profesion (
    id_profesion INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100),
    dotacion_vestido BOOLEAN,
    requiere_experiencia BOOLEAN,
    nivel VARCHAR(20) NOT NULL,
    tipo VARCHAR(50),
    fecha_inicial DATE,
    fecha_final DATE DEFAULT '9999-01-01'
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_profesion ON hrAirline.profesion (id_profesion);

DROP TABLE IF EXISTS hrAirline.expediente CASCADE;
CREATE TABLE hrAirline.expediente (
    id_expediente INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_empleado INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100),
    documento_realizado VARCHAR(50),
    nivel VARCHAR(50),
    afecta_cv BOOLEAN,
    fecha_reporte DATE DEFAULT CURRENT_DATE,
    fecha_final_reporte DATE DEFAULT '9999-01-01'
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_expediente ON hrAirline.expediente (id_expediente);

DROP TABLE IF EXISTS hrAirline.aviones CASCADE;
CREATE TABLE hrAirline.aviones (
    id_avion INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100),
    tipo VARCHAR(20) NOT NULL,
    marca VARCHAR(20) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    fecha_inicio DATE DEFAULT CURRENT_DATE,
    fecha_final DATE DEFAULT '9999-01-01'
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_avion ON hrAirline.aviones (id_avion);

DROP TABLE IF EXISTS hrAirline.sedes CASCADE;
CREATE TABLE hrAirline.sedes (
    id_sede INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100),
    activo BOOLEAN NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    nombre_calle VARCHAR(50),
    n_calle_av VARCHAR(50),
    n_casa VARCHAR(50),
    fecha_inicial DATE DEFAULT CURRENT_DATE,
    fecha_cierre DATE DEFAULT '9999-01-01'
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_sedes ON hrAirline.sedes (id_sede);

DROP TABLE IF EXISTS hrAirline.empleados CASCADE;
CREATE TABLE hrAirline.empleados (
    id_empleado INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    numero_identidad INT NOT NULL,
    fecha_de_nacimiento DATE NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL,
    estado_civil VARCHAR(50) NOT NULL,
    genero VARCHAR(20) NOT NULL CHECK (genero IN ('M', 'F')),
    ciudad_residencia VARCHAR(20) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono BIGINT NOT NULL,
    fecha_contrato DATE NOT NULL,
    fecha_renuncia DATE DEFAULT '9999-01-01',
    jefe_inmediato VARCHAR(100),
    id_sede INT,
    id_profesion INT,
    id_departamento INT,
    id_avion INT,
    FOREIGN KEY (id_sede) REFERENCES hrAirline.sedes(id_sede),
    FOREIGN KEY (id_profesion) REFERENCES hrAirline.profesion(id_profesion),
    FOREIGN KEY (id_departamento) REFERENCES hrAirline.departamento(id_departamento),
    FOREIGN KEY (id_avion) REFERENCES hrAirline.aviones(id_avion)
);
CREATE UNIQUE INDEX IF NOT EXISTS index_id_empleado ON hrAirline.empleados (id_empleado);