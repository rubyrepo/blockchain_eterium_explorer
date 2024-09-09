import web3
from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)

# eth = "HTTP://127.0.0.1:7545"

eth = 'https://sepolia.infura.io/v3/09d360f6341c4b3987c24f8d53dd7618'


w3 = Web3(web3.HTTPProvider(eth))

def get_blockchain_info():
    latest_block_number = w3.eth.block_number
    connection_status = w3.isConnected()
    latest_block = w3.eth.get_block('latest')

    return latest_block_number, connection_status, latest_block

def get_latest_transaction_hash(input_text):
    transaction = w3.eth.get_transaction(input_text)
    return transaction


@app.route("/")
def index():
    try:
        latest_block_number, connection_status, latest_block = get_blockchain_info()
    except:
        latest_block_number, connection_status, latest_block = None, False, 0

    print(latest_block_number)
    print(connection_status)
    print(latest_block)
    return render_template('index.html', block=latest_block_number, connection = connection_status, latest_block = latest_block)

@app.route("/process_form", methods = ['POST'])
def process_form():

    input_text = request.form.get('inputField')

    input_text = str(input_text)

    try:
        transaction = get_latest_transaction_hash(input_text)

    except:
        transaction = None

    print("This is the transaction!")

    print(transaction)

    return render_template('index_02.html', input = transaction)

if __name__ == '__main__':
    app.run(debug=True)