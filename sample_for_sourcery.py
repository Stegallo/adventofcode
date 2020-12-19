class Sample:
    def __init__(self):
        self.__input = 0

    def __iteration_function(self):
        if self.__input < 10:
            self.__input += 1

    def run(self, function):
        while True:
            before = str(self.__input)
            function()
            if before == str(self.__input):
                break

            print(self.__input)

    def main(self):
        self.run(self.__iteration_function)


s = Sample()
s.main()
print('END')
