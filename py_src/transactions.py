import requests
import json
import time
import datetime
from decimal import Decimal

def transactions(addr):
    url = "https://blockchain.info/rawaddr/"

    # # addr = "3BMEXyn3rFJwGH6tTVMgC9ERz8TdDhVLuv"

    resp = requests.get(url+addr)

    # time.sleep(2)
    data = resp.text

    # print(data)
    trxns = json.loads(data)
    # print(json.dumps(trxns["txs"][0], indent = 2))

    result = {}

    # iterating over all transactions
    for i in range(len(trxns["txs"])):
        inputs = []
        outputs = []

        hahs = trxns["txs"][i]["hash"]

        epoch_time = trxns["txs"][i]["time"]
        time_utc = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%d-%m-%Y %H:%M:%S')
        txn_time = time_utc + "+00:00 UTC"
        
        hahs = hahs + " \t date & time: " + txn_time

        temp = trxns["txs"][i]["inputs"]    

        # getting all inputs in the transaction
        for j in temp:
            value = Decimal(j["prev_out"]["value"]) / Decimal(100000000)
            if trxns["txs"][i]["fee"] != 0:
                if j["prev_out"]["addr"] == addr:
                    inputs.insert(0, f'{j["prev_out"]["addr"]} : {value}')
                else:
                    inputs.append(f'{j["prev_out"]["addr"]} : {value}')
            else:
                inputs.append(f'Newly Generated Coins, {value}')
        
        # getting all outputs in the transactions
        temp = trxns["txs"][i]["out"]
        for j in temp:
            value = Decimal(j["value"]) / Decimal(100000000)
            if j["addr"] == addr:
                outputs.insert(0, f'{j["addr"]} : {value}')
            else:
                outputs.append(f'{j["addr"]} : {value}')
        
        all_trxn = dict(input = inputs, out = outputs)
        result[hahs] = all_trxn
    
    # result = json.dumps(result)

    return result

# print(transactions("1FvzCLoTPGANNjWoUo6jUGuAG3wg1w4YjR"))
# trxns_in

# file = open("new.json", "w")
# file.write(json.dumps(transactions("1FvzCLoTPGANNjWoUo6jUGuAG3wg1w4YjR"), indent = 4))