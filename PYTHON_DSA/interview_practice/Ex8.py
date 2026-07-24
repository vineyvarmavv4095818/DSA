
def solve(list):
    max_product = lst[0] * lst[1]

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i] * lst[j]

            if product > max_product:
                max_product = product

    return print("max product:", max_product)

lst = [1, 3, 6, 8, 2, 9]
solve(lst)