# Tax brackets and superannuation rates
tax_brackets = [
    (0, 18200, 0), (18201, 45000, 0.19), (45001, 120000, 0.325),
    (120001, 180000, 0.37), (180001, float('inf'), 0.45)
]
super_rate = 0.11
gst_rate = 0.10
expenses_percentage = 0.30  # Assuming 30% of the income is spent on expenses
