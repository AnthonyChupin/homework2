class Cell():
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells
    def __sub__(self, other):
        if self.cells > other.cells:
         return self.cells - other.cells
        else: return ('Error')
    def __mul__(self, other):
        return self.cells * other.cells
    def __truediv__(self, other):
        return (round(self.cells // other.cells))
    def make_order(self, row): # принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
        self.row = row
        i = 0
        j = self.cells / row
        j2 = self.cells / j
        my_list = []
        i2 = 0
        while i < j:

            while i2 < j2:
                my_list.append('*')
                i2 += 1
            print(str(''.join(my_list)))
            i += 1



cells1 = Cell(15)
cells2 = Cell(10)
print(cells2 + cells1)
print(cells2 - cells1)
print(cells2 * cells1)
print(cells2 / cells1)
cells1.make_order(5)

