import inspect
import sys

for f in inspect.stack():
    print(f._source)