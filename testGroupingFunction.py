def grouping(total, gn):
    for i in range(1, total+1):
        for j in range(0, gn + 1):
            if i % gn == j:
                print(i, ", G", j)
grouping(10, 5)