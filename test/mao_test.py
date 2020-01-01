import unittest
from urllib import parse


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_parse(self):
        dict1 = {'wd': '与经济发展相关的指标'}
        url_data = parse.urlencode(dict1)  # unlencode()将字典{k1:v1,k2:v2}转化为k1=v1&k2=v2
        url = 'http://www.baidu.com/s?' + url_data
        print(url)
        url_data2 = '经济指标'
        url2 = 'http://www.baidu.com/s?wd=' + parse.quote(url_data2)
        print(url2)


if __name__ == '__main__':
    unittest.main()
