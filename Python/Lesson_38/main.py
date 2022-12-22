class Operations:
    def print_to_terminal(self, *args):
        print(*args)

    def save_to_file(self, *args):
        with open("file.txt", "w") as file:
            file.write(str(*args))

    def reverse(self, *args):
        result = args[::-1]
        print(result)
        return result

    def get_max(self, *args):
        result = max(*args)
        print(result)
        return result

    def get_min(self, *args):
        result = max(*args)
        print(result)
        return result


class Choices:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def save(self, *args):
        if input("Write to file? [Y/N]") == "Y":
            self.strategy.save_to_file(*args)
        else:
            self.strategy.print_to_terminal(*args)

    def operation(self, *args):
        choice = input("Max, min or reverse? [max/min/rev]")
        if choice == "max":
            return self.strategy.get_max(*args)
        elif choice == "min":
            return self.strategy.get_min(*args)
        else:
            return self.strategy.reverse(*args)


obj = Choices()
obj.set_strategy(Operations())
with open("file.txt", "r") as file:
    data = file.read()
nums = obj.operation(data)
obj.save(nums)
