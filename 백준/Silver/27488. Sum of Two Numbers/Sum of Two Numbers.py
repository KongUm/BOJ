T = int(input())

for _ in range(T):

    N = int(input())

    s = str(N)

    ans1, ans2 = "", ""

    checker = True

    

    for i in s:

        i = int(i)

        if i == 1:

            if checker:

                ans1 += "1"

                ans2 += "0"

                checker = False

            else:

                ans1 += "0"

                ans2 += "1"

                checker = True

        else:

            d = i // 2

            if i % 2 == 0:

                ans1 += str(d)

                ans2 += str(d)

            else:

                if checker:

                    ans1 += str(i - d)

                    ans2 += str(d)

                    checker = False

                else:

                    ans1 += str(d)

                    ans2 += str(i - d)

                    checker = True

    ans1 = int(ans1)

    ans2 = int(ans2)

    print(ans1, ans2)                

            