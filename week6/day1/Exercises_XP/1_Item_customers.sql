create table items(
name varchar(100),
price int
);

insert into items( name,price)
                  values("Small Desk", 100),
                  ("Large Desk", 300),
                  ("Fan", 80),
                  ("Ball", 40),
                  ("Banana", 20);

create table customers(
    first_name varchar(100),
    last_name varchar(100)
);

insert into customers(first_name, last_name)
VALUES ("Greg", "Jones"),
("Sandra", "Jones"),
("Scott", "Scott"),
("Trevor", "Green"),
("John", "Smith"),
("Melanie", "Johnson");
-- # all the items
select * from items;
-- # All the items with a price above 80 (80 not included).
select * from items where price < 80;
-- # All the items with a price below 300. (300 included)
select * from items where price < 300;
-- # All customers whose last name is ‘Smith’ (What will be your outcome?).
select * from customers where last_name="Smith" ;
-- # All customers whose last name is ‘Jones’.
select * from customers where last_name="Jones" ;
-- # All customers whose firstname is not ‘Scott’.
select * from customers where first_name not in ("Scott");
-- select * from customers where first_name <>"Scott";