import random
resposta = "y"
resposta=input("Voçê quer jogar um dado? y ou n:")
while resposta ==  "y":
    no = random.randint(1,6)
    if no == 1:
      print("[-----]")
      print("[--0--]")
      print("[-----]")
    elif no == 2:
      print("[0----]")
      print("[-----]")
      print("[----0]")
    elif no == 3:
      print("[0----]")
      print("[--0--]")
      print("[----0]")
    elif no == 4:
      print("[0---0]")
      print("[-----]")
      print("[0---0]")
    elif no == 5:
      print("[0---0]")
      print("[--0--]")
      print("[0---0]")
    elif no == 2:
      print("[0---0]")
      print("[0---0]")
      print("[0---0]")
     
    resposta = input("deseja continuar? y ou n : ")
    