CREATE DATABASE IF NOT EXISTS APPCONSOLE;
USE APPCONSOLE;

CREATE TABLE USUARIOS(

    id  int(25) auto_increment not null,
    nombre  varchar(100) not null,
    apellidos varchar(255),
    email   varchar(255) not null,
    password varchar(255) not null,
    fecha   date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT unique_email UNIQUE(email)

)ENGINE=InnoDb;

CREATE TABLE NOTAS(

    id int(25) auto_increment NOT NULL,
    usuario_id int(25) NOT NULL,
    titulo varchar(255) NOT NULL,
    descripcion varchar(255) NOT NULL,
    fecha_creacion date NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT usuario_id FOREIGN KEY(usuario_id) REFERENCES USUARIOS(id)

)ENGINE=InnoDb;