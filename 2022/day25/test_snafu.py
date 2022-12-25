def snafu_to_decimal(snafu_number):
    decimal = 0
    for index, c in enumerate(snafu_number):
        pos = (len(snafu_number) - index) - 1
        if c == '2':
            decimal += 5**pos * 2
        elif c == '1':
            decimal += 5**pos
        elif c == '0':
            continue
        elif c == '=':
            decimal -= 5**pos * 2
        elif c == '-':
            decimal -= 5**pos
    return decimal


def decimal_to_snafu(decimal):
    encode = '012=-'
    res = ''
    while decimal:
        res += encode[decimal % 5]
        if decimal > 2:
            decimal += 2
        decimal //= 5
    return res[::-1]

    # max_pos = 0
    # while True:
    #     value = 5**max_pos
    #     if decimal <= value:
    #         break
    #     value = 5**max_pos * 2
    #     if decimal <= value:
    #         break
    #     max_pos += 1

    # snafu = ''
    # for pos in range(max_pos, -1, -1):
    #     value = 5**pos * 2
    #     if decimal >= value:
    #         snafu += '2'
    #         decimal -= value
    #         break
    #     if decimal >= (value - 2):
    #         snafu += '='
    #         decimal -= value
    #         break
    #     if decimal >= (value - 1):
    #         snafu += '-'
    #         decimal -= value
    #         break
    #     value = 5**pos
    #     if decimal >= value:
    #         snafu += '1'
    #         decimal -= value
    #         break
    #     if decimal >= (value - 2):
    #         snafu += '='
    #         decimal -= value
    #         break
    #     if decimal >= (value - 1):
    #         snafu += '-'
    #         decimal -= value
    #         break
    #     snafu += '1'
    #     decimal -= value

    # return snafu


def test_snafu0():
    assert snafu_to_decimal('1') == 1
    assert decimal_to_snafu(1) == '1'


def test_snafu1():
    assert snafu_to_decimal('2') == 2
    assert decimal_to_snafu(2) == '2'


def test_snafu2():
    assert snafu_to_decimal('1=') == 3
    assert decimal_to_snafu(3) == '1='


def test_snafu3():
    assert snafu_to_decimal('1-') == 4
    assert decimal_to_snafu(4) == '1-'


def test_snafu4():
    assert snafu_to_decimal('10') == 5
    assert decimal_to_snafu(5) == '10'


def test_snafu5():
    assert snafu_to_decimal('11') == 6
    assert decimal_to_snafu(6) == '11'


def test_snafu6():
    assert snafu_to_decimal('12') == 7
    assert decimal_to_snafu(7) == '12'


def test_snafu7():
    assert snafu_to_decimal('2=') == 8
    assert decimal_to_snafu(8) == '2='


def test_snafu8():
    assert snafu_to_decimal('2-') == 9
    assert decimal_to_snafu(9) == '2-'


def test_snafu9():
    assert snafu_to_decimal('20') == 10
    assert decimal_to_snafu(10) == '20'


def test_snafu10():
    assert snafu_to_decimal('1=0') == 15
    assert decimal_to_snafu(15) == '1=0'


def test_snafu11():
    assert snafu_to_decimal('1-0') == 20
    assert decimal_to_snafu(20) == '1-0'


def test_snafu12():
    assert snafu_to_decimal('1=11-2') == 2022
    assert decimal_to_snafu(2022) == '1=11-2'


def test_snafu13():
    assert snafu_to_decimal('1-0---0') == 12345
    assert decimal_to_snafu(12345) == '1-0---0'


def test_snafu14():
    assert snafu_to_decimal('1121-1110-1=0') == 314159265
    assert decimal_to_snafu(314159265) == '1121-1110-1=0'
