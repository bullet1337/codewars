# https://www.codewars.com/kata/5950eec3a100d72be100003f
class E():
    def __init__(self, func, failure, exceptions_types):
        self.func = func
        self.failure  = failure
        self.exceptions_types = tuple(exceptions_types)
        
    def __enter__(self):
        pass
        
    def __exit__(self, type, value, traceback):
        if isinstance(value, self.exceptions_types):
            self.failure(self.func, value)
            return True
            

def handle(func, success, failure, *exception_types):
    with E(func, failure, exception_types):
        success(func, func())