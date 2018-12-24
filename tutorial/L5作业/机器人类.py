class Robot():
    population = 0

    def __del__(self,name):
        self.name = name
        Robot.Population += 1

    def say_hi(self):
        print('大家好,我是{}'.format(self.name))

    #1 类方法装饰器
    @classmethod
    def how_many(cls):
        print('目前总人数',cls.population)

    # 2 静态方法装饰器
    # @staticmethod
    # def how_many():
    #     print('目前总人数',Robot.population)

    # 3对象方法。   不推荐这种写法
    # def how_many(self):    不推荐这种写法
    #     print('目前总人数',)