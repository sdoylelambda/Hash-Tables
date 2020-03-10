import random

def how_many_before_collisions(buckets, loops=1):
    # roll random hashes indexes into buckets and p[rint how many rolls before  a collision
    # run loops times

    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1

            else:
                # we have collision
                break
        #                                                                                   1 decimal format
        print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f}%")

how_many_before_collisions(1000, 1)