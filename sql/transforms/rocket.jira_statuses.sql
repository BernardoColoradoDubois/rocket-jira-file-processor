drop table if exists rocket.jira_statuses; 
create table if not exists rocket.jira_statuses as 
select 
	status_id , 
	status_name  
from rocket.stg_jira_issues sji ;