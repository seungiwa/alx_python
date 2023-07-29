import requests
from collections import defaultdict

# TronGrid API endpoint
url = "https://api.trongrid.io/v1/transactions"

# Define the time range for the past 60 days
import datetime
from_timestamp = int((datetime.datetime.now() - datetime.timedelta(days=60)).timestamp()) * 1000
to_timestamp = int(datetime.datetime.now().timestamp()) * 1000

# Dictionary to store address and their smart contract interactions
address_interactions = defaultdict(set)

# Query transactions in the given time range
params = {
    "only_confirmed": True,
    "limit": 100,  # Adjust the limit as per your needs
    "start_timestamp": from_timestamp,
    "end_timestamp": to_timestamp
}

response = requests.get(url, params=params)

# Process the transactions to count interactions for each address
if response.status_code == 200:
    data = response.json().get("data", [])
    for tx in data:
        from_address = tx.get("raw_data", {}).get("contract[0].parameter.value.owner_address")
        to_address = tx.get("raw_data", {}).get("contract[0].parameter.value.to_address")
        contract_address = tx.get("raw_data", {}).get("contract[0].parameter.value.contract_address")

        address_interactions[from_address].add(contract_address)
        address_interactions[to_address].add(contract_address)

# Sort addresses based on the number of unique smart contract interactions
sorted_addresses = sorted(address_interactions.items(), key=lambda x: len(x[1]), reverse=True)

# Get the top 20 addresses with diverse smart contract interactions
top_20_addresses = sorted_addresses[:20]

# Display the result
for idx, (address, interactions) in enumerate(top_20_addresses, 1):
    print(f"{idx}. Address: {address}")
    print("   Categorized Interactions:")
    for contract_address in interactions:
        print(f"     - {contract_address}")

