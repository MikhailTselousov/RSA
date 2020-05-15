import random
import math

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext

import time
from decimal import Decimal

N = 0
e = 0
s = 0

def Fermat(N):
        if N%2 == 0:
                return False
        for i in range(100):
                i = i
                a = random.randint(2, N-2)
                if pow(a, N-1, N) != 1 :
                        return False
        return True

def Euclid(a, b):
        r = -1
        while r != 0:
                r = a%b
                a = b
                b = r
        return a

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0

def Jacobi(a, b):
        if Euclid(a,b) != 1 :
                return 0

        r = 1
        
        if a<0:
                a = -a
                if b%4 == 3 :
                        r = -r

        check = 0
        while check != 1:
                t = 0
                while a%2 == 0:
                        t = t+1
                        a = a/2

                if t%2 == 1:
                        if b%8 == 3 or b%8 == 5 :
                                r = -r

                if a%4 == b%4  == 3 :
                        r = -r
                c = a
                a = b%c
                b = c

                if a == 0:
                        check = 1
        
        return r

def SolovayStrassen(N):
        if N%2 == 0:
                return False
        for i in range(100):
                i=i
                a = random.randint(2, N-1)
                if Euclid(a, N) > 1:
                        return False
                if pow(a, int((N-1)/2), N) != (int(Jacobi(a, N)))%N:
                        return False
        return True

def primeFactors(n):
        factors = []
        if n%2 == 0:
                factors.append(2)
                while n%2 == 0:
                        n = n/2

        f = math.sqrt(n)
        i = 3
        while (i <= f) :
                if n%i == 0:
                        factors.append(i) 
                        while n%i == 0:
                                n = n/i
                i = i + 1
        if n>2:
                factors.append(n)
        return factors

def LucasTest(N):
        if N%2 == 0:
                return False
        
        factors = primeFactors(N-1)

        for i in range(20):
                a = random.randint(2, N-1)
                if pow(a, N-1, N) != 1:
                        return False
                else:
                        check = True
                        for j in factors:
                                if pow(a, int((N-1)/j), N) == 1:
                                        check = False
                                        break
                        if check == True :
                                return True

        return False

def getNumberOfDigits(N):
        count = 0
        while (N > 0):
                count = count + 1
                N = N//10
        return count

def RSAencrypt():
        input = inputTab1.get(0.0, tk.END)
        input = list(input)
        input.pop(-1)
        s = int(inputstab1.get())
        N = int(inputNtab1.get())

        r = ""

        for i in input:
                t = ord(i)
                t = pow(t, s, N)
                t = str(t)
                t = t + '\n'
                r = r + t

        r = r[:-1]
        outputTab1.delete(1.0, tk.END)
        outputTab1.insert(tk.END, r)       

        return 0

def RSAdecrypt():
        input = inputTab2.get(0.0, tk.END)
        while input[-1] == '\n':
                input = input[:-1]
        input = input.split('\n')
        
        print(input)
        
        N = int(inputNtab2.get())
        e = int(inputetab2.get())

        r = ""

        for i in input:
                c = int(i)
                chi = pow(c, e, N)
                ch = chr(chi)
                r = r + ch

        outputTab2.delete(1.0, tk.END)
        outputTab2.insert(tk.END, r)

        return 0

def NesGen():
        print("ive started")
        starttime = time.time()
        checkO = 0
        while checkO != 1:
                check = 0
                while check != 1:
                        P = random.randint(4 * 1e12, 1e13 - 1)
                        fermathtrue = False
                        startfermathtime = Decimal(time.time())
                        fermathtrue = Fermat(P)
                        endfermathtime = Decimal(time.time())
                        if (fermathtrue == True):
                                lucastrue = False
                                startlucastime = Decimal(time.time())
                                lucastrue = LucasTest(P)
                                endlucastime = Decimal(time.time())
                                if (lucastrue == True):
                                        check = 1

                print("P FermathTime = ", Decimal(endfermathtime - startfermathtime))
                print("P LucasTime = ", Decimal(endlucastime - startlucastime))

                check = 0
                while check != 1:
                        Q = random.randint(4 * 1e13, 1e14 - 1)
                        fermathtrue = False
                        startfermathtime = Decimal(time.time())
                        fermathtrue = Fermat(Q)
                        endfermathtime = Decimal(time.time())
                        if (fermathtrue == True):
                                lucastrue = False
                                startlucastime = Decimal(time.time())
                                lucastrue = LucasTest(P)
                                endlucastime = Decimal(time.time())
                                if (lucastrue == True):
                                        check = 1
                
                print("Q FermathTime = ", Decimal(endfermathtime - startfermathtime))
                print("Q LucasTime = ", Decimal(endlucastime - startlucastime))

                N = P*Q
                print("N = ", N)
                if getNumberOfDigits(N) == 27:
                        checkO = 1

        print("P = " + str(P)+" Q = "+str(Q))
        d = (P-1)*(Q-1)

        check = 0
        while check != 1:
                s = random.randint(2, d-1)
                if Euclid(s,d) == 1:
                        check = 1
        
        e = xgcd(s, d)
        while (e < 0):
                e = e + d

        N_ = "N = "+str(N)
        e_ = "e = "+str(e)
        s_ = "s = "+str(s)

        print(N_ + " " + e_ + " " + s_)

        labelNgen.config(state = tk.NORMAL)
        labelNgen.delete(1.0, tk.END)
        labelNgen.insert(tk.END, N_)
        labelNgen.config(state = tk.DISABLED)

        labelegen.config(state = tk.NORMAL)
        labelegen.delete(1.0, tk.END)
        labelegen.insert(tk.END, e_)
        labelegen.config(state = tk.DISABLED)

        labelsgen.config(state = tk.NORMAL)
        labelsgen.delete(1.0, tk.END)
        labelsgen.insert(tk.END, s_)
        labelsgen.config(state = tk.DISABLED)

        print("time of Gen N.e.s = ", time.time() - starttime)
        print()

        return 0


