import sqlite3, litecli

connection = sqlite3.connect('testDB.db')
cursor = connection.cursor()

dataformytable = [('Chuwie', '200', 'flying, eating, dreaming', '1'),
                ('Luke', '18', 'fighting, digging', '1'),
                ('Ben Solo', '21', 'fightting, shouting', '0'),
                ('Kylo Ren', '21', 'fightting, shouting', '0'),
                ('Rey', '21', 'fighting, running', '1'),
                ('Snape', '38', 'protecting, teaching', '0'),
                ('Potter jr.', '30', 'wondering, wizarding', '1'),
                ('Lupin', '39', 'biting, running, scratching', '1'),
                ('Ged', '40', 'hunting, traveling', '0'),
                ('Ogion', '89', 'watching, reading', '0'),
                ('Lionel', '25', 'fightting, shouting', '1'),
                ('Marcy', '1008', 'playing, biting', '1'),
                ('Bubblegum', '1000', 'exploring, creating', '1'),
                ('Ludvig', '24', 'flying, eating, dreaming', '1'),
                ('Rosemary', '636', 'fighting, digging', '1'),
                ('Michele', '118', 'fightting, shouting', '0'),
                ('Helene', '42', 'fightting, shouting', '0'),
                ('Josh', '25', 'fighting, running', '1'),
                ('Swift', '67', 'protecting, teaching', '1'),
                ('Potter James', '11', 'wondering, wizarding', '0'),
                ('Lucy', '32', 'biting, running, scratching', '0'),
                ('Diamond', '34', 'hunting, traveling', '1'),
                ('Atuan', '34', 'watching, reading', '1'),
                ('Percy', '27', 'fightting, shouting', '1'),
                ('Fabricio', '28', 'playing, biting', '0'),
                ('Oomelawuluwati', '46', 'exploring, creating', '0'),
                ('T', '14', 'flying, eating, dreaming', '0'),
                ('Ekling', '100', 'fighting, digging', '0'),
                ('Ratsy', '237', 'fightting, shouting', '1'),
                ]

query = "INSERT into mytable values (?, ?, ?, ?)"

cursor.executemany(query, dataformytable)

connection.commit()