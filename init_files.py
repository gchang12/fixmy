from fixmy.prefixes import *


def fix_init():
    initlist = tuple()
    for stuff in old_to_new:
        mdl = stuff[-1] + ' import *'
        if mdl not in initlist:
            initlist += mdl,
    home = sep.join(destination.split(sep)[:-1])
    f = ['__init__.py']
    p = home.split('\\')
    e = {}
    for stuff in initlist:
        u = stuff[5:-9]
        v = u.split('.')[:-1]
        newpath = sep.join(p + v + f)
        if f[0][:-3] in u:
            continue
        if newpath in e.keys():
            e[newpath] += stuff,
        else:
            e[newpath] = stuff,
    for key, val in e.items():
        with open(key, 'w') as wfile:
            for m in val:
                wfile.write(m), wfile.write('\n')


if __name__=='__main__':
    fix_init()