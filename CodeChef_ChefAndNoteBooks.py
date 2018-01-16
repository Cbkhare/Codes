from sys import stdin as si


if __name__ == "__main__":
    m = int(si.readline().strip())
    for i in range(m):
        x, y, k, n = map(int, si.readline().split())
        for j in range(n):
            p, c = map(int, si.readline().split())
            if p+y >= x and c <= k:
                print("LuckyChef")
                break
        else:
            print("UnluckyChef")
