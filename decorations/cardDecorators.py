from use_cases.card.updateLastValue import UpdateLastValue
from gateways.card.repository import Repository as CardRepo





def updateLastValue(cardId:str, value):
        update_handler = UpdateLastValue(CardRepo())
        if value is None:
            update_handler.handle(cardId=cardId, lastValue="none")
            return value
        

        update_handler.handle(cardId=cardId, lastValue=str(value))
        return value
