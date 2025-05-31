import numpy as np

array1 = np.random.randint(1, 11, size=5)
array2 = np.random.randint(1, 11, size=5)
print("Перший масив:", array1)
print("Другий масив:", array2)
sum1 = np.sum(array1)
sum2 = np.sum(array2)
print("Сума елементів масиву 1:", sum1)
print("Сума елементів масиву 2:", sum2)

difference = array1 - array2
print("Різниця між масивами:", difference)

product = array1 * array2
print("Добуток елементів:", product)

power = np.power(array1, array2)
print("Піднесення array1 до ступеня array2:", power)

