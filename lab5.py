def stop_and_wait():
    n = int(input("Enter the total number of frames: "))
    i = 0
    while i != n:
        frame = int(input("Enter received frame: "))
        if frame == i + 1:
            print(f"Transmitting..... ACK to frame {frame}")
            i += 1
        else:
            print(f"Negative ACK.... to frame {i + 1}")

def go_back_n():
    n = int(input("Enter the total number of frames: "))
    size = int(input("Enter window size of frames: "))
    print("Sending frames ", end="")
    for j in range(size):
        print(j + 1, end=" ")
    
    for j in range(n):
        print(f"\nIs Frame {j + 1} received (1 or 0): ", end="")
        t = int(input())
        if t == 1:
            print(f"\nSending ACK to frame {j + 1}\nSliding window")
            print("In window ", end="")
            for k in range(j + 1, j + 1 + size):
                if k < n:
                    print(k + 1, end=" ")
        else:
            print("\nRetransmitting frames\t", end="")
            for m in range(j, j + size):
                if m < n:
                    print(m + 1, end=" ")
            j -= 1

def selective_repeat():
    n = int(input("Enter the total number of frames: "))
    print("Sending frames ", end="")
    for j in range(n):
        print(j + 1, end=" ")
    
    print("\nEnter the number of frames received: ")
    m = int(input())
    a = [0] * m
    print("Enter received frame: ")
    for i in range(m):
        a[i] = int(input())
    
    trigger = 0
    for i in range(n):
        trigger = 0
        for j in range(m):
            if i + 1 == a[j]:
                trigger = 1
        if trigger == 0:
            print(f"Retransmitting frame {i + 1}")
            a.append(i + 1)
    
    a.sort()
    print("\nSorting ", end="")
    for i in range(n):
        print(a[i], end=" ")

if __name__ == "__main__":
    while True:
        print("\nEnter 1. Stop And Wait protocol\n"
              "2. Go back N\n3. Selective repeat\n")
        val = int(input())
        if val == 1:
            stop_and_wait()
        elif val == 2:
            go_back_n()
        elif val == 3:
            selective_repeat()
        else:
            break
