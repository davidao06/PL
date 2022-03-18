import re

aliens_ids = ['_0898989811abced_','_abce','_09090909abcD0','_09090909abcD0dsaw231d','_09090909abcD0231dsad211_']

regex = r'^_\d+[A-Za-z]{3,}(.*[A-Za-z_])?$'

for s in aliens_ids:
    p = re.match(regex,s)
    if p:
        print("Valido",p.group())
    else:
        print("Invalido")