from fixmy.prefixes import *

def copy_replace(src,dest,strings=old_to_new,replace=True):
    '''

    :param src: Path to source text file
    :param dest: Path to destination
    :param strings: list of 2-tuples
    :param replace: Indicates whether or not to replace
    :return: None
    '''
    original=tuple()
    with open(src,'r') as r_file:
        for line in r_file.readlines():
            original+=line,

    new=tuple()
    for line in original:
        l=line
        for tpl in strings:
            l=l.replace(tpl[0],tpl[-1])
        new+=l,

    l=dest.split(sep)[:-1]
    s=sep.join(l)
    from os.path import exists
    from os import mkdir

    ls=original
    if replace:
        ls=new

    if not exists(s):
        mkdir(s)
    with open(dest,'w') as w_file:
        for line in ls:
            w_file.write(line)


def list_diff(biglist,smalllist):
    l=[]
    for m in biglist:
        if m not in smalllist:
            l+=[m]
    return l


def fix_imports(src=source,dest=destination,files=search_in,replace=True):
    '''
    :param src: Where the module is being copied from
    :param dest: Where the module is being copied to
    :param files: List of 2-tuples of str objects
    :param replace: Indicates whether you wish to replace import names
    :return: None
    '''
    for path,file in files:
        l=dest.split(sep)
        s=src.split(sep)
        p=path.split(sep)
        branch=list_diff(p,s)
        if len(branch) > 0:
            l=sep.join(l+branch)
        else:
            l=sep.join(l)
        copy_replace(src=path+sep+file,dest=l+sep+file,replace=replace)


if __name__=='__main__':
    fix_imports()