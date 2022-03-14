import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
g_trumps_broken = False


def convert_rank_to_number(rank):
    number = 0
    if rank == '1':
        number = 1
    elif rank == '2':
        number = 2
    elif rank == '3':
        number = 3
    elif rank == '4':
        number = 4
    elif rank == '5':
        number = 5
    elif rank == '6':
        number = 6
    elif rank == '7':
        number = 7
    elif rank == '8':
        number = 8
    elif rank == '9':
        number = 9
    elif rank == '10':
        number = 10
    elif rank == 'J':
        number = 11
    elif rank == 'Q':
        number = 12
    elif rank == 'K':
        number = 13
    elif rank == 'A':
        number = 14
    return number


def compare_cards(trumps, card1, card2):
    """compare card1 with card2 and return the higher card. card1 gets precedence."""
    higher_card = Card(rank=0, suit='joker')

    card1_rank, card1_suit = card1
    card2_rank, card2_suit = card2
    if card2_suit == trumps and card1_suit != trumps:
        # if the second card is a trump then it takes precedence
        higher_card = card2
    elif card2_suit == card1_suit:
        # if they are the same suit, then higher card wins
        if convert_rank_to_number(card1_rank) > convert_rank_to_number(card2_rank):
            higher_card = card1
        else:
            higher_card = card2
    else:
        # if suits are mismatched, and card2 is not a trump, then card1 wins
        higher_card = card1
    return higher_card


def valid_card(trumps, trumps_broken, player, card, *played):
    """
    you cannot lead with a trump unless trumps are broken
    you have to follow suit if you can
    if you cannot follow suit, you can play any card

    :param trumps:
    :param trumps_broken:
    :param played:
    :return allowed:
    """
    allowed = False

    cards_played = played[0]
    card_rank, card_suit = card
    # you cannot lead with a trump unless trumps are broken or you only have trumps left
    if len(cards_played) == 0: # this means that you are leading
        if not trumps_broken: # this means you cannot play a trump
            if card_suit != trumps: # if don't play trumps, its fine
                allowed = True
            else: # if do play trumps, that must be all you have
                for card in player.hand:
                    # v_card_rank, v_card_suit = card
                    v_card_suit = card[1]
                    if v_card_suit != trumps:
                        allowed = False
                        break
                    else:
                        allowed = True
        else:
            allowed = True
    else:
        # you have to follow suit if you can
        first_played = cards_played[0]
        first_card = first_played[1]
        #first_card_rank, first_card_suit = first_card
        first_card_suit = first_card[1]
        if first_card_suit == card_suit:
            # if you've followed suit then fine.
            allowed = True
        else:
            # check if the player has any of the first card's suit in their hand
            for card in player.hand:
                #v_card_rank, v_card_suit = card
                v_card_suit = card[1]
                # if there is a card in your hand that is the same as first card played
                if v_card_suit == first_card_suit:
                    allowed = False
                    break
                else:
                    # if you cannot follow suit, you can play any card
                    allowed = True

    return allowed
