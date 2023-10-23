import numpy as np 
import math as mt 
from collections import counter


#peluang
#hitung peluang untuk mendapatkan kartu AS dalam 52 kartu, dimana kartu AS jumlahnya 4

kartu = 52
kartu_AS = 4

peluang_AS = kartu_AS / kartu

print(round(peluang_AS,2)
persen = peluang_AS *100
print (str(round(persen, 0))  + '%')
