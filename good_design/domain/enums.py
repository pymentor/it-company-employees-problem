from enum import Enum


class Role(Enum):
    """
    This class represents roles an employee can have in a company.
    """

    DEVELOPER: str = "developer"
    MANAGER: str = "manager"
    ACCOUNTANT: str = "accountant"
    QA: str = "qa"


class Employment(Enum):
    """
    This class represents employment conditions (contract details) for an employee.
    """

    # regular employment type stands for a full-time employee with a fixed salary per month
    REGULAR: str = "regular"
    CONTRACTOR: str = "contractor"
    FRELANCEER: str = "freelancer"



class ProgrammingLanguage(Enum):
    """
    This class represents programming languages that developers can learn and use for their tasks.
    """

    PYTHON: str = "python"
    JAVASCRIPT: str = "javascript"
    CPP: str = "cpp"


class TaskStatus(Enum):
    """
    This class represents statuses of a developer task.
    """

    NEW: str = "new"
    DEV_IN_PROGRESS: str = "dev_in_progress"
    DONE: str = "done"
    INTEGRATED: str = "integrated"
