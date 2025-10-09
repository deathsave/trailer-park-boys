from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestAttractMode(MpfMachineTestCase):

    def test_attract(self):

        self.assertModeRunning('attract')
