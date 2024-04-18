import pandas as pd


class TaxStrategy:
    def calculate_tax(self, income):
        raise NotImplementedError("You should implement this method!")


class SuperannuationStrategy:
    def calculate_super(self, income):
        raise NotImplementedError("You should implement this method!")


class DefaultTaxStrategy(TaxStrategy):
    def __init__(self, brackets):
        self.brackets = brackets

    def calculate_tax(self, income):
        tax_paid = 0
        for bracket in self.brackets:
            if income > bracket[1]:
                tax_paid += (bracket[1] - bracket[0]) * bracket[2]
            else:
                tax_paid += (income - bracket[0]) * bracket[2]
                break
        return tax_paid


class FixedSuperStrategy(SuperannuationStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_super(self, income):
        return income * self.rate


def calculate_medicare_levy(income):
    medicare_levy_rate = 0.02
    return income * medicare_levy_rate


# Tax brackets and superannuation rates
tax_brackets = [
    (0, 18200, 0), (18201, 45000, 0.19), (45001, 120000, 0.325),
    (120001, 180000, 0.37), (180001, float('inf'), 0.45)
]
super_rate = 0.11

# Instantiate strategies
tax_strategy = DefaultTaxStrategy(tax_brackets)
super_strategy = FixedSuperStrategy(super_rate)

# GST related constants
gst_rate = 0.10
expenses_percentage = 0.30  # Assuming 30% of the income is spent on expenses


def sole_trader():
    daily_rate = 1000
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
        "Category": ["Annual Income", "Income Tax", "Superannuation", "Medicare Levy", "Net GST Payable",
                     "Net Income incl. Super & GST",
                     "Net Income excl. Super & GST"],
        "Sole Trader": [f"${weekly_rate:.2f}", f"${income_tax:.2f}", f"${superannuation:.2f}", f"${medicare_levy:.2f}",
                        f"${net_gst_payable:.2f}", f"${net_income_incl_super:.2f}", f"${net_income_excl_super:.2f}"]
    }


def permanent_employee():
    salary = 180000
    income_tax_employee = tax_strategy.calculate_tax(salary)
    superannuation_employee = super_strategy.calculate_super(salary)
    medicare_levy_employee = calculate_medicare_levy(salary)
    net_income_incl_super_employee = salary - income_tax_employee - medicare_levy_employee
    net_income_excl_super_employee = salary - income_tax_employee + superannuation_employee - medicare_levy_employee

    return {
        "Category": ["Annual Income", "Income Tax", "Superannuation", "Medicare Levy", "Net GST Payable",
                     "Net Income incl. Super & GST",
                     "Net Income excl. Super & GST"],
        "Permanent Employee": [f"${salary:.2f}", f"${income_tax_employee:.2f}", f"${superannuation_employee:.2f}",
                               f"${medicare_levy_employee:.2f}",
                               "N/A", f"${net_income_incl_super_employee:.2f}",
                               f"${net_income_excl_super_employee:.2f}"]
    }


def main():
    sole_trader_data = sole_trader()
    permanent_employee_data = permanent_employee()

    comparison_data = {
        "Category": ["Annual Income", "Income Tax", "Superannuation", "Medicare Levy", "Net GST Payable",
                     "Net Income incl. Super & GST",
                     "Net Income excl. Super & GST"],
        "Sole Trader": sole_trader_data["Sole Trader"],
        "Permanent Employee": permanent_employee_data["Permanent Employee"]
    }

    df = pd.DataFrame(comparison_data)
    print(df)


if __name__ == "__main__":
    main()
