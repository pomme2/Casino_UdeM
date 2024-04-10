--create database projdb;
go
--use projdb;
go
if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'recette' )
begin
	alter table recette drop constraint fk_recette_machine;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'panne' )
begin
	alter table panne drop constraint fk_panne_type;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'panne' )
begin
	alter table panne drop constraint fk_panne_personnel;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'machine_de_jeu' )
begin
	alter table machine_de_jeu drop constraint fk_machine_jeu;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'personnel' )
begin
	alter table personnel drop constraint fk_personnel_role;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'personnel' )
begin
	alter table personnel drop constraint fk_personnel_adresse;
end;

if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'pieces' )
begin
	alter table pieces drop constraint fk_pieces_fournisseur;
end;
if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'pieces' )
begin
	alter table pieces drop constraint fk_pieces_machine;
end;
if exists(SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
          WHERE TABLE_NAME = 'pieces' )
begin
	alter table pieces drop constraint fk_pieces_panne;
end;

drop table if exists type_panne;
drop table if exists jeu;
drop table if exists fournisseur;
drop table if exists pieces;
drop table if exists role_personnel;
drop table if exists adresse_civique;
drop table if exists recette;
drop table if exists panne;
drop table if exists machine_de_jeu;
drop table if exists distributeur_de_jeton;
drop table if exists panneau_affichage;
drop table if exists camera_surveillance;
drop table if exists outils_de_communication;
drop table if exists system_eclairage;
drop table if exists systeme_sonorisation;
drop table if exists personnel;

create table jeu(
	id int primary key,
	nom varchar(50),
	min_mise int,
	max_mise int
);


CREATE TABLE machine_de_jeu (
	id int primary key,
	date_service date,
	id_jeu int
);

create table distributeur_de_jeton(
	id int primary key,
	nombre_jeton int,
	date_service date
);

create table panneau_affichage(
	id int primary key,
	marque varchar(50),
	longueur int,
	largeur int,
);

create table camera_surveillance(
	id int primary key,
	secteur int,
);

create table outils_de_communication(
	id int primary key,
	type_comm varchar(10),
);

create table system_eclairage(
	id int primary key,
	nom varchar(50),
	min_luminosite int,
	max_luminosite int,
);
create table systeme_sonorisation(
	id int primary key,
	nom varchar(50),
	min_volume int,
	max_volume int,
);

create table adresse_civique(
	numero_adresse int,
	rue varchar(50),
	ville varchar(50),
	primary key(numero_adresse, rue, ville)
);

create table role_personnel(
	id int primary key,
	nom varchar(20),
	secteur int,
	expertise varchar(20),
	droit_acces int
);

create table personnel(
	id int primary key,
	nom varchar(50) not null,
	prenom varchar(50) not null,
	id_role int,
	numero_adresse int, 
	rue varchar(50), 
	ville varchar(50)
);

create table recette(
	id int primary key,
	date_recette date,
	profit decimal(19, 4),
	cout decimal(19, 4),
	information varchar(100),
	id_machine_de_jeu int,
	rentable binary,
);

create table type_panne(
	id int primary key,
	nom varchar(50),
	categorie varchar(20)
);

create table panne(
	id int primary key,
	id_type_panne int,
	date_panne date,
	id_personnel int
);

create table fournisseur(
	id int primary key,
	nom varchar(50),
	ville varchar(50)
);

create table pieces(
	id int primary key,
	nom varchar(50),
	date_service date,
	etat varchar(50),
	id_fournisseur int,
	id_machine_jeu int,
	id_panne int
);

alter table pieces add constraint fk_pieces_fournisseur foreign key (id_fournisseur) references fournisseur(id) ON DELETE CASCADE;
alter table pieces add constraint fk_pieces_machine foreign key (id_machine_jeu) references machine_de_jeu(id) ON DELETE CASCADE;
alter table pieces add constraint fk_pieces_panne foreign key (id_panne) references personnel(id) ON DELETE CASCADE;
alter table personnel add constraint fk_personnel_role foreign key (id_role) references role_personnel(id) ON DELETE CASCADE;
alter table personnel add constraint fk_personnel_adresse foreign key (numero_adresse, rue, ville) references adresse_civique(numero_adresse, rue, ville) ON DELETE CASCADE;
alter table machine_de_jeu add constraint fk_machine_jeu foreign key (id_jeu) references jeu(id) ON DELETE CASCADE;
alter table recette add constraint fk_recette_machine foreign key (id_machine_de_jeu) references machine_de_jeu(id) ON DELETE CASCADE;
alter table panne add constraint fk_panne_type foreign key (id_type_panne) references type_panne(id) ON DELETE CASCADE;
alter table panne add constraint fk_panne_personnel foreign key (id_personnel) references personnel(id) ON DELETE CASCADE;



