from typing import Protocol

from _decimal import Decimal

from good_design.domain.enums import Employment


class IPaymentCalculator(Protocol):
    def __call__(self, payment_rate: Decimal, worked_period: Decimal | None) -> Decimal:
        """
        This is an interface for payment calculation functions for different employment types.

        :param payment_rate: employee's payment rate according to the employment type
        :param worked_period: number of worked periods (hours, days, etc.) according to the employment type
        :return: calculated payment (salary) for the employee according to the employment type
        """
        pass


def calculate_payment_for_regular_employee(
    payment_rate: Decimal, worked_period: Decimal | None
) -> Decimal:
    return payment_rate


def calculate_payment_for_contractor_employee(
    payment_rate: Decimal, worked_period: Decimal | None
) -> Decimal:
    return payment_rate * worked_period


def calculate_payment_for_freelancer_employee(
    payment_rate: Decimal, worked_period: Decimal | None
) -> Decimal:
    return payment_rate * Decimal(0.9)


PaymentCalculatorsMap: dict[Employment, IPaymentCalculator] = {
    # this dict represents mapping between employment conditions and payment calculation methods
    Employment.REGULAR: calculate_payment_for_regular_employee,
    Employment.CONTRACTOR: calculate_payment_for_contractor_employee,
    Employment.FRELANCEER: calculate_payment_for_freelancer_employee
}
