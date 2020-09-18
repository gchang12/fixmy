from os import walk
from os.path import sep

#	The path where "paths.txt" is located, including "paths.txt"
filename=''

k=0

with open(filename,'r') as r_file:
    for line in r_file:
        if k >1:
            break
        line=line.strip()
        if k==0:
            source=line
        else:
            destination=line
        k+=1

oldname=source.split(sep)[-1]
newname=destination.split(sep)[-1]

#   Folders to exclude
excluded=('.idea','__pycache__','VIEW HISTORY','compiled')

name_to_prefix={}
search_in=[]

first=True

for stuff in walk(source):
    path=stuff[0]; files=stuff[-1]
    ls=path.split(sep)
    tail=ls[-1]
    if tail in excluded:
        continue
    tail+='.'
    midtail=ls[-2]+'.'
    if first:
        first=False
        item1=tail
    if midtail in name_to_prefix.values():
        if midtail!=item1:
            tail=midtail+tail
    for file in files:
        if file[-3:] == '.py':
            module=file[:-3]
            if module == tail[:-1]:
                continue
            search_in+=[(path,file)]
            name_to_prefix[module]=tail

old_to_new=[]

for key,val in name_to_prefix.items():
    repl_val='from '+ val + key
    if oldname == repl_val[5:5+len(oldname)] or ' '+oldname in repl_val:
        repl_val=repl_val.replace(oldname,newname)
    else:
        u=repl_val.split(' ')
        u.insert(1,newname+'.')
        mod=[u[1]+u[2]]
        repl_val=' '.join([u[0]]+mod)
    n = len(newname)
    old_to_new += [('from ' + key, repl_val),('from '+oldname+repl_val[5+n:],repl_val)]

if __name__=='__main__':
    initlist=tuple()
    for stuff in old_to_new:
        mdl=stuff[-1]+' import *'
        if mdl not in initlist:
            initlist+=mdl,
    home=sep.join(source.split(sep)[:-1])
    f=['__init__.py']
    p=home.split(sep)
    l=tuple()
    for stuff in initlist:
        u=stuff[5:-9]
        v=u.split('.')[:-1]
        newpath=sep.join(p+v+f)
        if newpath not in l:
            l+=newpath,
    for thin in l:
        print(thin)
        with open(thin,'r') as rfile:
            for line in rfile.readlines():
                print(line)