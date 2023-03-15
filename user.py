class User():
    def __init__(self, username, password, email, first_name, 
                last_name, gender, birth_date, education, country, province, login):
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._birth_date = birth_date
        self._education = education
        self._country = country
        self._province = province 
        self._login = login  # Composition of Login
    