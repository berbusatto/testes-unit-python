create database api;

use api;

create table name (
	id_name integer primary key auto_increment,
	nome varchar(255)
);

select * from name;
insert into name (nome) values ('Teste');
select * from name;
