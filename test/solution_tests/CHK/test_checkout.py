from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AAAAAA") == 250

    def test_wrong_input(self):
        assert checkout_solution.checkout("AAAAJB") == -1

    def test_cross_promotion(self):
        assert checkout_solution.checkout("BBBEEEEE") == 230               