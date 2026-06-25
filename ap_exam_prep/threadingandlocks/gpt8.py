# NB2_18.py

import threading as tr, time, random

### Exercise 16 ##############################
# Context:
# A bank account is shared by many ATM threads.
#
# Each ATM receives a list of transactions.
# Positive numbers are deposits.
# Negative numbers are withdrawals.
#
# A withdrawal may only happen if the account has enough money.
# If there is not enough money, the withdrawal must be rejected.
#
# Your job is to fill in the BankAccount class.
#
# Requirements:
# - Multiple ATM threads must be able to use the same BankAccount object.
# - Deposits must always be accepted.
# - Withdrawals must only be accepted if there is enough money.
# - The account balance must never become negative.
# - Every accepted transaction must be recorded exactly once.
# - Every rejected transaction must be recorded exactly once.
# - The program must not run sequentially by joining after every thread starts.
#
# You may edit only the BankAccount class.
# Do not edit the tests.

class BankAccount:
    def __init__( self, starting_balance ):
        self.balance: int = starting_balance
      
        self.accepted = []
        self.rejected = []
        self.bank_account_lock = tr.Lock()
        #self.bank_event = tr.Event()
        
    

    def process_transaction( self, atm_id, transaction_id, amount ):
        # Fill in this method.
        with self.bank_account_lock:
            if amount <=0:
                if self.balance + amount >=0:
                    self.balance += amount
                    self.accepted.append((atm_id, transaction_id, amount))
                else:
                    self.rejected.append((atm_id, transaction_id, amount)    )      
            else:
                self.balance += amount
                self.accepted.append((atm_id, transaction_id, amount))
            
    

    def run_atm( self, atm_id, transactions ):
        # Fill in this method.
        for i in range(len(transactions)):
            self.process_transaction( atm_id=atm_id, transaction_id=i, amount= transactions[i] )

##############################################


### Tests ####################################

def run_test( starting_balance, all_transactions ):
    account = BankAccount( starting_balance )

    threads = [
        tr.Thread( target=account.run_atm, args=(atm_id, transactions) )
        for atm_id, transactions in enumerate( all_transactions )
    ]

    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    accepted_total = sum( amount for atm_id, transaction_id, amount in account.accepted )
    expected_balance = starting_balance + accepted_total

    assert account.balance == expected_balance, \
        f"Balance is wrong. Expected {expected_balance}, got {account.balance}"

    assert account.balance >= 0, \
        f"Balance became negative: {account.balance}"

    all_given_transactions = []
    for atm_id, transactions in enumerate( all_transactions ):
        for transaction_id, amount in enumerate( transactions ):
            all_given_transactions.append( (atm_id, transaction_id, amount) )

    recorded = account.accepted + account.rejected

    assert sorted( recorded ) == sorted( all_given_transactions ), \
        f"Some transactions were lost or duplicated. Recorded: {recorded}"

    seen = set()
    replay_balance = starting_balance

    for atm_id, transaction_id, amount in account.accepted:
        assert (atm_id, transaction_id) not in seen, \
            f"Transaction recorded twice: {(atm_id, transaction_id, amount)}"

        seen.add( (atm_id, transaction_id) )

        if amount < 0:
            replay_balance += amount
            assert replay_balance >= 0, \
                f"Accepted withdrawal should have been rejected: {(atm_id, transaction_id, amount)}"
        else:
            replay_balance += amount


if __name__ == "__main__":
    run_test(
        starting_balance=100,
        all_transactions=[
            [50, -20, -80, 10],
            [-30, 40, -90],
            [25, -10, -70]
        ]
    )

    run_test(
        starting_balance=0,
        all_transactions=[
            [100, -50, -70, 20],
            [-10, 80, -30],
            [60, -100, -5]
        ]
    )

    run_test(
        starting_balance=500,
        all_transactions=[
            [random.choice([25, 50, -10, -20, -75]) for _ in range(50)]
            for _ in range(8)
        ]
    )

    print( "All tests passed." )