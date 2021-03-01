import unittest

from task import DictMachine

class TestDictMachine(unittest.TestCase):
    def test_dictmachine_right(self):
        input_data = {
            'hired':{
                'be':{
                    'to':{
                        'deserve':'I'
                    }
                }
            }
        }
        output_value = {
            'I': {
                'deserve': {
                    'to': {
                        'be': 'hired'
                    }
                }
            }
        }
        dm = DictMachine(input_data)
        res = dm.get_reverse_dict()
        self.assertEqual(res, output_value)
    def test_dictmachine_error(self):
        input_data = {
            'hired':{
                'be':{
                    'to':{
                        'deserve':'I'
                    }, 
                    'to':{
                        'deserve':'I'
                    }
                }
            }
        }
        dm = DictMachine(input_data)
        with self.assertRaises(Exception) as context:
            res = dm.get_reverse_dict()
            self.assertTrue('unsupport type of dict, key should be 1' in context.exception)

if __name__ == '__main__':
    unittest.main()