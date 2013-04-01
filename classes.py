class DefaultWear:
    shoeses = 'Ботинки'
    In_feet = 'Джинсы'
    In_body = 'Футболка'
    def New_wear(self, new_shoeses, new_In_feet,new_In_body ):
        self.new_shoeses = new_shoeses
        self.new_In_feet = new_In_feet
        self.new_In_body = new_In_body
class CasualWear(DefaultWear):
    shoeses = 'Кеды'
    In_feet = 'Джинсы'
    In_body = 'Кофта'
class SportWear(DefaultWear):
    shoeses = 'Кроссовки'
    In_feet = 'Шорты'
    In_body = 'Майка'
print('''выбирай:
        1 - Повседневный стиль
        2 - Спортивный стиль''')    
Your_wear = input()
