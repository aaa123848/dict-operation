"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
 
# Please write a function to reverse the following nested input value into output value
 
# Input:
# input_value = {
#   'hired': {
#     'be': {
#       'to': {

class DictMachine(object):
    def __init__(self, input_):
        self.input_ = input_
        self.key_list = [] 
        self.last_value = None
        self.__penetrate()

    def __penetrate(self):
        key_list = []
        target = self.input_
        while True:
            k, v = self.__get_key_value(target)
            key_list.append(k)
            if type(v) != dict:
                self.key_list = key_list
                self.last_value = v
                break
            target = v

    def __get_key_value(self, a_dict):
        if len(a_dict.keys()) != 1:
            raise ValueError('unsupport type of dict, key should be 1')
        key = next(iter(a_dict.keys()))
        value = next(iter(a_dict.values()))

        return key, value

    def __make_a_dict(self, key, value):
        return {key: value}

    def get_reverse_dict(self):
        value = self.key_list[0]
        for k in self.key_list[1:]:
            value = self.__make_a_dict(k, value)
        res = {}
        res[self.last_value] = value

        return res
  



