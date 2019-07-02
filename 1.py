class GenderException(Exception):
    def __init__(self,errMsg):
        super().__init__()
        self.errMsg = errMsg
    def __str__(self):
        return GenderException.__name__+':'+self.errMsg

a=GenderException('abc')
print(a)
