

def valid_braces(string):
    brace_list = []

    for brace in string:
        
        if brace == '(' or brace == '{' or brace == '[':
            brace_list.append(brace)
        else:
            open_brace = brace_list.pop() if brace_list else ""
            if open_brace == '(' and brace == ')':
                continue
            elif open_brace == '{' and brace == '}':
                continue
            elif open_brace == '[' and brace == ']':
                continue
            else:
                return False
    return len(brace_list) == 0

print(valid_braces("{)"))
