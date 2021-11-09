select count(rating) from film;
select rating from film where rating='PG-13' or rating='G';
select title from film where length>2 and rental_rate<3000;
select * from customer;
update customer
set first_name='Raphael',last_name='Boussidan'
where first_name='Carolyn';
delete from customer