INSERT INTO jeu (id, nom, min_mise, max_mise) VALUES
(1, 'Blackjack', 5, 500),
(2, 'Roulette', 2, 300),
(3, 'Poker', 10, 1000),
(4, 'Baccarat', 25, 1000),
(5, 'Slot Machine', 1, 100);

INSERT INTO machine_de_jeu (id, date_service, id_jeu) VALUES
(1, '2023-01-01', 1),
(2, '2023-02-01', 2),
(3, '2023-03-01', 3),
(4, '2023-04-01', 4),
(5, '2023-05-01', 5);

INSERT INTO distributeur_de_jeton (id, nombre_jeton, date_service) VALUES
(1, 500, '2023-01-15'),
(2, 600, '2023-02-15'),
(3, 700, '2023-03-15'),
(4, 800, '2023-04-15'),
(5, 900, '2023-05-15');

INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES
(1, 'Samsung', 100, 50),
(2, 'LG', 120, 60),
(3, 'Sony', 110, 55),
(4, 'Philips', 130, 65),
(5, 'Panasonic', 140, 70);

INSERT INTO camera_surveillance (id, secteur) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO outils_de_communication (id, type_comm) VALUES
(1, 'Radio'),
(2, 'Phone'),
(3, 'Intercom'),
(4, 'Email'),
(5, 'Text');

INSERT INTO system_eclairage (id, nom, min_luminosite, max_luminosite) VALUES
(1, 'Spotlight', 100, 1000),
(2, 'Ambient Light', 50, 500),
(3, 'Track Light', 75, 750),
(4, 'LED Panel', 60, 600),
(5, 'Halogen', 100, 1000);

INSERT INTO systeme_sonorisation (id, nom, min_volume, max_volume) VALUES
(1, 'Basic PA', 10, 100),
(2, 'Surround Sound', 20, 200),
(3, 'Concert System', 30, 300),
(4, 'Studio Quality', 40, 400),
(5, 'Outdoor Event', 50, 500);

INSERT INTO adresse_civique (numero_adresse, rue, ville) VALUES
( 101, 'Main St', 'Montreal'),
( 202, 'Second St', 'Quebec City'),
( 303, 'Third St', 'Sherbrooke'),
( 404, 'Fourth St', 'Ottawa'),
( 505, 'Fifth St', 'Toronto');

INSERT INTO role_personnel (id, nom, secteur, expertise, droit_acces) VALUES
(1, 'Manager', 1, 'Administration', 5),
(2, 'Security', 2, 'Surveillance', 4),
(3, 'Dealer', 3, 'Games', 3),
(4, 'Technician', 4, 'Maintenance', 4),
(5, 'Croupier', 3, 'Card Games', 3);

INSERT INTO personnel (id, nom, prenom, id_role, numero_adresse, rue, ville) VALUES
(1, 'Doe', 'John', 1, 101, 'Main St', 'Montreal'),
(2, 'Smith', 'Jane', 2, 202, 'Second St', 'Quebec City'),
(3, 'Brown', 'Bob', 3, 303, 'Third St', 'Sherbrooke'),
(4, 'Green', 'Alice', 4, 404, 'Fourth St', 'Ottawa'),
(5, 'White', 'Tom', 5, 505, 'Fifth St', 'Toronto');

INSERT INTO recette (id, date_recette, profit, cout, information, id_machine_de_jeu, rentable) VALUES
(1, '2023-04-01', 1000.00, 500.00, 'Good day', 1, 1),
(2, '2023-04-02', 800.00, 300.00, 'Average day', 2, 1),
(3, '2023-04-03', 200.00, 400.00, 'Bad day', 3, 0),
(4, '2023-04-04', 500.00, 200.00, 'Steady day', 4, 1),
(5, '2023-04-05', 300.00, 150.00, 'Slow day', 5, 1);

INSERT INTO type_panne (id, nom, categorie) VALUES
(1, 'Software Glitch', 'Software'),
(2, 'Mechanical Failure', 'Hardware'),
(3, 'Power Supply Issue', 'Electrical'),
(4, 'Screen Malfunction', 'Hardware'),
(5, 'Network Issue', 'Software');

