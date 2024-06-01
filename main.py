class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles

    def maintenance_needed(self):
        return self.mileage > 100000

    def reset_mileage(self):
        self.mileage = 0

car = Vehicle("Toyota", "Camry", 50000)
car.display_info()
car.drive(200)
car.display_info()
print(car.maintenance_needed())
car.reset_mileage()
print(car.mileage)










class Piece:
    def init(self, color, position):
        self.color = color
        self.position = position

    def move(self):
        pass

class Pawn(Piece):
    def move(self):
        print("Пішак: вперед на одне-два поля або по діагоналі вперед.")

class Rook(Piece):
    def move(self):
        print("Ладья: горизонтально або вертикально.")

class Knight(Piece):
    def move(self):
        print("Конь: форма «L»: два квадрати горизонтально або вертикально, потім один квадрат перпендикулярно.")

class Bishop(Piece):
    def move(self):
        print("Слон: по діагоналі.")

class Queen(Piece):
    def move(self):
        print("Ферзь: горизонтально, вертикально або діагонально.")

class King(Piece):
    def move(self):
        print("Король: одне поле в будь-якому напрямку.")

pieces = [
    Pawn("white", "A2"),
    Rook("black", "D4"),
    Knight("white", "G1"),
    Bishop("black", "E5"),
    Queen("white", "C3"),
    King("black", "H8")
]
for piece in pieces:
    piece.move()











import sqlite3
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL
                )''')
employees = [
    (1, 'John Doe', 'Manager', 50000),
    (2, 'Jane Smith', 'Developer', 60000),
    (3, 'Alice Johnson', 'Designer', 55000)
]

cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees)
conn.commit()
cursor.execute('SELECT * FROM employees')
for row in cursor.fetchall():
    print(row)
conn.close()
