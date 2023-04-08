class Worker:
    """Класс работника"""

    def _init_(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        """
        :param name: Имя работника
        :param surname: Фамилия работника
        :param position: Занимаемая должность
        :param wage: Оклад
        :param bonus: Премия
        """
        self.name = name
        self.surname = surname
        self.position = position

        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Класс позиции"""

    def get_full_name(self, reverse=False):
        """ Собирает полное имя для позиции в порядке 'заданном reverse
        :param reverse: порядок следования если False (по умолчанию) 'name surname'
         если True, то 'surname name'
        :return: Полное имя
        """
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        """ Вычисляет полный доход (оклад + премия)
        :return: Сумма оклада и премии
        """
        return sum(self._income.values())


if _name_ == '_main_':
    position_data = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'position': 'Scrum master',
            'wage': 40000,
            'bonus': 0
        },
        {
            'name': 'Petr',
            'surname': 'Petrov',
            'position': 'developer',
            'wage': 90000,
            'bonus': 60000
        },
        {
            'name': 'Irina',
            'surname': 'Ivanova',
            'position': 'service delivery manager',
            'wage': 60000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('#######################################')
        print('From data: ', item)
        print('Position name: ', position.name)
        print('Position surname: ', position.surname)
        print('Position full name: ', position.get_full_name())
        print('Position full name reverse: ', position.get_full_name(reverse=True))
        print('Position position: ', position.position)
        print('Position total income: ', position.get_total_income())
        print('#######################################\n\n')
