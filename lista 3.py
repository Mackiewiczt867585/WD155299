import math
from random import random
# #zadanie 1
# #A
# liczby=[1,2,3,4,5,6,7,8,9,10,11]
# A=[1/x for x in liczby]
# print(A)
# #B
# B=[2**x for x in range(10)]
# print(B)
# #C
# C=[x for x in B if x % 4 == 0]
# print(C)

# #zadanie 2
# M=[[round(random()*1000) for y in range(1+4*x,5+4*x)] for x in range(4)]
# print(M)
# przekatna=[M[x][x]for x in range(4)]
# print(przekatna)

# #zadanie 3
# slownik = {'pomidor':'waga','batony':'sztuki', 'woda':'litry','piwo':'sztuki'}
# print(slownik)
# odw = {key for key in slownik if slownik[key]=='sztuki'}
# print(odw) 

# #zadanie 4
# def monotonicznosc(a,b):
#     if(a<0):
#         print("ta funkcja jest malejaca")
#     elif (a==0):
#         printf("ta funkcja jest stala")
#     else:
#         print("ta funckja jest rosnaca")
# a=int(input('podaj a:'))
# b=int(input('podaj b:'))
# print(monotonicznosc(a,b))

# #zadanie 5
# def polozenie(a1,a2):
#     if(a1==a2):
#         print("te proste sa rownolegle")
#     elif(a1*a2==-1):
#         print("te proste sa prostopadle")
# print(polozenie(4,-0.25))

# #zadanie 6
# def promien (x=2,y=2,a=1,b=1):
#     r=(x-a)*(x-a)+(y-b)*(y-b)
#     r=math.sqrt(r)
#     return r
# print(promien())
# print(promien(2,2,1,1))

# #zadanie 7
# def przeciwprostokatna(a=2,b=1):
#     przeciw=(a**2)+(b**2)
#     przeciw=math.sqrt(przeciw)
#     return przeciw
# print(przeciwprostokatna(3,4))

# #zadanie 8
# def suma_ciagu(a1=1,r=1,ile=10):
#     if (ile==1):
#         suma=((2*a1+(ile-1)*r)/2)*ile
#     return suma
# print(suma_ciagu(1,1,3))

# #zadanie 9
# def il_ciagu(* liczby):
#     if (len(liczby)==0):
#         return a1
#     else:
#         il=1
#         for i in liczby:
#             il*=i
#     return il
# print(il_ciagu(1,1,3))

# #zadanie 10
# def lista (**klucz):
#     print("lista zakupow:\n")
#     ile=0
#     for i in klucz:
#         print(i,klucz[i])
#         ile+=klucz[i]  
#     print("\n Ilosc produktow:",ile)
# lista(kasztan=3,piwo=1,but=2)

