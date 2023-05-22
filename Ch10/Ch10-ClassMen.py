##Class에 메서드 정의 및 사용
class Men:
    def __init__(self, value):
        self.id = value
        self.name = None
        self.sex = None
        self.age = None

    def set_men(self, name, sex=None, age=None):
        self.name = name
        self.sex = sex
        self.age = age

    def get_men(self):
        id = self.id
        name = self.name
        sex = self.sex
        age = self.age
        return (id, name, sex, age)

men1 = Men('101')
print(men1.id)
men1.set_men(name='Kims', age=22, sex='F')
men1.get_men()
id, name, sex, age = men1.get_men()
print(id, name, sex, age)