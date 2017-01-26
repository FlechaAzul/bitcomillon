HASH_BITS = 64
HASH_MASK = 2**HASH_BITS - 1


def print_transactions(t):
    for i in range(len(t)):
        print "%064X %.8f (%.2f%%)" % (t[i][0], t[i][1], t[i][2] * 100)


def read_input():
    block_hash = long(raw_input(), 16) & HASH_MASK
    n_transactions = int(raw_input())
    transactions = []
    for _ in xrange(n_transactions):
        transaction = raw_input().split()
        transaction[0] = long(transaction[0], 16)
        transaction[1] = float(transaction[1])
        transactions.append(transaction)

    total = sum([t[1] for t in transactions])
    for i in range(len(transactions)):
        percentage = transactions[i][1] / total
        transactions[i].append(percentage)

    return (block_hash, transactions)


def draw_winner(block_hash, transactions):
    winner = 0
    start = 0
    for i in range(len(transactions)):
        end = start + int(HASH_MASK * transactions[i][2])
        if block_hash < end:
            winner = transactions[i][0]
            break
        start = end
    return winner


block_hash, transactions = read_input()
print "Using block hash %X" % (block_hash)
print_transactions(transactions)

winner = draw_winner(block_hash, transactions)
print "Winner: %064X" % (winner)
