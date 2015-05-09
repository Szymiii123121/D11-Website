def newstring(s, char):
    ns = s.replace(char, "")
    return ns

def OneLetterAway(wordlist, root):
    f = open(wordlist, 'r').read()
    f = f.split()
    my = []
    for line in f:
        if len(line) <= len(root):
            for char in line:
                if newstring(line, char) == newstring(root, root[line.find(char)]):
                    my += line
    return my

OneLetterAway('dictall.txt', 'store')
