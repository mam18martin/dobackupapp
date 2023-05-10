class miobjeto:
    mivar = None
    otra = None

    def __init__(self) -> None:
        pass

def mifuncion(vobj):
    vobj.mivar = "A verga"
    print(vobj)

ob = miobjeto()

print(ob)

mifuncion(ob)

print(ob.mivar)

def noseque():
    print("No se que")

  




#--------------------------------------------------------
#salida = None
#delimiter = '<br>'

#with open("logs/dumplog-20230505-1328.txt", "r") as f:
#    file = f.readlines()
#    salida = delimiter.join(file)

#htmlstr = "<div>"
#htmlstr += delimiter.join(salida.split("\\n"))
#htmlstr += "</div>"

#with open("logs/salida.html", "+a") as h:
#    h.write(htmlstr)