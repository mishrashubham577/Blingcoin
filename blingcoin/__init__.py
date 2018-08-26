import databasing, mining, networks, eccs, encodings, networks, threads
from hashlib import sha256

db 				= databasing.blingDB()
miner			= mining.blingcoinMiner()
network 		= networks.blingcoinNetwork()

ecc 			= eccs.ellipticCurve()
hasher 			= sha256
encoder 		= encodings.b58encoder()
threader 		= threads.blingcoinThreader()


from os.path import isfile
if not isfile(db.dbFile):
	db.createDB()