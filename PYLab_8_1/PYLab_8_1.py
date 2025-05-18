import matplotlib.pyplot as plt
import numpy as np

Sp= { "СТ1": ("Сталь углеродист", 0.00154), "СК3": ("Стеклотекстолит", 0.0060), "GR7": ("Алюмин.лист ", 0.047), "ШС45": ("Шпоночн.Сталь", 0.046), "ПС6": ("Полистирол ", 0.078), "FP43": ("Фенопласт ", 0.054), "CS9": ("Цинковый сплав ", 0.0108), "ЛТ23": ("Лента латунная", 0.038)}

X = np.arange(0, 2.01, 0.01)
Y = -X * np.cos(X + 3) + 2.5

I = np.trapz(Y,X)
print("Площадь заготовки =", I)

num_of_blanks = 1600
code = str(input("Введите код интересующего материала: "))
quant_of_mat = num_of_blanks * Sp[code][1] * I

print("Код -", code, "\nНаименование -", Sp[code][0], "\nКоличество заготовок -", num_of_blanks, "\nКоличество материала -", quant_of_mat)

plt.figure()
plt.grid()
plt.fill_between(X,Y,"blue")
plt.show()