#Window placement
window = tk.Tk()
window.title("RSA")
window.resizable(False, False)

tabcontrol = ttk.Notebook(window)
tabNesGen = ttk.Frame(tabcontrol)
tabencrypt = ttk.Frame(tabcontrol)
tabdecrypt = ttk.Frame(tabcontrol)
tabcontrol.add(tabNesGen, text = "N.e.s. Gen")
tabcontrol.add(tabencrypt, text="Encrypt")
tabcontrol.add(tabdecrypt, text = "Decrypt")
tabcontrol.pack(expand = 0, fill="both")

#N.e.s. Gen
labelNgen = tk.Text(tabNesGen, height = 9, width = 50)
labelNgen.delete(1.0, tk.END)
labelNgen.insert(1.0, "N = ")
labelNgen.config(state = tk.DISABLED)
#labelNgen.pack(expand = 0, fill="both")
labelNgen.grid(row = 0, column = 0, padx = 15, pady = 5)
labelegen = tk.Text(tabNesGen, height = 9, width = 50)
labelegen.delete(1.0, tk.END)
labelegen.insert(1.0, "e = ")
labelegen.config(state = tk.DISABLED)
#labelegen.pack(expand = 0, fill="both")
labelegen.grid(row = 1, column = 0, padx = 15, pady = 5)
labelsgen = tk.Text(tabNesGen, height = 9, width = 50)
labelsgen.delete(1.0, tk.END)
labelsgen.insert(1.0, "s = ")
labelsgen.config(state = tk.DISABLED)
#labelsgen.pack(expand = 0, fill="both")
labelsgen.grid(row = 2, column = 0, padx = 15, pady = 5)
GenButton = tk.Button(tabNesGen, text = "Gen", command = NesGen, width = 50)
GenButton.grid(row = 3, column = 0, padx = 15, pady = 5)

#encypt frame
labels = tk.Label(tabencrypt, text = "s = ")
labels.grid(row = 0, column = 1, sticky= tk.E)
inputstab1 = tk.Entry(tabencrypt, width = 20)
inputstab1.grid(row = 0, column = 2, padx = 5, pady = 10, sticky = tk.W)

labelN = tk.Label(tabencrypt, text = "N = ")
labelN.grid(row = 1, column = 1, sticky= tk.E)
inputNtab1 = tk.Entry(tabencrypt, width = 20)
inputNtab1.grid(row = 1, column = 2, padx = 5, pady = 10, sticky = tk.W)

inputTab1 = tk.Text(tabencrypt, width = 50, height = 10)
inputTab1.grid(row = 2, columnspan = 4, pady = 10, padx = 15)

button1Tab1 = tk.Button(tabencrypt, text = "Encrypt", command = RSAencrypt)
button1Tab1.grid(row = 3, columnspan = 4, pady=5)

outputTab1 = tk.Text(tabencrypt, width = 50, height = 10)
outputTab1.grid(row = 4, columnspan = 4, pady = 10, padx = 15)

#decypt frame
labele = tk.Label(tabdecrypt, text = "e = ")
labele.grid(row = 0, column = 1, sticky= tk.E)
inputetab2 = tk.Entry(tabdecrypt, width = 20)
inputetab2.grid(row = 0, column = 2, padx = 5, pady = 10, sticky = tk.W)

labelN = tk.Label(tabdecrypt, text = "N = ")
labelN.grid(row = 1, column = 1, sticky= tk.E)
inputNtab2 = tk.Entry(tabdecrypt, width = 20)
inputNtab2.grid(row = 1, column = 2, padx = 5, pady = 10, sticky = tk.W)

inputTab2 = tk.Text(tabdecrypt, width = 50, height = 10)
inputTab2.grid(row = 2, columnspan = 4, pady = 10, padx = 15)

button1Tab2 = tk.Button(tabdecrypt, text = "Decrypt", command = RSAdecrypt)
button1Tab2.grid(row = 3, columnspan = 4, pady=5)

outputTab2 = tk.Text(tabdecrypt, width = 50, height = 10)
outputTab2.grid(row = 4, columnspan = 4, pady = 10, padx = 15)

window.mainloop()


