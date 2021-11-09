-- # Write a query to display the names (first_name, last_name)
-- # using an alias name “First Name”, “Last Name”
-- # from the employee table
select first_name as "First Name",last_name as "Last Name"  from employees;
-- Write a query to get unique departments ID
-- from the employee table (ie. without duplicates).
select distinct department_id from employees order by department_id;
-- Write a query to get the details of all employees
-- from the employee table, do so in descending order by first name.
select * from employees order by first_name desc;
-- Write a query to get the names (first_name, last_name),
-- salary and 15% of salary as PF (ie. alias) for all the employees.
select concat(first_name,', ',last_name) as names, salary,
       0.15*salary as PF from employees;
-- Write a query to get the employee IDs,
-- names (first_name, last_name)
-- and salary in ascending order according to their salary.
select employee_id, concat(first_name,', ',last_name) as names, salary
from employees order by salary;
-- Write a query to get the total sum of all salaries paid
-- to the employees.
select sum(salary) as "sum of salary" from employees;
-- Write a query to get the maximum and minimum
-- salaries paid to the employees.
select min(salary) as "Min salary", max(salary) as "Max salary" from employees;
-- Write a query to get the average salary paid to the employees.
select avg(salary) as Average from employees;
-- Write a query to get the number
-- of employees working in the company.
select count(employee_id) from employees;
-- Write a query to get all the
-- first names from the employees table in upper case.
select upper(first_name) from employees;
-- Write a query to get the first three characters
-- of each first name of all the employees in the employees table.
select upper(substr(first_name,1,3))  from employees;
-- Write a query to get the full names of all the employees
-- in the employees table. You have to include the first name and last name.
select concat(first_name,', ',last_name) as names from employees;
-- Write a query to get the first name, last name and the length
-- of the full name of all the employees from the employees table.
select concat(first_name,', ',last_name) as names,length(first_name)+length(last_name) as fullname from employees;
-- Write a query to check whether the first_name column of the employees
-- table contains any numbers.
select first_name from employees where first_name like '%[0-9]%';
-- Write a query to select the first ten records from a table.
select * from employees limit 10;
-- Restricting And Sorting

-- Write a query to display the first_name, last_name and salary of all employees
-- whose salary is between $10,000 and $15,000.
select first_name,last_name,salary from employees where salary between 10000 and 15000;
-- Write a query to display the first_name, last_name
-- and hire date of all employees who were hired in 1987.
select first_name,last_name,hire_date from employees
where extract(year from employees.hire_date) = 1987;

-- Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’.
select first_name,last_name from employees where first_name like '%c%' or first_name like '%e%';
-- Write a query to display the last_name, job,
-- and salary of all the employees who don’t work as Programmers
-- or Shipping Clerks, and who don’t receive a salary equal to $4,500, $10,000, or $15,000.
select last_name,job_title,salary
from employees,jobs where jobs.job_id = employees.job_id
and job_title<>'Programmer' or job_title<>'Shipping Clerk'
and salary =4500 or salary = 10000 or salary = 15000;
-- NOT SUR
-- Write a query to display the last names of all employees whose last name
-- contains exactly six characters.
select last_name from employees where length(last_name)=6;
-- Write a query to display the last name of all employees who have
-- the letter ‘e’ as the third character in the name.
select last_name from employees where substr(last_name,3,1) ='e';
-- SUBSTRING ( expression ,start , length )
-- Write a query to display the jobs/designations available in the employees table.
select job_title as "Job available" from jobs where job_id in (
select job_id
from employees);

-- Write a query to select all information of employees whose last name is
-- either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.


-- select * from employees
-- where last_name in ('SCOTT','BLAKE','JONES','KING','FORD');
select * from employees where last_name = 'SCOTT'
                           or last_name='BLAKE'
                           or last_name='JONES'
                            or last_name='KING'
                            or last_name='FORD';


