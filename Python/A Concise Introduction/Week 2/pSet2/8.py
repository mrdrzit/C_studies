def problem2_8(temp_list):
    avg = 0
    max_ = max(temp_list)
    min_ = min(temp_list)
    for temps in range(0,len(temp_list)):
        avg = avg + temp_list[temps]
    avg = avg/len(temp_list)

    print("Average:",avg)
    print("High:",max_)
    print("Low:",min_)