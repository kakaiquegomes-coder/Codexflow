/*create database  biblioteca;*/
use biblioteca;

/*create table emprestimo(
    id_emprestimo int auto_increment primary key,
    dt_emprestimo date not null);

create table tbl_leitores(
    id_leitor int auto_increment primary key,
    nome_leitor varchar(100) not null,
    dt_nasc_leitor date not null,
    cpf_leitor varchar(14),
    fk_leitor_emprestimo int,
    constraint foreign key(fk_leitor_emprestimo) references emprestimo(id_emprestimo));

create table tbl_livros(
    id_livro int auto_increment primary key,
    nome_livro varchar(100) not null,
    dt_lancamento_livro date,
    genero_livro varchar(100),
    fk_livro_leitor int,
    constraint foreign key(fk_livro_leitor) references tbl_leitores(id_leitor));

create table tbl_autores(
    id_autor int auto_increment primary key,
    nome_autor varchar(100) not null,
    dt_nasc_autor date,
    fk_autores_livro int,
    constraint foreign key(fk_autores_livro) references tbl_livros(id_livro));

insert into emprestimo (dt_emprestimo)
 values
 ('2023-10-01');

insert into tbl_leitores (nome_leitor,dt_nasc_leitor, cpf_leitor, fk_leitor_emprestimo)
values('roberto','2008-04-21','123.578.325.12', 1);
insert into tbl_livros (nome_livro,dt_lancamento_livro,genero_livro,fk_livro_leitor)
values ('Dom Casmurro', '1899-01-01', 'Romance', 1);
insert into tbl_autores (nome_autor, dt_nasc_autor, fk_autores_livro)
values ('Machado de Assis', '1839-07-21', 1);

select tbl_autores.nome_autor, 
    tbl_livros.nome_livro, 
    tbl_leitores.nome_leitor, 
    emprestimo.dt_emprestimo
FROM tbl_autores
INNER JOIN tbl_livros 
ON tbl_autores.fk_autores_livro = tbl_livros.id_livro
INNER JOIN tbl_leitores
 ON tbl_livros.fk_livro_leitor = tbl_leitores.id_leitor
INNER JOIN emprestimo 
ON tbl_leitores.fk_leitor_emprestimo = emprestimo.id_emprestimo;*/

/*update tbl_livros
set nome_livro='harry potter'
where id_livro ='1'*/

/*update tbl_leitores
set nome_leitor='gabriel silva'	
where id_leitor='1'*/

/*update tbl_autores
set nome_autor='JK rowling'
where id_autor='1'*/

/*update emprestimo
set dt_emprestimo ='2026-09-09'
where id_emprestimo = '1'9*/