![](https://i.imgur.com/IysZgy8.png#center)

# Blingcoin
 
Blingcoin is a very basic blockchain-free cryptocurrency PoC in Python. It's a project for discovering cryptocurrencies.

Note that this is a PoC that runs only on local networks and does not provide proper security. The code should only be used to get familiar with the building blocks for a cryptocurrency.

This project was created as an exercise after reading "Mastering Bitcoin: unlocking digital cryptocurrencies".

## Project's purpose

The purpose of this project is to have people learn about the basic workings of a cryptocurrency. I've tried to create a simple-as-possible framework to play with. The current code allows nodes to exchange coins on a local network.  

In its current state the application does not handle consensus forks. Also, you can perform some double-spending attacks and easily out-mine other nodes. No smart transaction confirmation graphing is implemented to outwit blockchain implementations. However, this is the whole point. These methods are not implemented, but because the code is so simple you can easily try out ideas to see how and if they work. Thus, I hope that the project can be an addition to both complete beginners in the field of cryptocurrencies as well as researchers or advanced coders that want to test new ideas. 

## Usage

The following steps will allow you to run the code on the local network and spend coins.

#### 1. Run generateGenesis.py

We're going to need the code:

```
git clone https://github.com/mishub/blingcoin.git
cd blingcoin
```

Then you `python generateGenesis.py`. This will show you something like the following:

```
Private key:
    17761749377588078293913083910285222277328633594463995997908039960139540655010
Compressed public key:
    blingmHmF8qgic2re7yECUEtg1147v8FDycvQtC15cE7dQYPh
Address:
    blingcyggS8jAJvm7qgiX25L1aRGbhrRfbyLDcZVdqegUbS2DY
```

What you're seeing here is the base for a wallet. There is a private key, a compressed public key, and an address. We'll change the code such that the genesis transaction is transferred to your wallet, so you can spend the coins. In this example, I'll use the above values.

#### 2. Change the database template

The first time you run blingcoin.py, a database is generated from the template blingcoinBase.sql. This file holds the genesis transaction, which is the first transaction for the currency. This transaction creates coins from thin air, and transfers then to an account.

Go ahead and open blingcoinBase.sql. There is one line that looks like this:

`INSERT INTO transactions_outputs (id,amount,address,outputHash,transactionHash) VALUES (1,31337,'blingcoint3wMFeUjEyrNMRjUR3Y8wm2LopaQmy3PRjaKyWceN',.......`

This is the genesis transaction, that transfers 31337 coins to address blingcoint3wMFe... Change this address to the address generated with generateGenesis.py. So in this example, I change:

`blingcoint3wMFeUjEyrNMRjUR3Y8wm2LopaQmy3PRjaKyWceN`

to:

`blingcyggS8jAJvm7qgiX25L1aRGbhrRfbyLDcZVdqegUbS2DY`

If you ran blingcoin.py before, make sure you delete blingcoin.db after doing this edit.

#### 3. Fix your wallet

Do a `python blingcoin.py`. This will create the database and a random wallet. Now type `i`. You should see a wallet with no coins. Now type `q` to quit, and wait for it to quit.

Now, with blingcoin shut down, open blingcoin.db (the database) with an sqlite database editor. You can use a GUI tool for this or just `sqlite3`. On OS X I like to use a tool called DB Browser.
Browse to the table called wallets, and change the private key, public key and address to the values you generated with generateGenesis.py. Save the database, close the tool.

Now if everything went well, you can `python blingcoin.py`, and if you type `i` you should see that your wallet now contains 31337 coins. Neat.

#### 4. Exchange code

Make a copy of the blingcoin directory, and remove the blingcoin.db file from the copy. We'll use this copied directory on other nodes, so let's call this the public directory. You can rename it to blingcoinPub if you like. Now copy this public directory to another node on the network.

I'll refer to our main node (that holds the genesis private key) as node A, and the other node we just copied the public directory to node B.

On node B, just `python blingcoin.py` from the public directory. If you then type `i`, you should see a generated wallet address for B.

On node A, type `t` to make a transaction.
At `To: ` you enter the wallet address for node B. At `Amount: ` just enter a small number like 137.
Now if you press `i` on both nodes, you should see that the coins are transferred. Sometimes you need to type `b` on node B to sync the two.

You can now transfer coins from device A to device B and back as mentioned in the screenshots.
![](https://i.imgur.com/IysZgy8.png)![](https://i.imgur.com/de21Vqq.png)

## Common problems

- UDP is chosen to send transactions and such, because it doesn't take a lot of code. These packets have a maximum length of about 500 bytes. After that, you'll have to fragment packets, which kind of sucks. This is why zlib compression is used.  
- Don't forget to wait for the threads to end when you shut down blingcoin (`q` or CTRL-c).
- blingcoin only works on the local network because of UDP broadcasts, but you also need an internet connection or else the method `getLocalIP` will fail.
