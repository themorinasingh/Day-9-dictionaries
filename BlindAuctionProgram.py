from hammer import hammer

auction_data = {}

while True:
    name = input("Enter Your Name: ").title()
    bid_value = float(input("Bid Amount: $"))

    auction_data[name] = bid_value

    more_people = input("Are there more people in line to place a bid?\n y/n: ").lower()

    if more_people == "y":
        print("\n" * 25)
        continue
    else:
        print("\n" * 25)
        break

max_bidder = ""
max_bid = 0

for bidder in auction_data:
    if auction_data[bidder] > max_bid:
        max_bidder = bidder
        max_bid = auction_data[bidder]

print(f"The winner is {max_bidder} with a bid of ${max_bid}")
