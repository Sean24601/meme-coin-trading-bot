from solana.rpc.api import Client
from solana.transaction import Transaction
from base64 import b64decode
from solana.keypair import Keypair

# Initialize Solana client
client = Client("https://api.mainnet-beta.solana.com")

# Replace with your private key as a list of integers
private_key = [YOUR_PRIVATE_KEY_HERE]  # Replace with your Solana private key
keypair = Keypair.from_secret_key(bytes(private_key))

# Transaction details from GMGN API response
raw_tx_base64 = "AQAAAAAAAAAAAAAAAAAAA..."  # Replace with `swapTransaction` from GMGN response
recent_blockhash = "21AfWZnfQ1gQ5sHZkXSc2EZxfreeec17FtV2wPmsgjwR"  # Replace with the `recentBlockhash` from GMGN response

# Decode the raw transaction
raw_tx = b64decode(raw_tx_base64)
transaction = Transaction.deserialize(raw_tx)

# Update the blockhash and sign the transaction
transaction.recent_blockhash = recent_blockhash
transaction.sign(keypair)

# Send the transaction to the Solana blockchain
response = client.send_transaction(transaction, keypair)
print("Transaction Response:", response)
