class HotWaterException(Exception):
    def __init__(self, msg):
        self.msg = msg

class ColdWaterException(Exception):
    def __init__(self, msg):
        self.msg = msg

print(__name__)        
if __name__ == '__main__':
    print("lllll!!!")


