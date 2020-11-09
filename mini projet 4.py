import sqlite3
conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

datas = [
(1,'George','Orwell',1674635417,'Georgeorwell@gmail.com','ami'),
(2,'Dune','Herbert',1657532413,'Duneherbert@gmail.com','ami'),
(3,'Fred','Asimov',1619514568,'Fredasimov@gmail.com','frère'),
(4,'Luc','Huxley',1619314698,'Luchuxley@gmail.com','ami'),
(5,'Frank','Bradbury',1619536435,'Frankbradbury@gmail.com','cousin'),
(6,'Ursus','K.Dick',1657387625,'Ursusk-dick@gmail.com','collegue'),
(7,'Cris','Bradbury',1619506753,'Crisbradbury@gmail.com','tonton'),
(8,'Lea','Barjavel',1619685690,'Leabarjavel@gmail.com','ami'),
(9,'Brice','K.Dick',1619684671,'Bricek-dick@gmail.com','collegue'),
(10,'Lance','Asimov',1619506745,'Lanceasimov@gmail.com','frère')
]

print("dans la base de données annuaires")
print("1.insertion")
print("2.suppression")
print("3.modification")
print("4.recherche")
print("5.fin du programme")
print("Quelle est votre choix?")
if print(1):
    cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRES(id INT, nom TEXT, prénom TEXT, téléphone INT, email TEXT, qualité TEXT)")
    cur.executemany("INSERT INTO ANNUAIRES (id, nom, prénom, téléphone, email, qualité) VALUES (?, ?, ?, ?, ?, ?)", datas)
    conn.commit()
    cur.close()
    conn.close()

if print(2):
    suppr = ('George',)
    cur.execute('DELETE FROM LIVRES WHERE nom = ?', suppr)
    conn.commit()
    cur.close()
    conn.close()


if print(3):
    modif = ('cousin', 'Cris')
    cur.execute('UPDATE LIVRES SET qualité = ? WHERE nom = ?', modif)
    conn.commit()
    cur.close()
    conn.close()
    
if print(4):
    recherche = ('Barjavel', 'ami')
    cur.execute('SELECT titre FROM LIVRES WHERE nom < ? AND qualité > ?', recherche)
    conn.commit()
    cur.close()
    conn.close()
    
if print(5):
    cur.close()
    conn.close()


