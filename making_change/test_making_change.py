import unittest
from making_change import making_change


class Test(unittest.TestCase):
    def setUp(self):
        self.denominations = [1, 5, 10, 25, 50]

    def test_making_change_small_amount(self):
        self.assertEqual(making_change(0, self.denominations), 1)
        self.assertEqual(making_change(1, self.denominations), 1)
        self.assertEqual(making_change(5, self.denominations), 2)
        self.assertEqual(making_change(10, self.denominations), 4)
        self.assertEqual(making_change(20, self.denominations), 9)
        self.assertEqual(making_change(30, self.denominations), 18)
        self.assertEqual(making_change(100, self.denominations), 292)
        self.assertEqual(making_change(200, self.denominations), 2435)
        self.assertEqual(making_change(300, self.denominations), 9590)

    def test_making_change_large_amount(self):
        self.assertEqual(making_change(350, self.denominations), 16472)
        self.assertEqual(making_change(400, self.denominations), 26517)
        self.assertEqual(making_change(1000, self.denominations), 801451)
        self.assertEqual(making_change(2000, self.denominations), 11712101)
        self.assertEqual(making_change(5000, self.denominations), 432699251)
        self.assertEqual(making_change(10000, self.denominations), 6794128501)
        self.assertEqual(
            making_change(
                2000000400000000050000080000000080000000003000006600700000800400005000000000000,
                self.denominations,
            ),
            10666675200002557565310424122091798208471690598157086773176519187882327741954880466566394543266843399244373550575284157061033432727032009991201693742046702141328719199330198255767745485108434215714872597152450866008387719965502737920893612580042846991114736010914287225633517901740875439094366873763954294784,
        )


if __name__ == "__main__":
    unittest.main()
