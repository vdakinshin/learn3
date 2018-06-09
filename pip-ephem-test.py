import datetime
import ephem

today = datetime.date.today()
today = today.strftime('%Y/%m/%d')
#now = datetime.datetime.now()
#print('Сегодня {}' .format(today))
#print('Сейчас {}' .format(now))


mars_today = ephem.Mars(today)
constellation_of_mars_today = ephem.constellation(mars_today)
#print(constellation_at_date)

def ephem_const_today():
    user_input_planet = input('Введине название планеты: ')
    user_input_planet = str(user_input_planet)
    print(today)
    if user_input_planet == 'Mars':
        known_planet = ephem.Mars(today)
        constellation_of_known_planet_today = ephem.constellation(known_planet)
        return constellation_of_known_planet_today
    elif user_input_planet == 'Venus':
        known_planet = ephem.Venus(today)
        constellation_of_known_planet_today = ephem.constellation(known_planet)
        return constellation_of_known_planet_today
    else:
        return 'Такой планеты ({}) в базе не найдено' .format(user_input_planet)


if __name__ == '__main__':
    result = ephem_const_today()
    print(result)
