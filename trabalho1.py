# coding utf-8

"""
Fundamentos de Informática em Biomecânica
Nome: Maria Emília Llopes Castelucci  Nº: 11812604
Professor: Paulo Santiago
"""

real = [0 , 0, 0]
cam1 = [0 , 0, 0]
cam2 = [0 , 0, 0]
projcam1 = [0 , 0, 0]
projcam2 = [0 , 0, 0]

mr1 = [0 , 0, 0]
mr2 = [0 , 0, 0]
br1 = [0 , 0, 0]
br2 = [0 , 0, 0]

vetX = [0 , 0, 0]
vetY = [0 , 0, 0]

REC3D = [0 , 0, 0]

erro = [0 , 0, 0]

erroabs = [0 , 0, 0]

real[0] = float(input("Insira os valores reais de X: "))
real[1] = float(input("Insira os valores reais de Y: "))
real[2] = float(input("Insira os valores reais de Z: "))

cam1[0] = float(input("cam1 - Insira o valor de X da cam1: "))
cam1[1] = float(input("cam1 - Insira o valor de Y da cam1: "))
cam1[2] = float(input("cam1 - Insira o valor de Z da cam1: "))
cam2[0] = float(input("cam2 - Insira o valor de X da cam2: "))
cam2[1] = float(input("cam2 - Insira o valor de Y da cam2: "))
cam2[2] = float(input("cam2 - Insira o valor de Z da cam2: "))

projcam1[0] = float(input("projcam1 - Insira o valor de X da projeção da cam1: "))
projcam1[1] = float(input("projcam1 - Insira o valor de Y da projeção da cam1: "))
projcam1[2] = float(input("projcam1 - Insira o valor de Z da projeção da cam1: "))
projcam2[0] = float(input("projcam2 - Insira o valor de X da projeção da cam2: "))
projcam2[1] = float(input("projcam2 - Insira o valor de Y da projeção da cam2: "))
projcam2[2] = float(input("projcam2 - Insira o valor de Z da projeção da cam2: "))


mr1[0] = (projcam1[1] - cam1[1])/(projcam1[0] - cam1[0])
mr1[1] = (projcam1[2] - cam1[2])/(projcam1[0] - cam1[0])
mr1[2] = (projcam1[1] - cam1[1])/(projcam1[2] - cam1[2])
mr2[0] = (projcam2[1] - cam2[1])/(projcam2[0] - cam2[0])
mr2[1] = (projcam2[2] - cam2[2])/(projcam2[0] - cam2[0])
mr2[2] = (projcam2[1] - cam2[1])/(projcam2[2] - cam2[2])

br1[0] = (-1 * (mr1[0] * cam1[0] - cam1[1]))
br1[1] = (-1 * (mr1[1] * cam1[0] - cam1[2]))
br1[2] = (-1 * (mr1[2] * cam1[2] - cam1[1]))
br2[0] = (-1 * (mr1[0] * cam1[0] - cam1[1]))
br2[1] = (-1 * (mr1[1] * cam1[0] - cam1[2]))
br2[2] = (-1 * (mr1[2] * cam1[2] - cam1[1]))

vetX[0] = round((-(mr2[0]*cam2[0]) + cam2[1] + (mr1[0]*cam1[0]) - cam1[1]) / (mr1[0] - mr2[0]), 3)
vetX[1] = round((-(mr2[1]*cam2[0]) + cam2[2] + (mr1[1]*cam1[0]) - cam1[2]) / (mr1[1] - mr2[1]), 3)
vetX[2] = round((-(mr2[2]*cam2[2]) + cam2[1] + (mr1[2]*cam1[2]) - cam1[1]) / (mr1[2] - mr2[2]), 3)

vetY [0] = round(((mr1[0]*vetX[0]) - (mr1[0]*cam1[0]) + cam1[1]), 3)
vetY [1] = round(((mr1[1]*vetX[1]) - (mr1[1]*cam1[0]) + cam1[2]), 3)
vetY [2] = round(((mr1[2]*vetX[2]) - (mr1[2]*cam1[2]) + cam1[1]), 3)

REC3D[0] = round(((vetX[0] + vetX[1])/2), 3)
REC3D[1] = round(((vetY[0] + vetY[2])/2), 3)
REC3D[2] = round(((vetY[1] + vetX[2])/2), 3)

erro[0] = round(real[0] - REC3D[0], 3)
erro[1] = round(real[1] - REC3D[1], 3)
erro[2] = round(real[2] - REC3D[2], 3)

erroabs[0] = round(abs(erro[0]), 3)
erroabs[1] = round(abs(erro[1]), 3)
erroabs[2] = round(abs(erro[2]), 3)

print("X \t\t\t\t Y")
print(vetX[0],"\t",vetY[0])
print(vetX[1],"\t",vetY[1])
print(vetX[2],"\t\t",vetY[2])

print("\t\t\t\tx\t\t\ty\t\t\tz")
print("---------------------------------------------------")
print("REC3D\t\t", REC3D[0], "\t", REC3D[1],  "\t", REC3D[2])
print("Real\t\t", real[0], "\t\t", real[1], "\t\t", real[2])
print("Erro\t\t", erro[0], "\t\t", erro[1],  "\t\t", erro[2])
print("Erro Abs.\t", erroabs[0], "\t\t", erroabs[1],  "\t\t", erroabs[2])
print("---------------------------------------------------")

Errotot = (erroabs[0] + erroabs [1] + erroabs [2]) /3
print("Erro Total\t\t\t\t", Errotot)
