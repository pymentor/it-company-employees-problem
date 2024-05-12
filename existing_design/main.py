class Employee:
    # this is a base class for all employees
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class RegularEmployee(Employee):
    # this is a base class for regular employees (who work full-time on a long-term basis and have a fixed salary)
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def calculate_payment(self):
        return self.salary


class RegularDeveloperEmployee(RegularEmployee):
    # this is a class for regular developers
    def __init__(self, name, email, salary, programming_language):
        super().__init__(name, email, salary)
        self.programming_language = programming_language
        self.tasks = []  # fifo queue

    def add_task(self, task):
        self.tasks.append(task)
        print(f"{self.name} accepted the task: {task}")

    def process_tasks(self):
        for task in self.tasks:
            print(f"{self.name} is writing code for task: {task}")

        self.tasks.clear()
        print(f"{self.name} completed all tasks")


class RegularManagerEmployee(RegularEmployee):
    # this is a class for regular managers
    def __init__(self, name, email, salary, team_name):
        super().__init__(name, email, salary)
        self.team_name = team_name
        self.developers = []
        self.team_tasks = []

    def add_task_to_team(self, task):
        self.team_tasks.append(task)
        print(f"Task: {task} is added to the team {self.team_name}")

    def add_developer_to_team(self, regular_developer):
        self.developers.append(regular_developer)
        print(f"{regular_developer.name} is added to the team {self.team_name}")

    def assign_tasks_to_developers(self):
        print(
            f"Team {self.team_name} is working on the following tasks: {self.team_tasks}"
        )
        for task, developer in zip(self.team_tasks, self.developers):
            developer.add_task(task)

    def start_sprint(self):
        print(f"Team {self.team_name} is starting a new sprint")
        for developer in self.developers:
            developer.process_tasks()

    def finish_sprint(self):
        print(f"Team {self.team_name} has finished the sprint")
        self.team_tasks.clear()


# TODO: add support for contractor employees (developers and managers) !!!
class ContractorEmployee(Employee):
    # this is a base class for contractor employees (who work part-time on a short-term basis and have an hourly rate)
    def __init__(self, name, email, hourly_rate):
        super().__init__(name, email)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate

if __name__ == "__main__":
    # create regular manager
    regular_manager = RegularManagerEmployee(
        "Alice Brown", "alice@brown.com", 2000, "Regular Team A"
    )

    # add tasks to team
    regular_manager.add_task_to_team("Task 1")
    regular_manager.add_task_to_team("Task 2")

    # create regular developers
    regular_developer_1 = RegularDeveloperEmployee(
        "John Doe", "john@doe.com", 1000, "Python"
    )
    regular_developer_2 = RegularDeveloperEmployee(
        "Mike Smith", "mike@smith.com", 1200, "JavaScript"
    )

    # add developers to team
    regular_manager.add_developer_to_team(regular_developer_1)
    regular_manager.add_developer_to_team(regular_developer_2)

    # assign tasks to developers
    regular_manager.assign_tasks_to_developers()

    # start a new sprint
    regular_manager.start_sprint()

    # finish the sprint once all the tasks are completed
    regular_manager.finish_sprint()

    # pay employees for their work
    print(f"{regular_manager.name} got payment: {regular_manager.calculate_payment()}")
    print(
        f"{regular_developer_1.name} got payment: {regular_developer_1.calculate_payment()}"
    )
    print(
        f"{regular_developer_2.name} got payment: {regular_developer_2.calculate_payment()}"
    )
