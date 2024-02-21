def elect_next_budget_item(votes, balances, costs):
    # Calculate the satisfaction for each item
    satisfaction = {}
    for item, cost in costs.items():
        num_supporters = sum(1 for voter_votes in votes if item in voter_votes)
        satisfaction[item] = cost / num_supporters if num_supporters > 0 else float('inf')

    # Find the item with the lowest satisfaction (minimum budget needed per supporter)
    selected_item = min(satisfaction, key=satisfaction.get)
    min_budget_per_supporter = satisfaction[selected_item]
    print(f"To finance \"{selected_item}\", each supporter needs to contribute {min_budget_per_supporter:.2f}.")

    for i, voter_votes in enumerate(votes):
        balances[i] += min_budget_per_supporter
    # Update balances
    for i, voter_votes in enumerate(votes):
        if selected_item in voter_votes:
            balances[i] -= min_budget_per_supporter

    # Print remaining balances
    for i, balance in enumerate(balances):
        print(f"Citizen {i + 1} has {balance:.2f} remaining balance.")


# Example of using the modified algorithm
if __name__ == "__main__":
    # Define votes, balances, and costs
    votes = [["A", "B", "C", "D", "E"] for _ in range(51)] + [["F", "G", "H", "I", "J"] for _ in range(49)]
    balances = [0.0] * 100  # Set initial budget to 0 for each citizen
    costs = {"A": 100, "B": 100, "C": 100, "D": 100, "E": 100, "F": 100, "G": 100, "H": 100, "I": 100, "J": 100}

    # Call the function
    elect_next_budget_item(votes, balances, costs)
print()

votes1 = [["A", "B", "C", "D", "E"] for _ in range(70)] + [["F", "G", "H", "I", "J"] for _ in range(30)]
balances1 = [0.0] * 100  # Set initial budget to 0 for each citizen
costs1 = {"A": 100, "B": 100, "C": 100, "D": 100, "E": 100, "F": 100, "G": 100, "H": 100, "I": 100, "J": 100}

# Call the function
elect_next_budget_item(votes1, balances1, costs1)
