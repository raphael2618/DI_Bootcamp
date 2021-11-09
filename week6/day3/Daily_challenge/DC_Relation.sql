drop table customer;
 create table customer(
    id_customer int not null primary key ,
    first_name varchar(100) null,
    last_name  varchar(100) null
);

insert into customer (id_customer,first_name, last_name) values (1,'Greg','Jones'),
(2,'Sandra','Jones'),
(3,'Scott','Scott'),
(4,'Trevor','Green');

create table customer_profile(
    customer_profile_id int not null primary key,
    id_customer_fk int not null,
    address varchar(100),
    foreign key (id_customer_fk) references customer(id_customer)
);

insert into customer_profile (customer_profile_id,address,id_customer_fk)
values ('1','dafna 26,tlv',1),
('2','dafna 32,tlv',2),
('3','dafna 40,tlv',3);

select * from customer
inner join customer_profile
on customer.id_customer = customer_profile.id_customer_fk;

create table product(
    product_id int not null primary key ,
    name varchar(100),
    price int
);

create table order(
    fk_customer int not null references customer(id_customer),
    fk_product int not null references product(product_id)
);

SELECT *
FROM order
LEFT OUTER JOIN customer
  ON customer.id_customer  =order.fk_customer
LEFT OUTER JOIN product
  ON product.product_id = order.fk_product;

SELECT *
FROM order
INNER JOIN customer
  ON customer.id_customer  =order.fk_customer
INNER JOIN product
  ON product.product_id = order.fk_product;

SELECT *
FROM order
FULL JOIN customer
  ON customer.id_customer  =order.fk_customer
FULL JOIN product
  ON product.product_id = order.fk_product;

SELECT *
FROM order
RIGHT JOIN customer
  ON customer.id_customer  =order.fk_customer
RIGHT JOIN product
  ON product.product_id = order.fk_product;