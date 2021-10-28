CREATE TABLE FirstTab (
     id integer,
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;

--
 SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- we want count how many id from second table are null that are not in the first table = 0

SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- they want all the id that are not equal to 5 in the frist tab. there are 2 : 6 and 7.

 SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- it will return 0 because there is no id that is not in secondtab but in firsttable.

 SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- we caount all the id that not equal to the id not null in the second table means not equal to 5.
-- it count 2 : 6 and 7.