import time
import pandas as pd
import telegram
from web3 import Web3 
from asyncio import run 

class HorseData:
    _db = pd.read_csv("horse_db.csv")
    def __init__(self, id, price):
        self.id = int(id, 16)
        self.price = Web3.fromWei(int(price, 16), "ether")
        self.name = None
        self.genotype = None
        self.bloodline = None
        self.breed_type = None
        self.stable_name = None
        self.matched = False

        self.match_db()

    def match_db(self):
        horse_row = self._db[self._db["horse_id"] == self.id]
        print(horse_row)
        if not horse_row.empty:
            self.name = horse_row["name"].item()
            self.genotype = horse_row["genotype"].item()
            self.bloodline = horse_row["bloodline"].item()
            self.breed_type = horse_row["breed_type"].item()
            self.stable_name = horse_row["stable_name"].item()
            self.matched = True
        else:
            print(f"{self.id} Not Found")

    def __str__(self):
        if self.matched:
            return f"{self.genotype} {self.bloodline} {self.breed_type}\n{self.name}, {self.price}\n" + f"{self.stable_name}\n" + f"https://hawku.com/horse/{self.id}\n" + f"zlead.vercel.app/horses/{self.id}"
        else:
            return f"{self.id} Not found"

class EventsWatch:
    def __init__(self):
        # initial configuration
        self.api_key = "ALCHEMY_API_KEY"
        self.web3 = Web3(Web3.HTTPProvider(f"https://polygon-mainnet.g.alchemy.com/v2/{self.api_key}"))
        self.contract_address = "0x7aDBCED399630dd11A97f2E2dc206911167071ae"
        self.topics = ["0x597b23690eff5a748e9caeb1673aca23d360fa4591de869f7dfd0ce30408e0b5"] 
        self.telegram_client = telegram.Bot("TG_CLIENT_ID")
        self.telegram_chat_ids = [-696737..., -73705...] 

        # changing variables
        self.last_block_fetched = self.web3.eth.block_number
    
    def __extract_txs_data(self, txs):
        horses_data = []
        for tx in txs:
            horses_data.append(HorseData(tx["data"][2:66], tx["data"][66:130]))
        return horses_data

    def __get_latest_tx(self):
        latest_txs = self.web3.eth.get_logs({
            "fromBlock": self.last_block_fetched + 1, 
            "toBlock": "latest", 
            "address": self.contract_address,
            "topics": self.topics
        })

        print(f"latest_txs: {latest_txs}")
        horses_data = [] 
        if latest_txs != []:
            self.last_block_fetched = latest_txs[-1]["blockNumber"]
            horses_data = self.__extract_txs_data(latest_txs)

        return horses_data 
    
    #def run(self):
    async def run(self):
        while True:
            try:
                horses_data = self.__get_latest_tx()
                for horse in horses_data:
                    if horse.matched:
                        for chat_id in self.telegram_chat_ids:
                            await self.telegram_client.send_message(text=str(horse), chat_id=chat_id)
                time.sleep(5)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    run(EventsWatch().run())

