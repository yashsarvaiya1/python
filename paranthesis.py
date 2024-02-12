def paranthesis(s):
    if s.count('(') == s.count(')'):
        return True
    else:
        return False

print(paranthesis("(44(asd()())"))