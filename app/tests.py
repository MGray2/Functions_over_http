from django.test import SimpleTestCase

# I had to add '{}, True' to resolve an issue regarding the test cases.


class TestHeyYou(SimpleTestCase):
    def test_hey_nate(self):
        response = self.client.get("/hey/nate", {}, True)
        self.assertContains(response, "Hey, nate!")

    def test_hey_bcca(self):
        response = self.client.get("/hey/BCCA", {}, True)
        self.assertContains(response, "Hey, BCCA!")


class TestAgeIn(SimpleTestCase):
    def test_age_in_2050_born_2000(self):
        response = self.client.get("/age-in/2050/2000", {}, True)
        self.assertContains(response, "50")

    def test_age_in_2050_born_0(self):
        response = self.client.get("/age-in/2050/0", {}, True)
        self.assertContains(response, "2050")

    def test_age_in_2010_born_1995(self):
        response = self.client.get("/age-in/2010/1995", {}, True)
        self.assertContains(response, "15")

    def test_age_in_1950_born_1920(self):
        response = self.client.get("/age-in/1950/120", {}, True)
        self.assertContains(response, "30")


class TestOrderTotal(SimpleTestCase):
    def test_order_total_0_0_0(self):
        response = self.client.get("/order-total/0/0/0", {}, True)
        self.assertContains(response, "0.0")

    def test_order_total_1_1_1(self):
        response = self.client.get("/order-total/1/1/1", {}, True)
        self.assertContains(response, "7.0")

    def test_order_total_2_3_4(self):
        response = self.client.get("/order-total/2/3/4", {}, True)
        self.assertContains(response, "17.5")

    def test_order_total_4_3_2(self):
        response = self.client.get("/order-total/4/3/2", {}, True)
        self.assertContains(response, "24.5")
