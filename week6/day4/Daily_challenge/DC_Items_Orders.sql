create table orders(
order_id int(6),
name varchar(100)
);

insert into orders(order_id, name)
values(1,'chair'),
(2,'phone');

create table itemsDC(
items_id int(6),
unit_price int(5),
qte int(5),
order_id int(6),
foreign key (order_id)  references orders(order_id)
);

insert into itemsDC(items_id, unit_price, qte, order_id)
values(1,20,1,1),
       (2,100,2,2);
select unit_price,qte
from itemsDC,orders
where orders.order_id = itemsDC.order_id;

create function items.price_item(
@price int,
@qte int)
    returns int(50) as begin
        declare @total int(6)
        @total = @price * @qte
)

CREATE or REPLACE FUNCTION price_item(price varchar(50), qte varchar(100))
RETURNS price AS $total$
BEGIN
   RETURN(select unit_price,qte
from itemsDC,orders
where orders.order_id = itemsDC.order_id;);
END;
$price$

create table user(
user_id int(6),
nama int(5),
qte int(5),
order_id int(6),
foreign key (order_id)  references orders(order_id)
);




