![image](https://github.com/user-attachments/assets/6ac80be9-e503-4ee8-b8d9-3a4ecb0eb9a9)

To win at ZED RUN you need the best horses, to get the best horses you need to breed smart. 
This tool helps to SNIPE other people studs when they're put into the stud barn. 

-----------------------
---- Stud Watcher -----
-----------------------

Stud Watcher is a Python script designed to monitor Zed Run on-chain events;
- Tracks when studs are placed into the stud barn for breeding
- Sends notifications to Telegram chats

(!) Please use responsibilitiy, being mindful not to steal all of the stud's covers. 


-----------------------
------- Set-up --------
-----------------------

Ensure you have a CSV file named horse_db.csv. 

This database is essential; studs will only be triggered if on this database. 

You can get data on horse universes from the hawku data dumps: https://zed-odds.netlify.app/

Further analysis will be needed to refine the list to target the BEST studs - more on that in another post. 



-----------------------
------ API keys -------
-----------------------

    Obtain an API key from Alchemy.
    Obtain a Telegram Bot API token by creating a bot on Telegram.

Environment Variables: Set up the following environment variables on your system:

    export ALCHEMY_API_KEY='your_alchemy_api_key'
    export TG_CLIENT_ID='your_telegram_bot_api_token'

Update Configuration: Update the script to read these values from the environment variables.


-----------------------
----- VPS Stuff -------
-----------------------

Owners can put horses into stud whenever they like so this script needed to run 24/7, which means it needs to be run from a VPS. 

To do this you'll need to learn a little about UNIX and SSH to set-up the scirpt and then some more when updating the horse_db.csv. 

For an overview please see the UNIX_SSH_Stud_Watcher_GH PDF in the repo.

-----------------------
----- How it works ----
-----------------------

1. HorseData Class - The HorseData class is responsible for;

    Initializing a horse object with its ID and price.
    Matching the horse's ID with the data in the provided CSV database.
    Formatting the horse's information for display.

Methods;

    __init__(self, id, price): Initializes the horse data.
    match_db(self): Matches the horse's ID with the database.
    __str__(self): Returns a string representation of the horse's data.


2. EventsWatch Class - The EventsWatch class is responsible for:
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

<img width="470" alt="image" src="https://github.com/user-attachments/assets/206ca062-1dbf-4065-b66e-932dd9eb5458">

