create database bootcamp;
use bootcamp;

create table students(
id int(5) primary key AUTO_INCREMENT,
last_name varchar(100),
first_name varchar(100),
birth_date date
);


insert into students(last_name,first_name,birth_date)
values
('Marc',	'Benichou',	'2010-10-02'),
('Cohen',	'Yoan',	'2010-12-03'),
('Lea',	'Benichou',	'1987-07-27'),
('Amelia',	'Dux',	'1996-04-07') ,
('David',	'Grez',	'2003-06-14') ,
('Aurelie',	'Laura',	'2003-06-13') ,
('Omer',	'Simpson',	'1980-10-03');

-- Fetch all of the data from the table.
select * from students;

-- Fetch all of the students first_names and last_names.
select first_name,last_name from students;

-- For the following questions, only fetch the first_names and last_names of the students.
select first_name,last_name from students;
-- Fetch the student which id is equal to 2.
select first_name,last_name from students where id=2;
-- Fetch the student whose last_name is Benichou AND first_name is Marc.
select * from students where last_name="Benichou" and first_name="Marc";

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
select * from students where last_name="Benichou" or first_name="Marc";
-- Fetch the students whose first_names contain the letter a.
select * from students where first_name like "%a%";
-- Fetch the students whose first_names start with the letter a.
select * from students where first_name like 'a%';
-- Fetch the students whose first_names end with the letter a.
select * from students where first_name like '%a';
-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select * from students where first_name like '%a_';
select first_name from students where first_name like '%a-';
-- Fetch the students whose id’s are equal to 1 AND 3 .
select * from students where id=1 or id=3;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students where birth_date>='2000-01-01';

insert into students(id, last_name, first_name, birth_date)
values (29,'joan','marc','2021-01-21')
