from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.errors import SessionPasswordNeededError

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'
phone_number = int(input("ENTER YOUR NUMBER (e.g., 9838383929): "))

group_list = [
    "https://t.me/arkimart",
    "https://t.me/gwopchasers",
    "https://t.me/nighttimegains",
    "https://t.me/socialcapitalmarket",
    "https://t.me/stitchmarket",
    "https://t.me/tgonlinemarket",
    "https://t.me/undergroundmarket1620",
    "https://t.me/areumart",
    "https://t.me/exquisemarket",
    "https://t.me/souruteikamarketx",
    "https://t.me/cubashill",
    "https://t.me/primanovmm",
    "https://t.me/brazilshill",
    "https://t.me/exposerworld",
    "https://t.me/securedmarket",
    "https://t.me/diamondmarketsfs",
    "https://t.me/riosmarket",
    "https://t.me/trustedmarket",
    "https://t.me/lemonmartt",
    "https://t.me/instamarketplace",
    "https://t.me/socialmediamarkettt",
    "https://t.me/thewoochat",
    "https://t.me/marketplaceaio",
    "https://t.me/yaikmicmoney",
    "https://t.me/mini_martph",
    "https://t.me/caboverdeshill",
    "https://t.me/ogusernames",
    "https://t.me/oceans_market",
    "https://t.me/dmark8",
    "https://t.me/openmarketplace77",
    "https://t.me/mega4metable",
    "https://t.me/sijangmarket",
    "https://t.me/terramarket",
    "https://t.me/aiocrime2",
    "https://t.me/cryptomarketplaceopen",
    "https://t.me/digigrowthsfs",
    "https://t.me/swipersbijeennn",
    "https://t.me/viralsmarket",
    "https://t.me/paraguayshill",
    "https://t.me/scammarketph",
    "https://t.me/kremlinhacking",
    "https://t.me/igmarketplaces",
    "https://t.me/instabossmarket",
    "https://t.me/chopstarzzz",
    "https://t.me/fnayshopchat",
    "https://t.me/successed",
    "https://t.me/tiggerslounge",
    "https://t.me/bobamarket",
    "https://t.me/instamarket4u",
    "https://t.me/nishinoyamart",
    "https://t.me/global_deals",
    "https://t.me/colombiashill",
    "https://t.me/auxamarket",
    "https://t.me/fraudstars123",
    "https://t.me/fraudmtl21",
    "https://t.me/shanksmarket",
    "https://t.me/frioshopx",
    "https://t.me/betmarkett",
    "https://t.me/shikshumarket",
    "https://t.me/vv_card",
    "https://t.me/beachmarketph",
    "https://t.me/mmmarket"
]

def main():
    client = TelegramClient('session_name', api_id, api_hash)

    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            client.sign_in(phone_number, input('Enter the code you received via SMS: '))
        except SessionPasswordNeededError:
            password = input('Two-step verification is enabled. Enter your password: ')
            client.sign_in(password=password)

    for index, group in enumerate(group_list):
        try:
            client(JoinChannelRequest(group))
            print(f'Successfully joined {group}')
        except Exception as e:
            print(f'Failed to join {group}: {e}')

        # Sleep for 10 minutes after every 4th group
        if (index + 1) % 4 == 0:
            print("Sleeping for 10 minutes...")
            time.sleep(600)  # 600 seconds = 10 minutes

    client.disconnect()

if __name__ == '__main__':
    main()