import blingcoin.wallets
import blingcoin.transactions
import sqlite3
import threading


blingCOIN_DB_TEMPLATE = 'blingcoinBase.sql'
blingCOIN_DB_FILE = 'blingcoin.db'


class blingDB(object):
	""" blingcoin database class """

	def __init__(self, dbFile = blingCOIN_DB_FILE):
		
		self.dbFile = dbFile
		self.dblock = threading.Lock()

	def doQuery(self, query, args=False, result='all'):
		''' Perform a thread-safe query on the database '''

		self.dblock.acquire()

		self.conn = sqlite3.connect(self.dbFile)
		self.cursor = self.conn.cursor()

		if args:
			self.cursor.execute(query, args)
		else:
			self.cursor.execute(query)

		res = ''
		if result == 'all':
			res = blingcoin.db.cursor.fetchall()
		if result == 'one':
			res = blingcoin.db.cursor.fetchone()

		self.conn.commit()
		self.conn.close()

		self.dblock.release()

		return res


	def createDB(self):
		''' Create database from template and create wallet '''

		# maak db met genesis transaction en wallet
		sql = open(blingCOIN_DB_TEMPLATE,'r').read() 
		tmpConn = sqlite3.connect(self.dbFile)
		tmpCursor = tmpConn.cursor()
		tmpCursor.executescript(sql)
		tmpConn.commit()
		tmpConn.close()

		blingcoin.wallets.createNewWallet()