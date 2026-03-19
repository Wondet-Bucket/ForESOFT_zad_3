#Функция проверки соответствия количества открывающихся скобок закрывающимся.
#Быстрый поверхностный анализ
def check_pair_numbers(string):
    square_in = 0
    square_out = 0
    round_in = 0
    round_out = 0
    figure_in = 0
    figure_out = 0
    for char in string:
        if (char == '['):
            square_in+=1
        elif (char == '('):
            round_in+=1
        elif (char == '{'):
            figure_in+=1
        elif (char == ']'):
            square_out+=1
        elif (char == ')'):
            round_out+=1
        elif (char == '}'):
            figure_out+=1
        
    if (square_in == square_out and round_in == round_out and figure_in == figure_out):
        return True
    else:return False
#Функция превращения скобки в противоположную
def opposite_bracket(char):
    if (char == '['):
        return ']'
    elif (char == '('):
        return ')'
    elif (char == '{'):
        return '}'
#Функция глубокого анализа правильности строки
def check_inside(string):
    previos = ''
    this = ''
    char_history = []
    for char in string:
        #Если первая скобка закрывающаяся, то нет смысла дальше что-то проверять.
        #Можно сразу выдать False и закончить. При этом первая скобка не обязательно
        #Стоит в начале. Скобка считается первой, если до не было открытых скобок.
        if (len(char_history) == 0):
            if (char == '}' or char == ')' or char == ']'):
                return False
        #Программа основана на запоминании скобок, которые были.        
        char_history.append(char)
        last_opposite_char = opposite_bracket(char_history[len(char_history) - 2])
        #Сравнение текущей скобки с последней в истории
        if(char == last_opposite_char):
            #Если она является закрывающей для предыдущей, то из истории удаляется как текущая
            #Так и предыдущая скобка
            char_history.pop(len(char_history) - 1)
            char_history.pop(len(char_history) - 1)
#Если в конце работы не все скобки были закрыты, то история будет не пустая
    if (len(char_history) > 0):
        return False
#А если пустая, то строка правильная
    else: 
        return True
#Это общая функция, которая проверяет "правильность" входящей строки с помощью
#Поверхностного и глубокого анализа
def check_brackets(string):
    if (check_pair_numbers(string) == True):
        if(check_inside(string) == True):
            return(True)
    else: 
        return False 

# Работа программы - интерактив. Можно использовать функции и без этого,
# импортируя верхнюю часть кода. Но в данном случае принято решение сделать консольный
# интерфейс

print("Введите строку из скобок, которую необходимо проверить \n")
#Ввод пользователем строки
string = input()
#Экспресс-тест на лишние символы
for char in string:
    if (char == '[' or char == '(' or char == '{' or
    char == ']' or char == ')' or char == '}' ):
        pass
    else:
        print("\nОШИБКА!!! \nВаша последовательность содержит иные символы помимо скобок")
        quit()
# Использование функции проверки строки        
if (check_brackets(string)):
    print("Введенная вами строка - правильная")
else:
    print("Введенная вами строка - неправильная")