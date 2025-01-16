DROP TABLE IF EXISTS rocket.jira_projects;
CREATE TABLE rocket.jira_projects (
    project_id TEXT PRIMARY KEY,
    project_key TEXT NOT NULL,
    project_name TEXT NOT NULL,
    project_type_key TEXT,
    project_category_id TEXT,
    project_category_name TEXT,
    lead_account_id TEXT,
    lead_display_name TEXT,
    is_private BOOLEAN,
    simplified BOOLEAN
);