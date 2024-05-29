# def convert_to_dollar(transacations):
#     for id, data in transactions.items():
#         data['amount_cents'] /= 100
#     return transactions
    
# def calculate_rewards(transcations):

#     rules = {
#         'sportchek': [ (500, 75), (300, 75) ]
#     }

#     data = convert_to_dollar(transcations)
#     print(data)
    

# transactions = {
#     'T1': {'date': '2021-05-09', 'merchant_code' : 'sportcheck', 'amount_cents': 2500},
#     'T2': {'date': '2021-05-10', 'merchant_code' : 'tim_hortons', 'amount_cents': 1000},
#     'T3': {'date': '2021-05-10', 'merchant_code' : 'the_bay', 'amount_cents': 500}
# }


# calculate_rewards(transactions)

def calculate_rewards(transactions):
    # Define the reward rules
    reward_rules = [
        {"points": 500, "sportcheck": 75, "tim_hortons": 25, "subway": 25},
        {"points": 300, "sportcheck": 75, "tim_hortons": 25, "subway": 0},
        {"points": 200, "sportcheck": 75, "tim_hortons": 0, "subway": 0},
        {"points": 150, "sportcheck": 25, "tim_hortons": 10, "subway": 10},
        {"points": 75,  "sportcheck": 25, "tim_hortons": 10, "subway": 0},
        {"points": 75,  "sportcheck": 20, "tim_hortons": 0, "subway": 0},
    ]
    
    # Convert transaction amounts to dollars
    for t in transactions:
        transactions[t]['amount_dollars'] = transactions[t]['amount_cents'] / 100

    # Function to apply rules and maximize points
    def apply_rules(transactions):
        # Points accumulator for all transactions
        transaction_points = {t: 0 for t in transactions}

        # Apply rules to maximize points
        for rule in reward_rules:
            for t, data in transactions.items():
                if data['amount_dollars'] <= 0:
                    continue
                applicable = True
                required_spends = {}
                
                if rule['sportcheck'] and data['merchant_code'] == 'sportcheck':
                    required_spends['sportcheck'] = rule['sportcheck']
                if rule['tim_hortons'] and data['merchant_code'] == 'tim_hortons':
                    required_spends['tim_hortons'] = rule['tim_hortons']
                if rule['subway'] and data['merchant_code'] == 'subway':
                    required_spends['subway'] = rule['subway']
                
                while applicable:
                    for key, value in required_spends.items():
                        if transactions[t]['amount_dollars'] < value:
                            applicable = False
                            break
                    if applicable:
                        transaction_points[t] += rule['points']
                        for key in required_spends:
                            transactions[t]['amount_dollars'] -= required_spends[key]
        
        # Apply remaining points at 1 point per $1 spent
        for t, data in transactions.items():
            transaction_points[t] += data['amount_dollars']
        
        return transaction_points

    # Calculate points for each transaction
    transaction_points = apply_rules(transactions)

    # Calculate the total points for the month
    total_points = sum(transaction_points.values())

    return total_points, transaction_points

# New transactions
transactions = {
    'T1': {'date': '2021-05-09', 'merchant_code': 'sportcheck', 'amount_cents': 2500},
    'T2': {'date': '2021-05-10', 'merchant_code': 'tim_hortons', 'amount_cents': 1000},
    'T3': {'date': '2021-05-10', 'merchant_code': 'the_bay', 'amount_cents': 500}
}

# Calculate the rewards
total_points, transaction_points = calculate_rewards(transactions)
print("Total Reward Points for the Month:", total_points)
print("Reward Points per Transaction:", transaction_points)

