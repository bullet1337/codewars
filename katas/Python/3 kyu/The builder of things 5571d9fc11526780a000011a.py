# https://www.codewars.com/kata/5571d9fc11526780a000011a
import inspect


class Thing:

    def __init__(self, name):
        self.name = name
        self._is_a = None
        self._is_the = False
        self._of = None
        self._has = 0
        self._having = 0
        self._being_the = False
        self._prop = None
        self._can = False
        self._last_access = self
        self._iter = True
        self.__dict__['is_' + name] = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter:
            self._iter = False
            return self
        else:
            self._iter = True
            raise StopIteration

    def __getattr__(self, item):
        if self._is_a is not None:
            for element in self._last_access:
                element.__dict__['is_a_' + item] = self._is_a
            self._is_a = None
        elif self._is_the and item.endswith('_of'):
            self._of = item
            self._is_the = False
        elif self._of:
            for element in self._last_access:
                element.__dict__[self._of] = item
            self._of = None
        elif self._has:
            self.__dict__[item] = Thing(item) if self._has == 1 else tuple(Thing(item[:-1]) for _ in range(self._has))
            self._last_access = self.__dict__[item]
            self._has = 0
        elif self._having:
            for element in self._last_access:
                element.__dict__[item] \
                    = Thing(item) if self._having == 1 else tuple(Thing(item[:-1]) for _ in range(self._having))
            self._last_access = [x for element in self._last_access for x in element.__dict__[item]]
            self._having = 0
        elif self._being_the:
            self._prop = item
            self._being_the = False
        elif self._prop is not None:
            for element in self._last_access:
                element.__dict__[self._prop] = item
            self._prop = None
        elif self._can:
            def f(fnc, history=None):
                for k, v in self.__dict__.items():
                    if k[0] != '_' and type(k) != 'function':
                        inspect.stack()[1][0].f_globals[k] = v

                def g(*args):
                    res = fnc(*args)
                    if history:
                        self.__dict__[history].append(res)
                    return res
                if history:
                    self.__dict__[history] = []
                self.__dict__[item] = g
            self.item = f
            self._can = False
            return f
        return self

    @property
    def is_a(self):
        self._is_a = True
        return self

    @property
    def is_not_a(self):
        self._is_a = False
        return self

    @property
    def is_the(self):
        self._is_the = True
        return self

    @property
    def each(self):
        return self

    @property
    def being_the(self):
        self._being_the = True
        return self

    @property
    def and_the(self):
        self._being_the = True
        return self

    @property
    def can(self):
        self._can = True
        return self

    def has(self, count):
        self._has = count
        return self

    def having(self, count):
        self._having = count
        return self