INSERT INTO panne (id, id_type_panne, date_panne, id_personnel) VALUES
(1, 1, '2023-04-05', 1),
(2, 2, '2023-04-06', 2),
(3, 3, '2023-04-07', 3),
(4, 4, '2023-04-08', 4),
(5, 5, '2023-04-09', 5);

INSERT INTO fournisseur (id, nom, ville) VALUES
(1, 'Tech Supplies Inc.', 'Montreal'),
(2, 'Gaming Gear Ltd.', 'Quebec City'),
(3, 'Casino Equip Co.', 'Sherbrooke'),
(4, 'Entertainment Solutions', 'Montreal'),
(5, 'Professional Gaming Inc.', 'Toronto');

INSERT INTO pieces (id, nom, date_service, etat, id_fournisseur, id_machine_jeu, id_panne) VALUES
(1, 'Chipset', '2023-05-01', 'New', 1, 1, 1),
(2, 'Motherboard', '2023-06-01', 'Used', 2, 2, 2),
(3, 'Power Supply', '2023-07-01', 'Refurbished', 3, 3, 3),
(4, 'Joystick', '2023-08-01', 'New', 4, 4, 4),
(5, 'Button Set', '2023-09-01', 'New', 5, 5, 5);

DELETE FROM jeu WHERE id =1;
DELETE FROM machine_de_jeu WHERE id =1;
DELETE FROM distributeur_de_jeton WHERE id =1;
DELETE FROM panneau_affichage WHERE id =1;
DELETE FROM camera_surveillance WHERE id =1;
DELETE FROM outils_de_communication WHERE id =1;
DELETE FROM system_eclairage WHERE id =1;
DELETE FROM systeme_sonorisation WHERE id =1;
DELETE FROM role_personnel WHERE id =1;
DELETE FROM personnel WHERE id =1;
DELETE FROM recette WHERE id =1;
DELETE FROM type_panne WHERE id =1;
DELETE FROM panne WHERE id =1;
DELETE FROM fournisseur WHERE id =1;
DELETE FROM pieces WHERE id =1;

UPDATE jeu
SET 
    nom = 'New Name',
    min_mise = 10,
    max_mise = 1000
WHERE
    id = 1;
UPDATE machine_de_jeu
SET 
    date_service = '2024-04-09',
    id_jeu = 1
WHERE
    id = 1;
UPDATE distributeur_de_jeton
SET 
    nombre_jeton = 100,
    date_service = '2024-04-09'
WHERE
    id = 1;
UPDATE panneau_affichage
SET 
    marque = 'New Brand',
    longueur = 100,
    largeur = 50
WHERE
    id = 1;
UPDATE camera_surveillance
SET 
    secteur = 2
WHERE
    id = 1;

UPDATE outils_de_communication
SET 
    type_comm = 'New Type'
WHERE
    id = 1;
UPDATE system_eclairage
SET 
    nom = 'New Name',
    min_luminosite = 50,
    max_luminosite = 100
WHERE
    id = 1;
UPDATE systeme_sonorisation
SET 
    nom = 'New Name',
    min_volume = 20,
    max_volume = 80
WHERE
    id = 1;
UPDATE role_personnel
SET 
    nom = 'New Name',
    secteur = 2,
    expertise = 'New Expertise',
    droit_acces = 1
WHERE
    id = 1;
UPDATE personnel
SET 
    nom = 'New Name',
    prenom = 'New Firstname',
    id_role = 2,
    numero_adresse = 2,
    rue = 'New Street',
    ville = 'New City'
WHERE
    id = 1;
UPDATE recette
SET 
    date_recette = '2024-04-09',
    profit = 150.50,
    cout = 100.25,
    information = 'Updated information',
    id_machine_de_jeu = 2,
    rentable = 1
WHERE
    id = 1;
UPDATE type_panne
SET 
    nom = 'New Name',
    categorie = 'New Category'
WHERE
    id = 1;
UPDATE panne
SET 
    id_type_panne = 2,
    date_panne = '2024-04-09',
    id_personnel = 2
WHERE
    id = 1;
UPDATE fournisseur
SET 
    nom = 'New Name',
    ville = 'New City'
WHERE
    id = 1;
UPDATE pieces
SET 
    nom = 'New Name',
    date_service = '2024-04-09',
    etat = 'New State',
    id_fournisseur = 2,
    id_machine_jeu = 2,
    id_panne = 2
WHERE
    id = 1;
