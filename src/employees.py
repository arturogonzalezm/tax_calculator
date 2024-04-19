from src.strategies import DefaultTaxStrategy, FixedSuperStrategy
from src.utilities import calculate_medicare_levy
from src.config import tax_brackets, super_rate, gst_rate, expenses_percentage

tax_strategy = DefaultTaxStrategy(tax_brackets)
super_strategy = FixedSuperStrategy(super_rate)


def sole_trader(daily_rate):
    # daily_rate = 1000
    weekly_rate = daily_rate * 5 * 52
    income_tax = tax_strategy.calculate_tax(weekly_rate)
    superannuation = super_strategy.calculate_super(weekly_rate)
    medicare_levy = calculate_medicare_levy(weekly_rate)
    total_expenses = weekly_rate * expenses_percentage
    gst_collected = weekly_rate * gst_rate
    gst_credits = total_expenses * gst_rate
    net_gst_payable = gst_collected - gst_credits
    net_income_incl_super = weekly_rate - income_tax - superannuation - net_gst_payable - medicare_levy
    net_income_excl_super = weekly_rate - income_tax - net_gst_payable - medicare_levy

    return {
        "Category": ["Annual Income",
                     "Income Tax",
                     "Superannuation",
                     "Medicare Levy",
                     "Net GST Payable",
                     "Net Income incl. Super & GST",
                     "Net Income excl. Super & GST"],
        "Sole Trader": [f"${weekly_rate:.2f}",
                        f"${income_tax:.2f}",
                        f"${superannuation:.2f}",
                        f"${medicare_levy:.2f}",
                        f"${net_gst_payable:.2f}",
                        f"${net_income_incl_super:.2f}",
                        f"${net_income_excl_super:.2f}"]
    }


def permanent_employee(salary):
    # salary = 180000
    income_tax_employee = tax_strategy.calculate_tax(salary)
    superannuation_employee = super_strategy.calculate_super(salary)
    medicare_levy_employee = calculate_medicare_levy(salary)
    net_income_incl_super_employee = salary - income_tax_employee - medicare_levy_employee
    net_income_excl_super_employee = salary - income_tax_employee + superannuation_employee - medicare_levy_employee

    return {
        "Category": ["Annual Income",
                     "Income Tax",
                     "Superannuation",
                     "Medicare Levy",
                     "Net GST Payable",
                     "Net Income incl. Super & GST",
                     "Net Income excl. Super & GST"],
        "Permanent Employee": [f"${salary:.2f}",
                               f"${income_tax_employee:.2f}",
                               f"${superannuation_employee:.2f}",
                               f"${medicare_levy_employee:.2f}",
                               "N/A",
                               f"${net_income_incl_super_employee:.2f}",
                               f"${net_income_excl_super_employee:.2f}"]
    }
