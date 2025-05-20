import requests
# Last Epoch 899770
# Diablo IV 2344520
class SteamGames:
    game_id = None
    discount = None
    price = None
    price_after_discount = None

    def __init__(self, _game_id):
        self.game_id = str(_game_id)

    def getInfo(self):
        url = f"https://store.steampowered.com/api/appdetails?appids={self.game_id}"
        response = requests.get(url).json()
        print(response)
        if response[self.game_id]["success"] is True:
            game = response[self.game_id]["data"]["name"]
            if response[self.game_id]["data"]["is_free"] is False:
                self.price = (response[self.game_id]["data"]["price_overview"]["initial"]) / 100

                if response[self.game_id]["data"]["price_overview"]["discount_percent"] > 0:
                    self.discount = str(response[self.game_id]["data"]["price_overview"]["discount_percent"]) + "%"
                    self.price_after_discount = response[self.game_id]["data"]["price_overview"]["final_formatted"]
                else:
                    self.discount = "Aucune réduction"
                    self.price_after_discount = "N/A"
            else:
                self.price = 0

            return str(self.price), game, self.discount, self.price_after_discount
        else:
            return False