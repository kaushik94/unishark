import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(cur_dir, os.pardir))
import unishark
import unittest
import logging
from time import sleep

log = logging.getLogger(__name__)


class MyTestClass1(unittest.TestCase):
    @unishark.data_driven(*[{'user_id': 1, 'passwd': 'abc'}, {'user_id': 2, 'passwd': 'def'}])
    def repeat_part(self, **param):
        sleep(1)
        log.info('user_id: %d, passwd: %s' % (param['user_id'], param['passwd']))

    def test_1(self):
        """Here is test_1's doc str"""
        log.info('This is an example of data_driven decorator')
        self.repeat_part()

    @unishark.data_driven(user_id=[1, 2, 3, 4], passwd=['a', 'b', 'c', 'd'])
    def test_2(self, **param):
        """Here is test_2's doc str"""
        log.info('Another example of data_driven decorator')
        sleep(1)
        log.info('user_id: %d, passwd: %s' % (param['user_id'], param['passwd']))


class MyTestClass2(unittest.TestCase):
    @unittest.skip('Here is the reason of skipping test_3')
    def test_3(self):
        """Here is test_3's doc str"""
        log.info('Here is logging of test_3')
        sleep(2)
        self.assertEqual(1, 2)

    def test_4(self):
        """Here is test_4's doc str"""
        log.info('Here is logging of test_4')
        sleep(2)
        log.info('Try escape: <div>')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    reporter = unishark.HtmlReporter(dest='log')
    unittest.main(testRunner=unishark.BufferedTestRunner(reporters=[reporter]))
