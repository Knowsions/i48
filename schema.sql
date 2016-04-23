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
    values('11111', '2016/04/30',500,'Karimcho Fernandez',4777789786,'karim@correo.com',
    'Av. Siempre Viva 123',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('22222', '2016/05/07',1500,'Cosme Fulanito',4777789786,'cosme@correo.com',
    'Av. Chinbollo 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('33333', '2016/04/28',700,'Leonard Nimochatelas',4777798986,'leonard@correo.com',
    'calle Fresco del Chuy 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('44444', '2016/05/10',1000,'Aquino Esta',4777788376,'aquibo@correo.com',
    'Aquino Vive sin numero',1);
    
    