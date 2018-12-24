class People():
    def __init__(self,name,race,orighn,height,weight):
        self.name = name
        self.race = race
        self.orighn = orighn
        self.height = height
        self.weight = weight

    # def print_race(self):
    #     print('{}的人种是{}'.format(self.name,self.race))
    #
    # def print_orighn(self):
    #     print('{}的国家是{}'.format(self.name,self.orighn))
    #
    # def print_height(self):
    #     print('{}的身高是{}'.format(self.name,self.height))
    #
    # def print_weight(self):
    #     print('{}的体重是{}'.format(self.name,self.weight))
    def print_into(self):
        print('我叫{},我是{},我来自{}，身高{}，体重{}'.format(self.name,self.orighn,self.height,self.weight))

xiaoming = People('小明','黄种人','中国',180,70)
alice = People('Alice','白种人','美国',160,50)

xiaoming.print_into()
alice.print_into()





