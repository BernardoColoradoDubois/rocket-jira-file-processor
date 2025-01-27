DROP TABLE IF EXISTS rocket.jira_issues;
CREATE TABLE rocket.jira_issues ( 
    --tarea
    issue_id INT PRIMARY KEY, 
    issue_key TEXT NOT NULL, 
    -- proyecto
    project_id INT NOT NULL,
    project_key TEXT NOT NULL, 
    
    --usuario que crea la tarea
    creator_account_id TEXT, 
    creator_display_name TEXT,

    -- usuario asignado
    assignee_account_id TEXT, 
    assignee_display_name TEXT, 

    -- usuario que reporta
    reporter_account_id TEXT, 
    reporter_display_name TEXT, 

    -- textos
    summary TEXT, 
    description TEXT, 
    -- prioridad
    priority_id INT, 
    priority_name TEXT,

    --tiempos
    time_estimate INT,
    due_date TIMESTAMP WITH TIME ZONE,
    resolution_date TIMESTAMP WITH TIME ZONE,

    -- estado
    status_id INT,
    status_name TEXT, 
    -- marcas de tiempo
    created_date TIMESTAMP WITH TIME ZONE, 
    updated_date TIMESTAMP WITH TIME ZONE 
);