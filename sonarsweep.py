def main():
    increased = 0
    curr_arr = [0, 0, 0]
    previous_sum = 10000000000000
    with open('ss_input.txt') as f:
        while True:
            data = f.readline();
            if data == "":
                break
            else:
                swap_data(curr_arr, data)
                if(curr_arr[0] != 0):
                    if arr_sum(curr_arr) > previous_sum:
                        increased = increased+1
            previous_sum = arr_sum(curr_arr)
    print("Increases: " + str(increased))

def swap_data(arr, data):
    one = arr[1]
    two = arr[2]
    arr[0] = one
    arr[1] = two
    arr[2] = int(data)

def arr_sum(a):
    sum = 0
    for x in a:
        sum = sum + x
    return sum
main()
