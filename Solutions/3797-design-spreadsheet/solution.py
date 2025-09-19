class Spreadsheet:

    def __init__(self, rows: int):
        self.hash_table = {}

    def setCell(self, cell: str, value: int) -> None:
        self.hash_table[cell] = value

    def resetCell(self, cell: str) -> None:
        self.hash_table.pop(cell, None)

    def getValue(self, formula: str) -> int:
        result = 0
        for cell in formula[1:].split("+"):
            result += int(cell) if cell[0].isdigit() else self.hash_table.get(cell, 0)
        return result


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
