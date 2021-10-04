from src.fonts import fonts
fonttype = input(f'Enter your font type. 0 - {fonts.__len__()-1} ')
inp = input("Enter your phrase. ")
normal = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
res = []
for char in inp:
    if char == ' ':
          res.append(' ')
    for indx,l in enumerate(normal):
        fixed = char.upper()
        
        
        if fixed in normal[indx]:
             res.append(fonts[int(fonttype)][indx])
response = ''
for char in res:
      response += char
print(response)
