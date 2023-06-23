"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        index = int(str(ord(string[0])) + str(ord(string[1])))
        self.table[index] = string
        # print(self.table[index]) => it works!
        

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = int(str(ord(string[0])) + str(ord(string[1])))
        return index if self.table[index] == string else -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return int(str(ord(string[0])) + str(ord(string[1])))

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
