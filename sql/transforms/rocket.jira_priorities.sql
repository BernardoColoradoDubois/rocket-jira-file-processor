drop table if exists rocket.jira_priorities;
create table if not exists rocket.jira_priorities as 
select 
	priority_id, 
	priority_name 
from rocket.stg_jira_issues sji ;