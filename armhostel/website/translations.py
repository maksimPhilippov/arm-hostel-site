russian = 'rus'
english = 'eng'
armenian = 'arm'

def translateBase(func):
    def translate(language):
        pageTranslation = func(language)
        baseTranslation = dict()
        if language == russian:
            baseTranslation = {
                    'home_nav': 'Главная',
                    'about_us_nav': 'О нас',
                    'book_nav': 'Забронировать',
                    'services_nav': 'Услуги',
                    'contact_nav': 'Контакты',
                }
        elif language == english:
            baseTranslation = {
                    'home_nav': 'Main',
                    'about_us_nav': 'About us',
                    'book_nav': 'Book',
                    'services_nav': 'Services',
                    'contact_nav': 'Contacts',
                }
        elif language == armenian:
            baseTranslation = {
                    'home_nav': 'Главная',
                    'about_us_nav': 'О нас',
                    'book_nav': 'Забронировать',
                    'services_nav': 'Услуги',
                    'contact_nav': 'Контакты',
                }
        baseTranslation.setdefault('language', language)
        pageTranslation.update(baseTranslation)
        
        return pageTranslation
    return translate

@translateBase
def translateAboutUs(language):
    if language == russian:
        return {
            'main_header': 'О нас',
            'about_englishus_text_p1': '''Arm Hostel расположен в Ереване, в 400 метрах от 
            Армянского театра оперы и балета. С балкона открывается вид на город.''',

            'about_us_text_p2': '''В числе удобств круглосуточная стойка регистрации и 
            общая кухня, большой балкон, отдельные и общие номера с кондиционером и  на 
            всей территории работает бесплатный Wi-Fi. В стоимость проживания в хостеле 
            Arm Hostel & Tours включено постельное белье, и полотенца также  можно 
            заказать экскурсии.''',

            'about_us_text_p3': '''Неподалеку от хостела Arm Hostel находятся такие 
            популярные достопримечательности, как Армянский театр оперы и балета, Музей 
            истории Армении и Северный проспект. Расстояние до международного аэропорта 
            Звартноц составляет 10 ,1 км.''',

            'conditions_header': 'Условия проживания',
            'conditions_item1': '''Заезд в 14:00, выезд в 12:00.''',
            'conditions_item2': '''Курение в отеле строго запрещено. Гости отеля могут 
            курить только в балконе.''',

            'conditions_item3': '''Алкоголь строго запрещён на всей территории.''',
            'conditions_item4': '''В отеле не допускается проживание вместе с 
            животными''',

            'rules_header': 'Правила и условия',
            'rules_content': '''В целях безопасности проживающих, а также по 
            законодательным предписаниям, при регистрации каждый гость должен 
            предъявить действительное удостоверение личности с фотографией 
            (паспорт или водительское удостоверение).''',
        }
    elif language == english:
        return {
            'main_header': 'About us',
            'about_us_text_p1': '''Arm Hostel is located in Yerevan, 400 meters from 
            the Armenian Opera and Ballet Theater. It offers views of the city from 
            the balcony.''',

            'about_us_text_p2': '''Facilities include a 24-hour front desk and shared 
            kitchen, a large balcony, private and shared air-conditioned rooms and free 
            Wi-Fi is available throughout. Arm Hostel & Tours includes bed linen, and 
            towels can also be booked for excursions.''',

            'about_us_text_p3': '''Popular attractions such as the Armenian Opera and 
            Ballet Theater, the Museum of History of Armenia and Northern Avenue are 
            close to Arm Hostel. Zvartnots International Airport is 10.1 km away.''',

            'conditions_header': 'Accommodation conditions',
            'conditions_item1': '''Check-in is at 14:00, check-out is at 12:00.''',
            'conditions_item2': '''Smoking is strictly prohibited in the hotel. 
            Hotel guests can only smoke in the balcony.''',

            'conditions_item3': '''Alcohol is strictly prohibited in the entire area.''',
            'conditions_item4': '''The hotel does not allow accommodation with pets''',

            'rules_header': 'Rules and conditions',
            'rules_content': '''For the safety and security of the residents and in 
            accordance with legal regulations, each guest must present a valid photo 
            ID (passport or driver's license) upon check-in.''',
        }
    elif language == armenian:
        return {
            'main_header': 'О нас',
            'about_us_text_p1': '''Arm Hostel расположен в Ереване, в 400 метрах от 
            Армянского театра оперы и балета. С балкона открывается вид на город.''',

            'about_us_text_p2': '''В числе удобств круглосуточная стойка регистрации и 
            общая кухня, большой балкон, отдельные и общие номера с кондиционером и  на 
            всей территории работает бесплатный Wi-Fi. В стоимость проживания в хостеле 
            Arm Hostel & Tours включено постельное белье, и полотенца также  можно 
            заказать экскурсии.''',

            'about_us_text_p3': '''Неподалеку от хостела Arm Hostel находятся такие 
            популярные достопримечательности, как Армянский театр оперы и балета, Музей 
            истории Армении и Северный проспект. Расстояние до международного аэропорта 
            Звартноц составляет 10 ,1 км.''',

            'conditions_header': 'Условия проживания',
            'conditions_item1': '''Заезд в 14:00, выезд в 12:00.''',
            'conditions_item2': '''Курение в отеле строго запрещено. Гости отеля могут 
            курить только в балконе.''',

            'conditions_item3': ''' Алкоголь строго запрещён на всей территории.''',
            'conditions_item4': '''В отеле не допускается проживание вместе с 
            животными''',

            'rules_header': 'Правила и условия',
            'rules_content': '''В целях безопасности проживающих, а также по 
            законодательным предписаниям, при регистрации каждый гость должен 
            предъявить действительное удостоверение личности с фотографией 
            (паспорт или водительское удостоверение).''',
        }

@translateBase
def translateBook(language):
    if language == russian:
        return {

        }
    elif language == english:
        return {

        }
    elif language == armenian:
        return {

        }

@translateBase
def translateContacts(language):
    if language == russian:
        return {
            'main_header': 'Контакты',
            'address': 'Армения  Г. Ереван, Ул. Маштоц 29, дом 10/1, 5-ый этаж.',
            'phone': 'Телефон',
        }
    elif language == english:
        return {
            'main_header': 'Contacts',
            'address': 'Armenia Yerevan, 29 Mashtots St., Yerevan, house 10/1, 5th floor.',
            'phone': 'Phone',
        }
    elif language == armenian:
        return {
            'main_header': 'Контакты',
            'address': 'Армения  Г. Ереван, Ул. Маштоц 29, дом 10/1, 5-ый этаж.',
            'phone': 'Телефон',
        }

@translateBase
def translateHome(language):
    if language == russian:
        return {

        }
    elif language == english:
        return {

        }
    elif language == armenian:
        return {

        }

@translateBase
def translateServices(language):
    if language == russian:
        return {

        }
    elif language == english:
        return {

        }
    elif language == armenian:
        return {

        }
