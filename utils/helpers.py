# Utility functions for WorkflowForge

def validate_task_name(task_name):
    if not isinstance(task_name, str):
        return False

    if task_name.strip() == "":
        return False

    return True