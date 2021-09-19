class Canteen:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def branches(self):
        print("2")


class Items(Canteen):
    def food_items(self):
        print("The canteen name is:",self.name)
        print("The canteen phone number is:",self.number)
        dict1 = {"Puri": 20, "Chapati": 4, "Rice": 15, "Curd": 10}
        for i in dict1:
            print("Item is"+"\'"+i+"\'"+"and cost is", dict1[i])


class Branches(Items):
    def branches(self):
        print("4")
        """Here parent and  child classes have same method.
           in this situation this the way of calling parent
           methods
        """
        super().branches()


if __name__ == '__main__':
    desk1 = Items("Kaboor","99772")
    desk1.food_items()
    desk2 = Branches("love","98776")
    desk2.branches()
    