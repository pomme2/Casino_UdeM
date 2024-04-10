go
create or alter procedure rechercheProfitInterval (@date1 date, @date2 date)
as
Begin
    select * from recette where date_recette between @date1 and @date2;
end;

go
create or alter procedure rechercheProfitDate (@date1 date)
as
Begin
    select * from recette where date_recette = @date1;
end;

go
create or alter procedure recherchePieceParPanne (@enPanne binary)
as
Begin
if @enPanne = 0
    select * from pieces where id_panne is null;
else
	select * from pieces where id_panne is not null;
end;

go
create or alter procedure NbrPieceParFournisseur
as
Begin
select f.id ,count(p.id) NbrPiece from pieces p join fournisseur f on p.id_fournisseur=f.id group by f.id
	;
end;

go
create or alter procedure PersonnelSpecifique(@id_role int)
as
Begin
select * from personnel p1 where id_role = @id_role
	;
end;

go
create or alter procedure listePanne
as
Begin
	select * from machine_de_jeu ma
	join (select pie.id_machine_jeu, pa.date_panne,per.nom, per.prenom, tp.nom NomPanne, tp.categorie from panne pa 
	join pieces pie on pie.id_panne = pa.id 
	join personnel per on per.id = pa.id_personnel
	join type_panne tp on tp.id = pa.id_type_panne)
	tmp on tmp.id_machine_jeu =ma.id
	;
end;

go
create or alter procedure listeProfitJeuParSecteur
as
Begin
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
end;

go
create or alter procedure listeProfitMachineParSecteur
as
Begin
	--profit machine
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

end;

go
create or alter procedure listeProfitMachineParPanne(@enPanne binary)
as
Begin

if @enPanne = 0
    --profit par machine
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
else
	--profit par machine
	select tmp.id ,SUM(r.profit) Profit_Total from recette r
	join (select ma.id, pie.id_panne, j.id JeuID from machine_de_jeu ma
	join (select * from pieces p where p.id_panne is null) pie 
	on pie.id_machine_jeu = ma.id
	join jeu j
	on j.id = ma.id_jeu) tmp
	on tmp.id = r.id_machine_de_jeu
	join panne pa
	on pa.id = tmp.id_panne
	group by tmp.id
	;

end;

go
create or alter procedure listeProfitJeuxParPanne(@enPanne binary)
as
Begin

if @enPanne = 0
	--profit par jeux
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
else
	--profit par jeux
	select r.id, r.date_recette, SUM(r.profit) AS Profit_Total from recette r
	join (select ma.id, pie.id_panne, j.id JeuID from machine_de_jeu ma
	join (select * from pieces p where p.id_panne is null) pie 
	on pie.id_machine_jeu = ma.id
	join jeu j
	on j.id = ma.id_jeu) tmp
	on tmp.id = r.id_machine_de_jeu
	join panne pa
	on pa.id = tmp.id_panne
	group by r.date_recette, r.id
	;

end;


DECLARE @profit DECIMAL(19, 4);
DECLARE @cout DECIMAL(19, 4);
DECLARE @real_profit DECIMAL(19, 4);

DECLARE real_profit_cursor CURSOR FOR
SELECT profit, cout
FROM recette;

OPEN real_profit_cursor
FETCH NEXT FROM real_profit_cursor INTO @profit, @cout;

WHILE @@FETCH_STATUS = 0
BEGIN
	SET @real_profit = @profit - @cout;

	FETCH NEXT FROM real_profit_cursor INTO @real_profit;
END

CLOSE real_profit_cursor;
DEALLOCATE real_profit_cursor;


CREATE FUNCTION dbo.GetAverageProfitPerGame
(
    @gameId INT,
    @startDate DATE,
    @endDate DATE
)
RETURNS DECIMAL(19, 4)
AS
BEGIN
    DECLARE @averageProfit DECIMAL(19, 4);

    SELECT @averageProfit = AVG(profit)
    FROM recette AS r
    INNER JOIN machine_de_jeu AS mdj ON r.id_machine_de_jeu = mdj.id
    WHERE mdj.id_jeu = @gameId AND
          r.date_recette BETWEEN @startDate AND @endDate;

    -- If there are no records, ensure we return 0 instead of NULL
    IF @averageProfit IS NULL
        SET @averageProfit = 0;

    RETURN @averageProfit;
END;
