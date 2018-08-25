#!/usr/bin/python

import blingcoin

import blingcoin.wallets
import blingcoin.transactions


commands = {'q':'quit', 'h':'help', 'b':'broadcast', 't':'transaction', 'i':'information'}
running = True

if __name__ == "__main__":

	blingcoin.network.startNetworking()
	blingcoin.miner.startMining()
	
	while running:

		try:
		
			ui = raw_input("> ")

			if ui == 'q':
				break

			if ui == 'h':
				for c in commands:
					print "%s: %s" % (c, commands[c])

			if ui == 't':
				to = raw_input("To: ")
				amount = raw_input("Amount: ")
				blingcoin.transactions.createTransaction(to, amount)

			if ui == 'i':
				blingcoin.wallets.printBasicInfo()

			if ui == 'b':
				blingcoin.network.broadcastSync()

		except KeyboardInterrupt:
			print "Exiting ..."
			running = False
			break
				
		except Exception as e:
			print "Exception in main: " + e.message
			break

	blingcoin.network.stopServer = True
	blingcoin.miner.stopMiner = True
	blingcoin.threader.waitForThreads()
