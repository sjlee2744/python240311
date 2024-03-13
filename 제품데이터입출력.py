import sqlite3

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                price REAL)''')
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        self.cursor.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)",
                            (product_id, name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cursor.execute("UPDATE products SET price = ? WHERE id = ?",
                            (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

# 데이터베이스 생성
db = ProductDatabase('products.db')

# 샘플 데이터 입력
sample_data = [
    (1, '스마트폰', 1000000),
    (2, '태블릿', 800000),
    (3, '노트북', 1500000),
    (4, '이어폰', 50000),
    (5, '스피커', 120000),
    (6, '마우스', 30000),
    (7, '키보드', 50000),
    (8, '헤드폰', 70000),
    (9, '모니터', 300000),
    (10, '카메라', 200000)
]

for data in sample_data:
    db.insert_product(*data)

# 데이터 출력
for i in range(1, 11):
    print(db.select_product(i))

# 제품 가격 업데이트
db.update_product_price(1, 1200000)

# 업데이트된 데이터 출력
print("업데이트 후:")
print(db.select_product(1))

# 제품 삭제
db.delete_product(10)

# 삭제된 데이터 출력
print("삭제 후:")
print(db.select_product(10))

