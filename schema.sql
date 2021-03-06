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
  telefono text,
  correo  varchar,
  direccion text,
  estatus integer
);

drop table if exists historial;
create table historial(
  id_historial integer primary key,
  detalle_siniestro text,
  monto_pago double,
  descuento integer,
  razon_descuento text,
  fecha_hora  bigint,
  id_poliza integer
);

insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('11111','Choque casual',  '553.24', '40', 'Es buena persona.', '1430098138');

insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('11111','Choque leve.',  '580.22', '10', 'Todo en regla.', '1451179738');

insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('11111','Choquecito',  '604.19', '0', 'Sin comentarios.', '1452389338');


insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('22222','Choque de frente',  '2176.01', '10', 'Se puso muy molesto, ya no queria nada.', '1430098138');

insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('22222','Choque de espadas',  '800.50', '30', 'Es de muchos años cliente.', '1451179738');

insert into historial(id_poliza, detalle_siniestro, monto_pago, descuento, razon_descuento, fecha_hora)
  values('22222','Choque de copas',  '1200', '13', 'Conocido de tiempo.', '1452389338');



--Insercion polizas 
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('11111', '2016/04/30',500,'Karimcho Fernandez','+524772398525','karim@correo.com',
    'Av. Siempre Viva 123',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('22222', '2016/05/07',1500,'Cosme Fulanito','+524772398525','cosme@correo.com',
    'Av. Chinbollo 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('33333', '2016/04/28',700,'Leonard Nimochatelas','+524772398525','leonard@correo.com',
    'calle Fresco del Chuy 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('44444', '2016/05/10',1000,'Aquino Esta','+524772398525','aquibo@correo.com',
    'Aquino Vive sin numero',1);
    
--otros
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('156253', '2016/04/30',5200,'Jesus Correa','+524772398525','yisus@correo.com',
    'Av. Siempre Viva 123',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('9384762', '2016/04/25',5800,'Homero J Simpson','+524772398525','jsimpson@correo.com',
    'Av. Chinbollo 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('273622', '2016/04/24',3000,'Patricio Estrella','+524772398525','estrella@correo.com',
    'calle Fresco del Chuy 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('823732', '2016/04/26',6625,'Calamardo Flautista','+524772398525','calamardo@correo.com',
    'Aquino Vive sin numero',1);
    
--otros mas
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('226352', '2016/04/30',5200,'Daniel Olalde','+524772398525','olalde@correo.com',
    'Av. Siempre Viva 123',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('8827362', '2016/04/25',5800,'Alejandra Montelongo','+524772398525','montelongo@correo.com',
    'Av. Monterrey 77',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('2887362', '2016/04/24',3000,'Fabian Cervantes','+524772398525','cervantes@correo.com',
    'calle Geteo 55',1);
    
insert into polizas(no_poliza, fecha_vencimiento,costo_renovacion,nombre_cliente,
  telefono,correo,direccion,estatus) 
    values('993827', '2016/04/26',6625,'Magdiel Pichiruche','+524772398525','pichiruche@correo.com',
    'Aquisi Vive ',1);
