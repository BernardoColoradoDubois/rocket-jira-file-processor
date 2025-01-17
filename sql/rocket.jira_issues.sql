DROP TABLE IF EXISTS rocket.jira_issues;
CREATE TABLE jira_issues ( 
    issue_id TEXT PRIMARY KEY, 
    issue_key TEXT NOT NULL, 
    project_key TEXT NOT NULL, 
    created_date TIMESTAMP WITH TIME ZONE, 
    updated_date TIMESTAMP WITH TIME ZONE, 
    summary TEXT, 
    description TEXT, 
    assignee_account_id TEXT, 
    assignee_display_name TEXT, 
    status_name TEXT, 
    priority_name TEXT, 
    reporter_account_id TEXT, 
    reporter_display_name TEXT, 
    creator_account_id TEXT, 
    creator_display_name TEXT 
);