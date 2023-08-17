from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A A A A B") == 210

    def test_wrong_input(self):
        assert checkout_solution.checkout("A A A A J B") == -1        