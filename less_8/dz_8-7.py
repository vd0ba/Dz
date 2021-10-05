# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return f'{self.num_1 + other.num_1}+{self.num_2 + other.num_2}*i'

    def __mul__(self, other):
        return f'{self.num_1*other.num_1 - self.num_2 * other.num_2}+' \
               f'{self.num_1*other.num_2 + self.num_2 * other.num_1}*i'

    def __str__(self):
        return f'{self.num_1}+{self.num_2}*i'

numb_1 = ComplexNumber(4, 5)
numb_2 = ComplexNumber(7, 3)
print(numb_1 + numb_2)
print(numb_1 * numb_2)