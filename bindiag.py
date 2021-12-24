def main():
    gamma = ""
    epsilon = ""
    data_read = read_data();
    zero_crate = data_read[0]
    one_crate = data_read[1]
    for x in range(0, len(zero_crate)):
        if zero_crate[x] >= one_crate[x]:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        elif zero_crate[x] <= one_crate[x]:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def read_data():
    zero_crate = [0,0,0,0,0,0,0,0,0,0,0,0];
    one_crate = [0,0,0,0,0,0,0,0,0,0,0,0];
    with open("diag_input.txt") as f:
        while True:
            data = f.readline()
            if data == "":
                break
            else:
                for x in range(0, len(data)-1):
                    if int(data[x]) == 0:
                        zero_crate[x] = zero_crate[x]+1
                    elif int(data[x]) == 1:
                        one_crate[x] = one_crate[x]+1
                    else:
                        print("PANIC")
        return [zero_crate, one_crate]

print(main())
