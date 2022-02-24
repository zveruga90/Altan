# *** kollektsiya ***

# spisok (list)

# sozdanie pustogo spiska

list_1 = []
list_2 = list()

# sozdanie predvritelno zapolnennogo spiska
list_3 = [10, 20, 7, 3.14, "python", "!", [1,2,3]]

# dobavlenie obecta (elementa) v spisok
list_1.append(1000)
list_1.append("A")

list_3.append(0.0)

# dobalenie obecta po indeksu
list_3.insert(3, "hello")

# dobavlenie interiruemyh obectov
list_3.extend([100, 200])
list_3.extend("hello")

# chtenie znachenii elementov spiska
# pryamaya indeksatsiya
el_1 = list_3[0]
# el_2 = list_3[20]

#uznaem dlinu ili kolichestvo elementov spiska
# print(f"dlina spiska = {len(list_3)}")

el_2 = list_3[15]

# obratnaya indeksatsiya
el_3 = list_3[-1]

# chtenie znachenii vlozhennyh kollektsii
list_4 = [[1,2,3], [10,20,30,40,50]]

# print(list_4[1][-1])

#zamena znachenii
list_5 = list("hello, world!")

list_5[1] = 100

# udalenie elementov po indeksu
del list_5[-1]


# udalenie elementov po znacheniyu (pervoe sovpadenie)

# list_5.remove("l")


# srezy spiska
list_5 = list("hello, world!")
# srez ot nachala do indeksa b
# konechniy indeks ne vklyuchaetsya v srez

slice_1 = list_5[0:5]
slice_1 = list_5[:5]

# srez ot indeksa proizvolnogo a do b
slice_2 = list_5[1:5]

# srez ot indeksa proizvolnogo a do kontsa spiska
slice_3 = list_5[5:]

# shak sreza ot indeksa A lj indeksa B c shagom
slice_3 = list_5[1:10:2]

# shak sreza ot indeksa A do indeksa B c shagom
slice_3 = list_5[-2:-10:-2]

slice_3 = list_5[::-1]

print(list_5)
print(slice_3)
