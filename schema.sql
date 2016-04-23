drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);


drop table if exists catalogo_estatus;
create table catalogo_estatus(
  id integer not null,
  descripcion text not null 
);

insert into catalogo_estatus(id,descripcion) values(1,'Renovadas pendientes por pagar');
insert into catalogo_estatus(id,descripcion) values(2,'Notificado');
insert into catalogo_estatus(id,descripcion) values(3,'Renovada pagada');
insert into catalogo_estatus(id,descripcion) values(4,'Vencido');

drop table if exists polizas;
create table polizas(
  id_poliza integer primary key,
  no_poliza text not null,
  fecha_vencimiento date,
  costo_renovacion double,
  nombre_cliente text,
  telefono integer,
  correo  varchar,
  direccion text,
  estatus integer
);


insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('12345', '2016/04/30',500,Karimcho Fernandez,4777789786,'karim@correo.com',
    'Av. Siempre Viva 123',1);