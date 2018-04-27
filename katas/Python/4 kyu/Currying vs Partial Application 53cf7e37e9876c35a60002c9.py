# https://www.codewars.com/kata/53cf7e37e9876c35a60002c9
def curry_partial(f, *initial_args):
    if not callable(f):
        return f

    n_args = f.n_args if type(f).__name__ != 'function' else len(f.func_code.co_varnames)
    if n_args == 0:
        return f(*initial_args)

    if not initial_args:
        class G:
            def __init__(self, n_args=0):
                self.n_args = n_args

            def __call__(self, *args):
                if n_args <= len(args):
                    return f(*args[:n_args])
                else:
                    class F(G):
                        def __call__(self, *rest):
                            return G(self.n_args)(*(args + rest))
                    return F()
        return G(n_args)
    else:
        if n_args <= len(initial_args):
            return f(*initial_args[:n_args])
        else:
            class G:
                def __init__(self, n_args):
                    self.n_args = n_args

                def __call__(self, *args):
                    return f(*(initial_args + args))

            return curry_partial(G(n_args - len(initial_args)))