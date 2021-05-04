class Item:
    """Luokka, jonka avulla luodaan tarvikeolio.
    """

    def __init__(self, typex: list, description: str, size: str, brand: str, color: str, username: str):
        """Luokan konstruktori, joka luo uuden tarvikeolion.

        Args:
            typex (list): tarviketyyppi (dropdown)
            description (str): tarvikkeen tarkempi kuvaus
            size (str): tarvikkeen koko
            brand (str): tarvikkeen merkki
            color (str): tarvikkeen väri
            username (str): tarviketta vastaava käyttäjätunnus
        """

        self.type = typex
        self.description = description
        self.size = size
        self.brand = brand
        self.color = color
        self.username = username
