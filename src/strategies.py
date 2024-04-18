class TaxStrategy:
    def calculate_tax(self, income):
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


class SuperannuationStrategy:
    def calculate_super(self, income):
        raise NotImplementedError("You should implement this method!")


class FixedSuperStrategy(SuperannuationStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_super(self, income):
        return income * self.rate
