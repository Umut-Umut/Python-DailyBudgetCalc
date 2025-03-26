import sqlite3

class DB:
    def __init__(self, name):
        self.name = name

    def create_table(self):
        conn = sqlite3.connect(f"{self.name}.db")
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.name} (id INTEGER PRIMARY KEY,int_value INTEGER,float_value1 REAL,float_value2 REAL)")
        conn.commit()
        conn.close()

    def insert_values(self, int_value, float_value1, float_value2 = 0):
        conn = sqlite3.connect(f"{self.name}.db")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {self.name} (int_value, float_value1, float_value2) VALUES (?, ?, ?)", 
                    (int_value, float_value1, float_value2))
        conn.commit()
        conn.close()

    def get_values(self):
        # if there is no db file then created it
        conn = sqlite3.connect(f"{self.name}.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT int_value, float_value1, float_value2 FROM {self.name} ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        return row

    def update_values(self, int_value, float_value1, float_value2 = 0):
        conn = sqlite3.connect(f"{self.name}.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {self.name} SET int_value = ?, float_value1 = ?, float_value2 = ? WHERE id = (SELECT id FROM {self.name} ORDER BY id DESC LIMIT 1)"
                       , (int_value, float_value1, float_value2))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # Kullanım
    db = DB()

    db.create_table("variables")  # Tabloyu oluştur
    db.insert_values(10, 20.5, 30.75)  # Değerleri kaydet
    print(db.get_values())  # Kaydedilen değerleri oku
    db.update_values(15, 25.5, 35.75)  # Değerleri güncelle
    print(db.get_values())  # Güncellenmiş değerleri oku
