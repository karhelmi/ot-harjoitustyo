from user import User
from item import Item
from repositories.user_repository import user_repository
from repositories.item_repository import item_repository


class AppService:
    """Luokka, jonka avulla välitetään tietoa userfacesta repositorioon eli ns. palvelutaso.

    Attributes: user_repository: repositorio käyttäjätiedoille.
                item_repository: repositorio tarviketiedoille.

    """

    def __init__(self, user_repository, item_repository):
        """Luokan konstruktori, joka luo palvelutason yhteyden repositorioihin.

        Args:
            user_repository: käyttäjätietojen talletusrepositorio. 
            item_repository: tarviketietojen talletusrepositorio.
        """

        self.user = None
        self.user_repository = user_repository
        self.item_repository = item_repository

    def create_new_user_command(self, username, password):
        """Välittää tiedot uuden käyttäjän luontia varten.

        Args:
            username: ehdotettu käyttäjänimi
            password: ehdotettu salasana

        Raises:
            ValueError: Jos käyttäjänimi on jo olemassa.

        Returns:
            User- eli käyttäjäolion.
        """

        user_exists = self.user_repository.find_by_username(username)

        if user_exists:
            raise ValueError

        user = self.user_repository.create_user_to_database(
            User(username, password))

        return user

    def login_command(self, username, password):
        """Välittää kirjoitetut login-tiedot.

        Args:
            username: ui:ssa kirjoitettu käyttäjänimi
            password: ui:ssa kirjoitettu salasana

        Raises:
            ValueError: Jos käyttäjänimeä ei ole tai salasana ei vastaa käyttäjänimelle annettua salasanaa.

        Returns:
            User- eli käyttäjäolion.
        """

        user = self.user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise ValueError(
                "Annettua käyttäjätunnusta ei löytynyt tai salasana on väärä.")

        self.user = user

        return user

    def create_item_command(self, type1, description2, size3, brand4, color5, username):
        """Välittää kirjoitetut tarviketiedot, jotta ne lisätään tietokantaan.

        Args:
            type1: tarviketyyppi (dropwdown)
            description2: tarvikkeen tarkempi kuvaus
            size3: tarvikkeen koko
            brand4: tarvikkeen merkki
            color5: tarvikkeen väri
            username: käyttäjän käyttäjätunnus

        Returns:
            Item- eli tarvikeolion.
        """

        item = self.item_repository.create_item_to_database(
            Item(type1, description2, size3, brand4, color5, username))

        return item

    def retrieve_items_command(self, username, selection):
        """Palauttaa käyttäjän hakua vastaavat tarviketiedot tietokannasta.

        Args:
            username: käyttäjänimi
            selection: tarviketyyppi (dropdown)

        Returns:
            Listan Item- eli tarvikeolioista, jotka vastaavat hakua.
        """

        all_items_table = self.item_repository.retrieve_items_from_database(
            username, selection)

        return all_items_table


app_service = AppService(user_repository, item_repository)
