from fixmy.prefixes import *


def mass_replace(replace_with=''):
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
    t={}
    for key, val in e.items():
        with open(key, 'w') as wfile:
            for m in val:
                if replace_with == '':
                    wfile.write(m), wfile.write('\n')
                else:
                    wfile.write(replace_with)
                    break
        with open(key,'r') as rfile:
            t[key] = tuple()
            for line in rfile.readlines():
                t[key]+=line,
    for ioio in t.values():
        if ioio[0] != replace_with:
            return False
    return True


if __name__=='__main__':
    x=mass_replace(replace_with='#')
    print(x)