-- DVD RENTAL 1
-- Get a list of all film languages.
select name from language;
-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
select title, description,name from language,film where film.language_id = language.language_id;
-- Get all films, even if they don’t have languages.
select title, description,name from language left join film on film.language_id = language.language_id;
-- Get all languages, even if there are no films in those languages.
select title, description,name from film left join language on film.language_id = language.language_id;

create table new_film (
    id  serial primary key,
    name varchar(100)
);

insert into new_film (name) values ('Harry Potter 1'),
                                    ('Harry Potter 2'),
                                    ('Harry Potter 3');


create table customer_review(
    review_id serial primary key not null,
    film_id int references new_film(id) on delete restrict,
    language_id int references language(language_id),
    title varchar(100),
    score int check ( score between 1 and 10 ),
    review_text varchar,
    last_update date
);

insert into customer_review values (
                                    5,1,1,'verita',5,'very very bad movie !','2020-10-20'
                                   ),
                                   (2,2,4,'santa',5,'very very good movie !','2020-10-01');

delete * from customer_review;
-- it cause an error because of the restriction that we made before.

-- DVD RENTAL 2
update language SET name = 'EN' where name='English' ;
update language SET name = 'FR' where name='French' ;
select name from language;

-- the foreign key in the customer table are address.
-- when i made an insert i have to check that the address id is in
-- the address table before insert element.
-- otherwise it will put an error.

-- to delete the customer_review table, we have to check all the
-- film in the new_film table that have a review.Then we can delete the review table.

select * from rental where return_date not in (select return_date from rental);

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select title from film,film_actor,actor where  film.film_id = film_actor.film_id
and film_actor.film_id = film.film_id
and description like '%sumo wrestler%' ;
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title from category,film_category,film where name='Documentary'
and length <60
and rating='R'
and category.category_id = film_category.category_id
and film.film_id = film_category.film_id;

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
-- and he returned it between the 28th of July and the 1st of August, 2005.

select last_name from customer,payment,rental
where last_name='Matthew' and last_name='Mahan'
and amount='4.00'
and return_date between '2005-07-28' and '2005-08-28'
and rental.customer_id = customer.customer_id
and payment.rental_id = rental.rental_id;


-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat”
-- in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT max(replacement_cost)  from film,customer
where first_name='Matthew' and last_name='Mahan'            ---NOT FINISHED
and description like '%boat%' or title like '%boat%'
and customer.customer_id