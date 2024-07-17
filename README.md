-----------------------
---- Stud Watcher -----
-----------------------

Stud Watcher is a Python script designed to monitor on-chain events related to Zed Run's NFT horse racing game; tracking when studs are placed into the stud barn for breeding, matcheing them against a local horse database, and sending notifications to specified Telegram chats.

Please use responsibilitiy, being mindful not to steal all of the stud's covers. 


-----------------------
---- Requirments ------
-----------------------

To run stud_watcher.py, you need the following:
1. Python 3.8+
2. Required Python packages: pandas, python-telegram-bot, web3.py


-----------------------
------- Set-up --------
-----------------------

Database: Ensure you have a CSV file named horse_db.csv with the following columns: horse_id, name, genotype, bloodline, breed_type, stable_name. This contains all of the horses that you want to be notified about. 

API keys

    Obtain an API key from Alchemy.
    Obtain a Telegram Bot API token by creating a bot on Telegram.

Environment Variables: Set up the following environment variables on your system:

    export ALCHEMY_API_KEY='your_alchemy_api_key'
    export TG_CLIENT_ID='your_telegram_bot_api_token'

Update Configuration: Update the script to read these values from the environment variables.


-----------------------
----- How it works ----
-----------------------

HorseData Class - The HorseData class is responsible for;

    Initializing a horse object with its ID and price.
    Matching the horse's ID with the data in the provided CSV database.
    Formatting the horse's information for display.

Methods;

    __init__(self, id, price): Initializes the horse data.
    match_db(self): Matches the horse's ID with the database.
    __str__(self): Returns a string representation of the horse's data.


EventsWatch Class - The EventsWatch class is responsible for:
    Configuring the connection to the Polygon blockchain.
    Fetching the latest horse-related transactions.
    Sending horse information to the specified Telegram chats.

Methods;
    __init__(self): Initializes the watcher with necessary configurations.
    __extract_txs_data(self, txs): Extracts horse data from transactions.
    __get_latest_tx(self): Fetches the latest transactions from the blockchain.
    run(self): Main loop for monitoring transactions and sending Telegram notifications.

Main Execution
The script runs the EventsWatch class in an asynchronous loop to constantly monitor and notify about horse transactions.


-----------------------
------- Example -------
-----------------------

Upon running, the script will output the latest transactions and send formatted horse data to the configured Telegram chats if there's a match in the database.

9 Buterin genesis
Horse Kebalah, 0.0216
Stable: 4theloveofcheesenwine
Hawku: https://hawku.com/horse/42171
