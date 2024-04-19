import pandas as pd

from src.employees import sole_trader, permanent_employee


def main(daily_rate, salary):
    sole_trader_data = sole_trader(daily_rate)
    permanent_employee_data = permanent_employee(salary)

    comparison_data = {
        "Category": ["Annual Income", "Income Tax", "Superannuation", "Medicare Levy", "Net GST Payable",
                     "Net Income incl. Super & GST", "Net Income excl. Super & GST"],
        "Sole Trader": sole_trader_data["Sole Trader"],
        "Permanent Employee": permanent_employee_data["Permanent Employee"]
    }

    df = pd.DataFrame(comparison_data)
    return df.to_string(index=False)


if __name__ == "__main__":
    print(main(1000, 180000))
