from _decimal import Decimal
from dataclasses import dataclass

from domain.employees.abstract import Employee
from domain.payment import IPaymentCalculator, PaymentCalculatorsMap
from domain.work_reporter import WorkReporter


@dataclass
class Accountant(Employee):
    """
    This class represents an accountant that's responsible for calculating payments for employees.
    """

    # init
    work_reporter: WorkReporter

    def __hash__(self) -> int:
        return id(self)

    @staticmethod
    def _calculate_payment(employee: Employee, worked_period: Decimal | None) -> Decimal:
        """
        This method calculates payment for the employee based on the worked period and the payment rate.

        :param employee: employee to calculate payment for
        :param worked_period: number of worked periods (hours, days, etc.) according to the employment type
        :return: None
        """
        # get the payment calculator according to the employee's employment type
        payment_calculator: IPaymentCalculator | None = PaymentCalculatorsMap.get(
            employee.employment
        )

        # if the payment calculator is not found, raise an error
        if payment_calculator is None:
            raise ValueError(
                f"Payment calculator for employment type {employee.employment} is not found"
            )

        # calculate the payment for the employee
        return payment_calculator(employee.payment_rate, worked_period)

    def do(self) -> None:
        """
        This method emulates the accountant's work on calculating payments for employees.

        :return: None
        """
        print(f"Accountant {self} is starting to work")

        # report worked periods for itself
        self.work_reporter.add_employee_work_report(self, Decimal(1))

        # iterate over all employees and their worked periods in order to calculate payments
        for employee, worked_period in self.work_reporter.reports.items():
            # calculate payment for the employee
            print(f"Calculating payment for {employee}")
            payment: Decimal = self._calculate_payment(employee, worked_period)
            print(f"Payment for {employee} has been calculated: {payment}")

            # reset the work report for the current employee in order to start a new payment period
            self.work_reporter.reset_employee_work_report(employee)
            print(f"Work report for {employee} has been reset")

        print(f"Accountant {self} is finished working")
