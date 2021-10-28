create database bootcamp;
use bootcamp;

create table students(
id int(5) primary key AUTO_INCREMENT,
last_name varchar(100),
first_name varchar(100),
birth_date date
);

insert into students(
values (last_name,first_name,birth_date)
('Marc',	'Benichou',	'02/11/1998'),
('Cohen',	'Yoan',	'03/12/2010'),
('Lea',	'Benichou',	'27/07/1987'),
('Amelia',	'Dux',	'07/04/1996') ,
('David',	'Grez',	'14/06/2003') ,
('Omer',	'Simpson',	'03/10/1980')
);

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
select * from students where SUBSTR(last_name, 2, 1) = 'a';
-- Fetch the students whose id’s are equal to 1 AND 3 .
select * from students where id=1 or id=3;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students where date_birth>='1/01/2000';

