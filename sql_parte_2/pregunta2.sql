select department_id, department, hired_employess from (
select department_id, count(*) as hired_employess from (
select * from raw_hired_employees where department_id is not null and SPLIT_PART(datetime, '-', 1) = '2021'
) group by department_id) inner join raw_departments on raw_departments.id = department_id where hired_employess > (select avg(hired_employess) from (
select department_id, count(*) as hired_employess from (
select * from raw_hired_employees where department_id is not null and SPLIT_PART(datetime, '-', 1) = '2021'
) group by department_id));