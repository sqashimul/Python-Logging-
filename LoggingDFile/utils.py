import softest

class Utils(softest.TestCase):
    for stop in list:
        print("The text is: " + stop.text)
        self.soft_assert(self.assertEqual, stop.text, value)
        if stop.text == value:
            print("test passed")
        else:
            print("test failed")
    self.assert_all()