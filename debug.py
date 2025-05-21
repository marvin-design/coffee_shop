import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover('tests' , pattern='*_test.py')
    runner = unittest.TextTestResult(verbosity=2)
    runner.run(suite)