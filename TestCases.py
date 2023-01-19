from Num import Num


def test_nums():
    val = Num()
    lst = [1, 2, 3, 4, 5, 6, 7]
    for a in lst:
        val.add(a)
    # print(val.m2, val.n, val.mu)
    # print("in test class")
    # print(val.mid(0), round(val.div(0)))
    return (1 == val.mid(0)) and (4.0 == round(val.div(0)))


test_nums()
