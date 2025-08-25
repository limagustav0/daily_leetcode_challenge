import re
def to_camel_case(s):
    '''
    Given a string, return its camel case version using the following rules:

    Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
    The first word should be all lowercase.
    Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
    All spaces and separators should be removed.
    '''
    l = re.split('[- _]+', s.lower().strip())
    s = [l[index].capitalize() for index in range(1,len(l))]
    s="".join(l)
    return s


if __name__=="__main__":
    print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))