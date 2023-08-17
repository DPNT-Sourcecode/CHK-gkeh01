from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("HHHHHHHHHHHH") == 100


    def test_wrong_input(self):
        assert checkout_solution.checkout("AAAA8B") == -1

    def test_cross_promotion(self):
        assert checkout_solution.checkout("BBBEEEEE") == 230
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BEBEEE") == 160        

    def test_free_items(self):
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFFFFFF") == 70

    def test_bundle_promotions(self):
        assert checkout_solution.checkout("XSTYZXSTYZZZ") == 132                          