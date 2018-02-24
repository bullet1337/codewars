# https://www.codewars.com/kata/5470c635304c127cad000f0d
from typing import List


class Expression:
    pass


class Normal(Expression):
    def __init__(self, c: str) -> None:
        self.c = c

    def __str__(self) -> str:
        return self.c


class Any(Expression):
    def __str__(self) -> str:
        return '.'


class Or(Expression):
    def __init__(self, lop: Expression, rop: Expression) -> None:
        self.lop = lop
        self.rop = rop

    def __str__(self) -> str:
        return '({!s}|{!s})'.format(self.lop, self.rop)


class ZeroOrMore(Expression):
    def __init__(self, op: Expression) -> None:
        self.op = op

    def __str__(self) -> str:
        return '{!s}*'.format(self.op)


class Str(Expression):
    def __init__(self, expressions: List[Expression]) -> None:
        self.expressions = expressions

    def __str__(self) -> str:
        return '({})'.format(''.join(str(e) for e in self.expressions))


class State:
    def __init__(self, expressions: List[Expression]=None) -> None:
        self.expressions = expressions or []
        self.or_delimiter = None


def process_expressions(expressions: List[Expression]) -> Expression:
    if len(expressions) > 1:
        return Str(expressions)
    elif len(expressions) == 1:
        return expressions[0]
    else:
        return Normal('')


def parseRegExp(input):
    if input == '':
        return ''

    states_stack = [State()]

    for c in input:
        if c == '.':
            states_stack[-1].expressions.append(Any())
        elif c == '*':
            if not states_stack[-1].expressions or \
                    isinstance(states_stack[-1].expressions[-1], ZeroOrMore) \
                    or states_stack[-1].or_delimiter == len(states_stack[-1].expressions):
                return ''

            states_stack[-1].expressions[-1] = ZeroOrMore(states_stack[-1].expressions[-1])
        elif c == '|':
            if states_stack[-1].or_delimiter is not None:
                return ''
            states_stack[-1].or_delimiter = len(states_stack[-1].expressions)

        elif c == '(':
            states_stack.append(State())
        elif c == ')':
            if len(states_stack) == 1:
                return ''

            if states_stack[-1].or_delimiter is not None:
                states_stack[-2].expressions.append(
                    Or(
                        process_expressions(states_stack[-1].expressions[:states_stack[-1].or_delimiter]),
                        process_expressions(states_stack[-1].expressions[states_stack[-1].or_delimiter:])
                    )
                )
            elif states_stack[-1].expressions:
                states_stack[-2].expressions.append(process_expressions(states_stack[-1].expressions))
            else:
                return ''

            states_stack.pop()
        else:
            states_stack[-1].expressions.append(Normal(c))

    if len(states_stack) != 1:
        return ''

    if states_stack[0].or_delimiter is not None:
        states_stack[0].expressions = [
            Or(
                process_expressions(states_stack[0].expressions[:states_stack[0].or_delimiter]),
                process_expressions(states_stack[0].expressions[states_stack[0].or_delimiter:])
            )
        ]

    return str(process_expressions(states_stack[0].expressions))

    return str(process_expressions(states_stack[0].expressions))