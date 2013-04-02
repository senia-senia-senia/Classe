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
class OtherWear(DefaultWear):
    pass

print('''выбирай:
        1 - Повседневный стиль
        2 - Спортивный стиль
        3 - Другое''')    
Your_wear = input()
Your_wear = int(Your_wear)
if Your_wear == 1:
    Your_wear = CasualWear()
elif Your_wear == 2:
    Your_wear = SportWear()
elif Your_wear == 3:
    print('''Это специальный раздел, здесь ты сможешь выбрать себе нужную
    одежду''')
    Your_wear = OtherWear()
    print('Напиши, какую обувь ты хочешь надеть:')
    Your_wear.shoeses = input()
    print('Напиши, что ты хочешь одеть на ноги:')
    Your_wear.In_feet = input()
    print('А теперь напиши, что хочешь одеть на тело:')
    Your_wear.In_body = input()
print('Сегодня ты наденешь',Your_wear.shoeses, Your_wear.In_feet, Your_wear.In_body )
print('''Хочешь поменять свою одежду в ручную?
    1 - Да
    2 - Нет''')
Your_choice = int(input())
while Your_choice == 1:
    print('''Хочешь ли ты поменять:
        1 - обувь
        2 - одежду на ноги
        3 - одежду на тело''')
    Change = input()
    Change = int(Change)
    if Change == 1:
        print('меняешь', Your_wear.shoeses, 'на:')
        Your_wear.new_shoeses = input()
        Your_wear.shoeses = Your_wear.new_shoeses
    elif Change == 2:
        print('меняешь', Your_wear.In_feet, 'на:')
        Your_wear.new_In_feet = input()
        Your_wear.In_feet = Your_wear.new_In_feet
    elif Change == 3:
        print('меняешь', Your_wear.In_body, 'на:')
        Your_wear.new_In_body = input()
        Your_wear.In_body = Your_wear.new_In_body
    print('''Хочещь еще что-нибудь поменять?
        1 - Да
        2 - Нет''')
    Your_choice = int(input())

print('Да ты неплохо одет!',Your_wear.shoeses, Your_wear.In_feet, Your_wear.In_body )

