DROP TABLE IF EXISTS rocket.jira_issues;
CREATE TABLE IF NOT EXISTS rocket.jira_issues SELECT 
	issue_id, 
	issue_key, 
	project_id, 
	project_key, 
	creator_account_id, 
	assignee_account_id, 
	reporter_account_id, 
	summary, 
	description, 
	priority_id, 
	status_id, 
	time_estimate, 
	duedate, 
	resolution_date, 
	created_date, 
	updated_date
FROM rocket.stg_jira_issues;
