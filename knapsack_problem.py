def knapsack_max_value(array, max_capacity):
    '''
    input:
     - a list of tuples of initial goods: [(weight_1, value_1), (weight_2, value_2), ...]
     - given capacity of the knapsack
    output:
     - a list of goods, maximizing the total value of knapsack, not exceeding max_capacity restriction
    '''
    weights = [x[0] for x in array]
    values = [x[1] for x in array]
    goods_count = len(array)
    # create a matrix of first_goods by indexes in rows and max_capacities of hypotetical knapsacks limited my max_capacity
    # initialize it with zeroes
    values_matrix = [[0 for col in range(max_capacity + 1)] for row in range(goods_count + 1)]
    for k in range(1, goods_count + 1):
        for s in range (1, max_capacity + 1):
            if s >= weights[k - 1]:
                values_matrix[k][s] = max(values_matrix[k - 1][s], values_matrix[k - 1][s - weights[k - 1]] + values[k - 1])
            else:
                values_matrix[k][s] = values_matrix[k - 1][s]
    # create an array of best items
    items = []
    def get_items(k, s):
        if values_matrix[k][s] == 0:
            return
        if values_matrix[k - 1][s] == values_matrix[k][s]:
            get_items(k - 1, s)
        else:
            get_items(k - 1, s - weights[k - 1])
            items.append(array[k - 1])
    get_items(goods_count, max_capacity)
    return items

# a list of goods (weight, value)
goods_matrix = [(3, 1), (4, 6), (5, 4), (8, 7), (9, 6)]

print(knapsack_max_value(goods_matrix, 13))