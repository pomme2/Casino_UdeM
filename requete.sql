--profit par interval de date
select * from recette where date_recette between '2023-01-01' and '2023-04-09';
--profit avec date exact
select * from recette where date_recette = '2023-04-01';
--liste de machine en panne
select * from pieces where id_panne is not null;
--liste de machine pas en panne
select * from pieces where id_panne is null;
--liste des autres machines
select * from distributeur_de_jeton;
select * from panneau_affichage;
select * from camera_surveillance;
select * from outils_de_communication;
select * from system_eclairage;
select * from systeme_sonorisation;
--liste de nbr piece (par fournisseur)
select f.id ,count(p.id) NbrPiece from pieces p join fournisseur f on p.id_fournisseur=f.id group by f.id;
--liste du personnel par role
select * from personnel p1 where id_role =1;
--liste de panne avec tous info
select * from machine_de_jeu ma
join (select pie.id_machine_jeu, pa.date_panne,per.nom, per.prenom, tp.nom NomPanne, tp.categorie from panne pa 
join pieces pie on pie.id_panne = pa.id 
join personnel per on per.id = pa.id_personnel
join type_panne tp on tp.id = pa.id_type_panne)
tmp on tmp.id_machine_jeu =ma.id
;
--liste des profits de chaucun des jeux par secteur
select rp.secteur, tmp2.id_jeu, sum(tmp2.profit) ProfitParSecteur from role_personnel rp
join personnel per 
on per.id_role =rp.id
join(select pa.id_personnel, pie.id_machine_jeu from panne pa
join pieces pie
on pie.id_panne = pa.id) tmp1
on tmp1.id_personnel = per.id
join (select ma.id, ma.id_jeu, j.nom, r.profit from machine_de_jeu ma
join recette r
on r.id_machine_de_jeu = ma.id
join jeu j
on j.id = ma.id_jeu) tmp2
on tmp2.id = tmp1.id_machine_jeu
group by rp.secteur, tmp2.id_jeu
;
--liste des profits chacune des machine par secteur
select rp.secteur, tmp2.id, sum(tmp2.profit) ProfitParSecteur from role_personnel rp
join personnel per 
on per.id_role =rp.id
join(select pa.id_personnel, pie.id_machine_jeu from panne pa
join pieces pie
on pie.id_panne = pa.id) tmp1
on tmp1.id_personnel = per.id
join (select ma.id, ma.id_jeu, j.nom, r.profit from machine_de_jeu ma
join recette r
on r.id_machine_de_jeu = ma.id
join jeu j
on j.id = ma.id_jeu) tmp2
on tmp2.id = tmp1.id_machine_jeu
group by rp.secteur, tmp2.id
;
--Lister le profit des machine pendant les jours de panne. On veut également savoir le jeu associer

select tmp.id ,SUM(r.profit) Profit_Total from recette r
join (select ma.id, pie.id_panne, j.id JeuID from machine_de_jeu ma
join (select * from pieces p where p.id_panne is not null) pie 
on pie.id_machine_jeu = ma.id
join jeu j
on j.id = ma.id_jeu) tmp
on tmp.id = r.id_machine_de_jeu
join panne pa
on pa.id = tmp.id_panne
group by tmp.id
;
--Lister le profit des jeux pendant les jours de panne. On veut également savoir le jeu associer
select r.id, r.date_recette, SUM(r.profit) AS Profit_Total from recette r
join (select ma.id, pie.id_panne, j.id JeuID from machine_de_jeu ma
join (select * from pieces p where p.id_panne is not null) pie 
on pie.id_machine_jeu = ma.id
join jeu j
on j.id = ma.id_jeu) tmp
on tmp.id = r.id_machine_de_jeu
join panne pa
on pa.id = tmp.id_panne
group by r.date_recette, r.id
;
