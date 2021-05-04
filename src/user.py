class User:
    """Luokka, jonka avulla luodaan käyttäjäolio.
    """

    def __init__(self, username: str, password: str):
        """Luokan konstruktori, joka luo uuden käyttäjäolion.

        Args:
            username (str): käyttäjätunnus
            password (str): salasana
        """

        self.username = username
        self.password = password
