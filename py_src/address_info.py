import requests
import json
import datetime
from decimal import Decimal


# address = "1FvzCLoTPGANNjWoUo6jUGuAG3wg1w4YjR"

def get_info(addrs):

    url = "https://blockchain.info/rawaddr/"
    resp = requests.get(url+addrs)

    data = json.loads(resp.text)
    info = {}
    info["Address"] = data["address"]
    info["hash160"] = data["hash160"]
    info["No of Transactions"] = data["n_tx"]
    info["Received"] = float(Decimal(data["total_received"]) / Decimal(100000000))
    info["Sent"] = float(Decimal(data["total_sent"]) / Decimal(100000000))
    info["Current Balance"] = float(Decimal(data["final_balance"]) / Decimal(100000000))

    latest = data["txs"][0]["time"]
    oldest = data["txs"][-1]["time"]

    latest_time = datetime.datetime.utcfromtimestamp(latest).strftime('%d-%m-%Y %H:%M:%S')
    oldest_time = datetime.datetime.utcfromtimestamp(oldest).strftime('%d-%m-%Y %H:%M:%S')

    info["Last Transaction on"] = f'{latest_time}+00:00 UTC'
    info["First Transaction on"] = f'{oldest_time}+00:00 UTC'

    return info


# url = "https://blockchain.info/rawaddr/"
# response = requests.get(url+address)
# temp = response.text
# data = json.loads(temp)

# print(get_info(data))