import init

while(True != False):
    print("|-------------------------------------------------|")
    print("|               Programa graficas                 |")
    print("|-------------------------------------------------|\n")
    print("Seleccione que laboratiorio quiere probar:\n 1)SR1 \n 2)SR2 \n 3)SR3 \n 4)SR4")

    inp = input("--->")

    if(inp == "1"):
        init.glInit("bmp")
    elif(inp == "2"):
        init.glInit("line")
    elif(inp == "3"):
        init.glInit("obj")
    elif(inp == "4"):
        init.glInit("obj")
    else:
        print("|-------------------------|")
        print("|     Datos Invalidos     |")
        print("|-------------------------|")
    


