class LoanEligibility:

    def __init__(self, customer_name, salary, credit_score, employed):
        self.customer_name = customer_name
        self.salary = salary
        self.credit_score = credit_score
        self.employed = employed

    def check_eligibility(self):
        if (
            self.salary >= 50000
            and self.credit_score >= 700
            and self.employed
        ):
            return "Eligible for Loan"
        else:
            return "Not Eligible for Loan"


customer = LoanEligibility(
    "Priya Reddy",
    65000,
    750,
    True
)

print("Customer Name:", customer.customer_name)
print("Loan Status:", customer.check_eligibility())