salida = None
delimiter = '<br>'

with open("logs/dumplog-20230505-1328.txt", "r") as f:
    file = f.readlines()
    salida = delimiter.join(file)

htmlstr = "<div>"
htmlstr += delimiter.join(salida.split("\\n"))
htmlstr += "</div>"

with open("logs/salida.html", "+a") as h:
    h.write(htmlstr)