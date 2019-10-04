#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        if hash_table_retrieve(ht, limit - weights[i]) is not None:
            other_index = hash_table_retrieve(ht, limit - weights[i])
            return (i, other_index)

        hash_table_insert(ht, weights[i], i)
    return None


get_indices_of_item_weights([4, 4], 2, 8)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
