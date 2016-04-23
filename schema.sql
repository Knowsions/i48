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
