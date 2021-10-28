
-- All items, ordered by price (lowest to highest).
select * from items.items order by price;
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items.items where price<80 order by price desc;

-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
select  first_name,last_name from items.customers order by first_name,last_name limit 3;
-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name from items.customers order by last_name desc;

-- Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table:
create table purchases (

    item_id int, foreign key (item) references items,
    customers_id int primary key ,foreign key(customers) references customer(id)
)
