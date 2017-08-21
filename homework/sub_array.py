def count_sub_list(source_list, target_num):
    d = {}
    num_sum = 0
    count = 0
    d[0] = 1
    for num in source_list:
        num_sum += num
        if num_sum in d.keys():
            count = d[num_sum - target_num]

        d[num_sum] += 1

    print(count)


if __name__ == "__main__":
    l = [1, 1, 1, 1, 1]
    count_sub_list(l, 2)
