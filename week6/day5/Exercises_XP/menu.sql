create table menu_item(
   item_id smallint not null,
   price int not null,
   name_item varchar(100) not null
);

insert into menu_item(item_id, price, name_item) VALUES
(1,20,'raviolli'),
(2,10,'peperroni pinapple'),
(3,30,'shawarma'),
(4,50,'parguit');

select * from menu_item;