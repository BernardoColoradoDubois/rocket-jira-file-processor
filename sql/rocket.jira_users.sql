CREATE TABLE jira_users (
    account_id TEXT PRIMARY KEY,
    account_type TEXT NOT NULL,
    display_name TEXT NOT NULL,
    email_address TEXT,
    avatar_url TEXT,
    active BOOLEAN
);