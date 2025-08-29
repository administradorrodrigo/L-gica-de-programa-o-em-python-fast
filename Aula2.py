
v = ('aeiouAEIOU')
while True:
    letra = input("Digite a letra que vc quer descobrir se é vogal ou consoante: ")
     
    if len(letra)!= 1:
        print("vc digitou mais de uma letra")
        continue
           
    for x in(letra):
            if x in (v):
                print("vc digitou uma vogal")
            else:
                print("vc digitou uma consoante")
                break       
    break  
        