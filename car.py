#!/usr/bin/python3
import cgi
import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "HR.26 BR.9044":
    print("<body style='padding: 35px;'>")
    print('<h1 style="color:#fd043a;" >Output</h1>')
    print('''<pre>
    Registration Name     : Dadu.S
    License Number        : 6437912846
    Registration Date     : 10/Jan/2010
    Registering Authority : Haryana, India
    Model                 :  M-201
    Vehicle Class         : COOPERS
    Engine                : TFSI
    Fuel Type             : Petrol
    Insurance Upto        : 2/Apr/2022
    Fitness Upto          : 24/oct/2030
    </pre>''')
    print("</body>")

elif cmd == "H982 FKL":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#fd043a;" >Output</h1>')
    print('''<pre>
    Registration Name     : Utkarsh Srivastava
    License Number        : 37916482507
    Model                 : BMW / 107-S
    Registration Date     : 22/Feb/2013
    Registering Authority : Delhi, India
    Vehicle Class         : PORSCHE
    Engine                : S70/2
    Fuel Type             : Petrol: i, Diesel: d
    Insurance Upto        : 12/Dec/2024
    Fitness Upto          : 20/Aug/2035
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#fd043a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
