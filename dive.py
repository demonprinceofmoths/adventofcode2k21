def main():
    horizontal = 0
    depth = 0
    aim = 0
    with open('dive_input.txt') as f:
        while True:
            data = f.readline()
            if data == "":
                break
            else:
                line = data.split()
                #print(line[0])
                if line[0] == "forward":
                    horizontal = horizontal + int(line[1])
                    depth = depth + (aim * int(line[1]))
                elif line[0] == "up":
                    aim = aim - int(line[1])
                elif line[0] == "down":
                    aim = aim + int(line[1])
                else:
                    print("PANIC")
    return horizontal * depth
print(main())
