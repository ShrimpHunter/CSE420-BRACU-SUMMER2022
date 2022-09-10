company = 'gmail yahoo hotmail protonmail edumail g.bracu.ac.bd'.split()
domain = 'com net g.bracu.ac.bd bd org gov net edu biz uk us au'.split()


def num_start(str):
    if str[0] in "0123456789":
        return True
    else:
        return False


def web_front(str):
    if str[:4] == "www.":
        return True
    else:
        return False


def domain_back(str):
    temp = str.split('.')
    domain = ''
    for i in temp[-1]:
        domain += i

    return domain


def find_mail_company(str):
    temp = str.split('@')
    company = ''

    if 'g.bracu.ac.bd' in temp[1]:
        return 'g.bracu.ac.bd'

    for i in temp[1]:
        if i == '.':
            return company
        else:
            company += i


def caller(str, pos):
    if num_start(str):
        pass

    elif web_front(str) and domain_back(str) in domain and '@' not in str and str[-1] != '.':
        print('Web,', pos)

    elif '@' in str and not web_front(str) and find_mail_company(str) in company and domain_back(
            str) in domain and str[-1] != '.':
        print('Email,', pos)


f = open("input.txt", 'r')
inp = f.read()
inp = inp.splitlines()
[caller(j, i) for i, j in enumerate(inp)]