"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def start_auction(self, price):
        self._highest_bid = price
        self._notify_bidders()

    def get_cur_bidder(self):
        return self._highest_bidder

    def get_bid_amt(self):
        return self._highest_bid

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = list()
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            bidder(self)

    def accept_bid(self, bid, bidder="Starting Bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        self._highest_bid = bid
        self._highest_bidder = bidder
        self._notify_bidders()


class Bidder:
    """
    Bidders are the observers in the auction. These implement the __call__(auctioneer) protocol
    """

    def __init__(self, name, money=100, threat_chance=0.35, bid_increase=1.1):
        self.name = name
        self.bid_probability = threat_chance
        self.budget = money
        self.bid_increase = bid_increase
        self.highest_bid = 0

    def __call__(self, auctioneer):
        cur_bidder = auctioneer.get_cur_bidder()
        if cur_bidder is None:
            cur_bidder = 'Starting bid'
        bid_amt = auctioneer.get_bid_amt()
        c1 = cur_bidder != self
        new_bid_amt = auctioneer.get_bid_amt() * self.bid_increase
        c2 = new_bid_amt < self.budget
        c3 = random.random() <= self.bid_probability

        if c1 and c2 and c3:
            print("%s bidded %.2f in response to %s's bid of %.2f" % (self.name, new_bid_amt, cur_bidder, bid_amt))
            self.highest_bid = new_bid_amt
            auctioneer.accept_bid(new_bid_amt, self)

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.bidders = bidders
        self.item = ''
        self.price = 0

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        self.item = item
        self.price = start_price
        print(f'Auctioning {self.item} starting at {self.price}')

        a1 = Auctioneer()

        for bidder in self.bidders:
            a1.register_bidder(bidder)

        a1.start_auction(self.price)
        winner = a1.get_cur_bidder()
        amt = a1.get_bid_amt()

        print(f'\nThe winner of the auction is : {winner} at ${amt}')

        bidders_summary = {i:i.highest_bid for i in a1.bidders}

        print('Highest bids per Bidder')
        for i in bidders_summary:
            print(f'Bidder {i}\tHighest Bid: {bidders_summary[i]}')


def main():
    bidders = [Bidder("Jojo", 3000, random.random(), 1.2), Bidder("Melissa", 7000, random.random(), 1.5),
               Bidder("Priya", 15000, random.random(), 1.1), Bidder("Kewei", 800, random.random(), 1.9),
               Bidder("Scott", 4000, random.random(), 2)]

    # Hard coding the bidders.

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)


def user_input():
    item = input('Enter the item name')
    start_price = float(input('Enter the price'))
    choice = True
    bidders = list()

    while choice:
        print('Register new User:')
        name = input('Enter bidder name')
        budget = float(input('Enter bidder budget'))
        perc = float(input("Enter bidder's bid increase percent"))
        bidders.append(Bidder(name, budget, random.random(), perc))

        temp = int(input('1) Add new user\n2) Start auction'))
        choice = True if temp == 1 else 0

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction(item, start_price)


if __name__ == '__main__':
    # main()
    user_input()

