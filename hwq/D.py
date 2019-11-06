def reorder_list(v, cols):
    new = [0 for i in range(len(v))]
    h = len(v) // cols
    num_big = len(v) % cols
    
    for i in range(len(v)):
        if i <= (h + 1) * num_big:
            n_new = i // (h + 1) + cols * (i % (h + 1))
        else:
            k = num_big + (i - (h + 1) * num_big) // h
            r = i - num_big * (h + 1) - (k - num_big) * h
            n_new = k + r * cols
        new[n_new] = v[i]
    return new