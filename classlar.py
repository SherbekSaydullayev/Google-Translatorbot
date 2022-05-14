import sqlite3
class Sql:
	def __init__(self):
		self.conn = sqlite3.connect("Translator.db")
		self.c = self.conn.cursor()
	def baza_create(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS info(
			id integer PRIMARY KEY,
			username varchar(60),
			first_name varchar(60)

			)""")
		return self.conn.commit()
	def user_add(self,idi,username,first_name):
		self.c.execute("INSERT INTO info VALUES({},'{}','{}')".format(idi,username,first_name))
		return self.conn.commit()
	def user_id(self,idi):
		self.c.execute(f"SELECT id FROM info WHERE id = {idi}")
		data = self.c.fetchone()
		return data

	def sana(self):
		self.c.execute("SELECT COUNT(id) FROM info")
		fo = self.c.fetchall()
		return fo
	def reklama(self):
		self.c.execute("SELECT * FROM info")
		rek = self.c.fetchall()
		return rek