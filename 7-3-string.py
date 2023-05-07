
codebook=""" yhspqedirgvxwlukzofjambntc
rlhpndkqgjvszobmfiaeutcyxw
lizncrmbtouhdxsfapeqjvwkyg
kqlhazijdusvcrwnoxfpytebgm
gpfersjxwlokqacznutdhvbmyi
hjplgsdyxmoubnftqczawvkire
vmpeysukjtlwichdfobaqngzrx
yujmdqvtegrinhsolkwazfbpxc
mzgfoherplkuaxbicdjtnsvqwy
openjagrvqtxhdwzblcuiysfmk"""



codebook=codebook.split('\n')

def encrypt(codebook, text):
    output_str=''
    i=0
    for c in text:
        if c.isalpha():
            row_index=i%10
            is_upper_case=c<'a'
            if is_upper_case:
                c=c.lower()
            col_index=ord(c)-ord('a')
            encrypted_c=codebook[row_index][col_index]
            
            if is_upper_case:
                encrypted_c=encrypted_c.upper()
            output_str+=encrypted_c
            
            
        else:
            output_str+=c
        i+=1
        
    return output_str    


def decrypt(codebook,text):
    
    output_str=''
    i=0
    for c in text :
        if c.isalpha():
            row_index=i%10
            is_upper_case=c<'a'
            if is_upper_case:
                c=c.lower()
            row_str= codebook[row_index]
            j=0
            for e in row_str:
                if e==c:
                    break
                j+=1
            derypted_c=chr(ord('a')+j)
            if is_upper_case:
                decrypted_c=decrypted_c.upper()
                
            output_str+=decrypted_c
        else:
            output_str+=c
        i+=1
    return output_str

text=input()
if text[0]=='e':
    text=text[1:]
    print(encrypt(codebook, text))
elif text[0]=='d':
    text=text[1:]
    print(decrypt(codebook, text))
else:
    pass
            
            
            
            
            
            
