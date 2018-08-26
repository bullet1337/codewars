# https://www.codewars.com/kata/53574972e727385ad10002ca
spoken = lambda msg: msg + '.'
shouted = lambda msg: msg.upper() + '!'
whispered = lambda msg: msg.lower() + '.'

greet = lambda style, msg: style(msg)