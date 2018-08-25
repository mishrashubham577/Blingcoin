#!/usr/bin/python

import blingcoin

import blingcoin.wallets
import blingcoin.transactions

#while 1:
privateKey, publicKey = blingcoin.wallets.blingcoin.ecc.make_keypair()
compressedPublicKey  = blingcoin.wallets.compressPublicKey(publicKey)
newAddress = blingcoin.wallets.publicKeyToAddress(compressedPublicKey)

#print newAddress[:9]
#if newAddress[:9] in coolAddressNames:
print "Private key:\n\t%s" % privateKey
#print publicKey
print "Compressed public key:\n\t%s" % compressedPublicKey
print "Address:\n\t%s" % newAddress
