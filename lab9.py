import base64
import random
import base64

def inversa(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
    
def esprimo(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

def generarE(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e
def fi(num): 
    if(esprimo(num)):
        return number-1
    else:
        return False

def generarPrimo(): 
    while True: 
        x=random.randrange(200,1000) 
        if(esprimo(x)==True):
            return x
        
def GenerarClaves():
    p = generarPrimo()
    q = generarPrimo()
    n = p*q
    phi_n = (p-1) * (q-1)
    e = generarE(phi_n)
    d = inversa(e, phi_n)
    llave_publica = (str(e)+(".")+str(n))
    llave_privada = (str(d)+(".")+str(n))

    encodedBytes = base64.b64encode(llave_publica.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    encodedBytes2 = base64.b64encode(llave_privada.encode("utf-8"))
    encodedStr2 = str(encodedBytes2, "utf-8")
    
    print("p:",p)
    print("q:",q)
    print("n:",n)
    print("phi_n:",phi_n)
    print("e:",e)
    print("d:",d)
    print("llave publica:",llave_publica)
    print("llave publica base 64:",encodedStr)
    print(llave_privada)
    print("llave privada base 64:",encodedStr2)

llavePublica = "MzEzMTUxLjQxODM2Nw=="
llavePrivada = "NTc5OTM1LjQxODM2Nw=="

def Encriptar(llave, mensaje):
    base64_bytes = llave.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    claves = message.split(".")
    key = int(claves[0])
    n = int(claves[1])
    cipher = [pow(ord(char), key, n) for char in mensaje]
    concatenado = ""
    for i in cipher:
        concatenado += str(i)
    encodedBytes = base64.b64encode(concatenado.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(encodedStr)
    
    return cipher

def decriptado(llave, mensaje):
    base64_bytes = llave.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    claves = message.split(".")
    key = int(claves[0])
    n = int(claves[1])
#    base64_bytes = mensaje.encode('ascii')
 #   message_bytes = base64.b64decode(base64_bytes)
 #   message = message_bytes.decode('ascii')
 #   print(message)
    aux = [str(pow(char, key, n)) for char in mensaje]
    plain = [chr(int(char2)) for char2 in aux]
    return print(''.join(plain))

while True:
    print("1. Generar claves")
    print("2. Encriptar mensaje")
    print("3. Decriptar mensaje")
    print("4. Salir.")
    opcion = input("Ingresa el numero de opcion a elegir\n")
    if(opcion == "1"):
        print("Generar Claves")
        GenerarClaves()
        
    elif(opcion == "2"):
        print("Encriptar mensaje")
        mensaje = input("Ingrese el mensaje a cifrar:\n")
        print("Mensaje encriptado:")
        mensaje_encriptado = Encriptar(llavePublica,mensaje)
    elif(opcion == "3"):
        print("Decriptar mensaje")
        print("Mensaje decriptado:")
        decriptado(llavePrivada, mensaje_encriptado)
    elif(opcion == "4"):
        break
