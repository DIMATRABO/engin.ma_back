import unittest

# Import your test cases
from test.entities.testWalletBalanceEntity import TestWalletBlanceEntity
from test.entities.testWalletEntities import TestWalletEntity
from test.use_cases.wallet.testSave import TestSave as TestSaveWallet
from test.gateways.variable.testVariableRepository import TestVariableRepository
# Create a test suite and add your test cases
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestWalletBlanceEntity))
    test_suite.addTest(unittest.makeSuite(TestWalletEntity))
    #test_suite.addTest(unittest.makeSuite(TestSaveWallet))
    test_suite.addTest(unittest.makeSuite(TestVariableRepository)) 
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

