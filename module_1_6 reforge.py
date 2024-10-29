my_dict={"Vasya": 1975,"Egor":1999,"Masha":2002}
print (my_dict)
my_dict["Vasya"]=1976
print(my_dict["Vasya"])
print(my_dict.get("Dasha"))  #при вызове несуществующей выдает ошибку без добавления
my_dict.update({"Kolya":2001,"Anya":2003})
a=my_dict.pop("Vasya")
print(a)
print(my_dict)
my_set={1,"Яблоко",42.314,1,1,1,1}
print (my_set)
my_set.add(2)
my_set.add("Masha")
my_set.remove(1)
print (my_set)

