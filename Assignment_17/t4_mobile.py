import sqlite3
conn = sqlite3.connect("mobile.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE mobile (
        brand TEXT,
        name TEXT,
        year TEXT,
        camera TEXT,
        ram TEXT,
        memory TEXT,
        price TEXT
          )
""")

c.execute("""
CREATE TABLE laptop (
        brand TEXT,
        name TEXT,
        cpu TEXT,
        ram TEXT,
        hhd TEXT,
        ssd TEXT,
        os TEXT 
          )
""")

c.execute("INSERT INTO mobile VALUES ('Samsung', 'Galaxy a34', '2023', '48MP', '6GB', '128GB', '$300')")
c.execute("INSERT INTO mobile VALUES ('Samsung', 'Galaxy J8', '2018', '16MP', '4GB', '64GB', '$180')")
c.execute("INSERT INTO mobile VALUES ('Xiaomi', 'Redmi Note 12', '2022', '48MP', '8GB', '256GB', '$385'")
c.execute("INSERT INTO mobile VALUES (Apple), (Iphone 11), (2019), (12MP), (64GB), (128GB), ($750)")
c.execute("INSERT INTO mobile VALUES (Nothing Phone), (1), (2022), (50MP), (12GB), (256GB), ($470)")
c.execute("INSERT INTO mobile VALUES (Google), (Pixel Fold), (2023), (48MP), (12GB), (512GB), ($1800)")

c.execute("INSERT INTO laptop VALUES (Dell), (Inspiron 16), (Zen 3 Ryzen 5 7530U), (16GB), (None), (512GB), (Windows)")
c.execute("INSERT INTO laptop VALUES (Asus), (Vivobook 14X), (Intel Core i5-13500H), (16GB), (None), (512GB), (Windows)")
c.execute("INSERT INTO laptop VALUES (HP), (Dragonfly G4), (Intel Core i7-1365U), (16GB), (512GB), (512GB), (Windows)")
c.execute("INSERT INTO laptop VALUES (Lenovo), (IdeaPad Gaming Chromebook 16), (Intel Core i3-1215U), (8GB), (None), (256GB), (Windows)")
c.execute("INSERT INTO laptop VALUES (Apple), (MacBook Air 15 2023 M2), (3.8 GHz 8-core CPU), (8GB), (None), (512GB), (MacOs)")
c.execute("INSERT INTO laptop VALUES (Apple), (MacBook Air 2020 M1 Entry), (3.2 GHz 8-core CPU), (8GB), (None), (256GB), (MacOs)")
c.execute("INSERT INTO laptop VALUES (MSI), (Cyborg 15 A12VE), (Intel Core i7-13620H), (16GB), (None), (512GB), (Windows)")

conn.commit()
conn.close()
