def lenght_of_Collatz_sequence_x(x):  #dolžina zaporedja
    count = 1
    while True:
        if x == 1:
            break
        elif x % 2 == 0:
            b = x / 2
        elif x % 2 == 1:
            b = 3*x + 1
        x = b
        count += 1
    return count

def longest_Collatz_sequence_to_y(y):
    len_collatz = []
    i_ji = []
    for i in range(2, y+1):
        len_collatz.append(lenght_of_Collatz_sequence_x(i))
        i_ji.append(i)
    print("(dolžina zaporedja, začetno število)")
    return max(len_collatz), i_ji[len_collatz.index(max(len_collatz))]
