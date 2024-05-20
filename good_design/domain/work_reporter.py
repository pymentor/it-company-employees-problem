from collections import defaultdict
from dataclasses import dataclass, field

from _decimal import Decimal

from good_design.domain.employees.abstract import Employee


@dataclass
class WorkReporter:
    """
    This class represents reports receiver that's responsible for receiving work reports from managers.
    Work report contains reference to an employee and its worked periods number.
    """

    reports: defaultdict[Employee, Decimal] = field(
        default_factory=lambda: defaultdict(Decimal)
    )

    def add_employee_work_report(
        self, employee: Employee, worked_period: Decimal
    ) -> None:
        """
        This method adds a work report for the employee

        :param employee: employee to add work report
        :param worked_period: worked period to add
        :return: None
        """
        self.reports[employee] += worked_period

    def reset_employee_work_report(self, employee: Employee) -> None:
        """
        This method resets the work report for the employee

        :param employee: employee to reset work report
        :return: None
        """
        self.reports[employee] = Decimal(0)
