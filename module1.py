import module2

name = input("Введите имя студентика: ")
surname = input("Введите фамилию студентика: ")
count_fail = int(input("Введите количество незакрытых зачетов у студентика: "))

a = module2.Students(name, surname, count_fail)
a.write_name()
a.write_tests()
