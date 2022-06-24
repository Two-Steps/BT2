se = input('Nhập vào giá trị đầu và cuối, phân cách nhau bởi dấu cách: ')
se_list = se.split()
s = int(se_list[0])
e = int(se_list[1])
if s < e:
    for i in range(s,e+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
else:
    print('Giá trị cuối phải lớn hơn giá trị đầu')