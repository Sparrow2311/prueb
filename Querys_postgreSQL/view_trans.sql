CREATE VIEW view_trans AS
select c2.company_name , c.created_at,  sum(amount)  as monto_total  from charges c 
join  companies c2 on c2.id = c.id 
group by c2.company_name ,c.created_at; 

select * from view_trans