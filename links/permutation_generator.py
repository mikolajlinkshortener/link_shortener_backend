from django.conf import settings
from itertools import permutations


class Permutation:
    """
    This class generates a short link of the length defined in the settings using SHORT_LINK_LENGTH.
    To avoid problems after a server restart, the list is shuffed. 
    """

    short_link_generator = permutations(settings.SYMBOLS_LIST, settings.SHORT_LINK_LENGTH)

    @classmethod
    def create_diffrent_permutation_generator(
        self, symbol_list: list[str], r: int
    ) -> None:
        """
        Overrides the permutation generator. For testing purpose only.
        """
        self.short_link_generator = permutations(symbol_list, r)
