s=input()
l=s.split(',')

output_str=''

for e in l:
    e=e.strip()
    if e[0]=='x':
        e='0'+e
        decimal_num=int(e,16)
        output_str+=str(decimal_num)+' '
    
    
    elif e[:2]=='0x':
        decimal_num=int(e,16)
        output_str+=str(decimal_num)+' '
        
    else:
        output_str+=e+' '
                
 

print(output_str, end='')        
