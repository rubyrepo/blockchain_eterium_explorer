import web3
from web3 import Web3

eth = "HTTP://127.0.0.1:8545"

w3 = Web3(web3.HTTPProvider(eth))

print(w3.isConnected())

def get_account_balance():
    address = input("Give me the account address: ")
    balance = w3.eth.get_balance(address)
    return balance

def get_account_balance_Ether(balance):
    ether_balance = w3.fromWei(balance,'ether')
    return ether_balance

def get_latest_transaction_hash(input_text):
    transaction = w3.eth.get_transaction(input_text)
    return transaction

def get_blockchain_info():
    latest_block_number = w3.eth.block_number
    connection_status = w3.isConnected()
    latest_block = w3.eth.get_block('latest')

    return latest_block_number, connection_status, latest_block

def get_latest_parent_hash():
    latest_block = w3.eth.get_block('latest')
    return latest_block['parentHash']




# balance = get_account_balance()
# print("This is the balance in wei: ")
# print(balance)
# print("This is the balance in ether:")
# print(get_account_balance_Ether(balance))


# 0x5fabc224ed7d214418818ed273c9206e8c8f58a0e315660c8aafd5591512e63e

# transaction = get_latest_transaction_hash(0x5fabc224ed7d214418818ed273c9206e8c8f58a0e315660c8aafd5591512e63e)
# print(transaction)
# latest_block_number, connection_status, latest_block = get_blockchain_info()
# print(latest_block_number)
# print("------------------------------------")
# print(connection_status)
# print("------------------------------------")
# print(latest_block)


print(get_latest_parent_hash())
