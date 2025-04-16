select department, job, sum(Q1) as Q1, sum(Q2) as Q2, sum(Q3) as Q3, sum(Q4) as Q4 
from 
(
select
raw_departments.department as department,
raw_jobs.job as job,
case 
when SPLIT_PART(datetime, '-', 1) = '2021' and SPLIT_PART(datetime, '-', 2) between '01' and '03' then 1
else 0
end as Q1,
case 
when SPLIT_PART(datetime, '-', 1) = '2021' and SPLIT_PART(datetime, '-', 2) between '04' and '06' then 1
else 0
end as Q2,
case 
when SPLIT_PART(datetime, '-', 1) = '2021' and SPLIT_PART(datetime, '-', 2) between '07' and '09' then 1
else 0
end as Q3,
case 
when SPLIT_PART(datetime, '-', 1) = '2021' and SPLIT_PART(datetime, '-', 2) between '10' and '12' then 1
else 0
end as Q4
from raw_hired_employees 
inner join raw_departments on raw_hired_employees.department_id = raw_departments.id 
inner join raw_jobs on raw_hired_employees.job_id = raw_jobs.id)
group by department, job order by department ASC, job ASC;