class Students:
    def __init__(self, name, surname, count_fail):
        self.__name = name
        self.__surname = surname
        self.__count_fail = count_fail

    def write_tests(self):
        if self.__count_fail < 2:
            print("Какой молодец, до армии ему пока что далеко:(")
        else:
            print("К сожалению, отчислен! ВПЕРЕД! Армия!")

    def write_name(self):
        print(self.__name, self.__surname)

