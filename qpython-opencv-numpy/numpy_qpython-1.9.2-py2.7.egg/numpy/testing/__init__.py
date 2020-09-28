# fake tester, android don't have unittest
class Tester(object):
    def test(self, *args, **kwargs):
        pass
    def bench(self, *args, **kwargs):
        pass
test = Tester().test
