import random

def longest_linked_list_chain(keys, buckets, loops=10):
    """roll keys number of keys into buckets number of random buckets and count collisions"""

    for i in range(loops):
        # dictionary pythongs implementation of a hashtable
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random) % buckets
            key_counts[hash_index] += 1

        largest_number = 0
        for key in key_counts:
            if key_counts[key] > largest_number:
                largest_number = key_counts[key]

        print(f"Longest Linked list chain for {keys} keys in {buckets} buckets (load factor: {keys/buckets:.2f}): {largest_number}")

longest_linked_list_chain(5, 100, 5)