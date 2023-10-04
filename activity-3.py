def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key},{value}")


name_args(scott="cool")


def all_true(*arg):
    return all(arg)

print(all_true(True))
print(all_true(True,False))

def one_true(*args):
    return any(args)

print(one_true(True,False))

def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_factorial(num-1)
    

print(recursive_factorial(6))

def recurs_dedup(string, i = 0):
    if len(string) <=1 or i == len(string) - 1:
        return string
    else:
        if string[i] == string[i+1]:
            return recurs_dedup(string[0:i] + string[i+1:],i)
        else:
            return recurs_dedup(string, i + 1)
        
print(recurs_dedup('appppppple'))

def recurs_reversed(string,i=0):
    if len(string) == 0:
        return ''
    elif i == len(string)-1:
        return string[0]
    else:
        return string[-1 - i] + recurs_reversed(string,i+1)
    

print(recurs_reversed('apple'))