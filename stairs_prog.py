def Calculate(N, Index, Former, Current):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 3
    if Index == N:
        return Current
    else:
        Keeper = Former + Current
        Former = Current
        Current = Keeper
        return Calculate(N, Index + 1, Former, Keeper)


def main():
    N = int(input("enter number of stairs"))
    Index = 3
    Former = 2
    Current = 3
    FinalAnswer = Calculate(N, Index, Former, Current)
    print(FinalAnswer)


if __name__ == "__main__":
    main()
