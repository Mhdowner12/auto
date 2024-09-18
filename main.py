import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time

# List of group usernames to join, with @ before every group
group_usernames = [
    '@oginstagramm', '@ogmarts', '@olympusmarket', '@onepiecemarket', '@onyxmarkettt',
    '@ourigmarket', '@palengke', '@paradisomarket', '@parallelmarket02', '@pawxiemarket',
    '@paxchat', '@paxinstagram', '@percmarts', '@peytxxmarket', '@phmartpremiums',
    '@phvirtualmarket', '@pietersmarket', '@piscesmarket', '@plazadeac', '@popthatpussyptp',
    '@premiermarket', '@premiumsmarketplace', '@premiumszxcc', '@premsmania', '@psychomarkett',
    '@pyxismarket', '@redymarket', '@renevagemarket', '@riosmarket', '@rvelvetmarket',
    '@sandboxmart', '@sarisarimarket', '@sbmarkett', '@scammarketph', '@serpentmarkett',
    '@sevendeadlysinsmarket', '@sfs_market', '@sfsbuysell', '@sfsgrinds', '@sfsmarketchat',
    '@sfsmarkets', '@sfsmarketss', '@sijangmarket', '@sinserssfs', '@sismark8', '@skylersmarket',
    '@slumdrunk', '@slxrpsmarket', '@smmarketlounge', '@snapchatgainchat', '@socialbuyandsell',
    '@socialmaniaog', '@socialmarkets', '@solanamart', '@solastamarketplace', '@soleilmarket',
    '@solmarkett', '@souruteikamarketx', '@spoktimarket', '@ssgains', '@stopnshoppe',
    '@supernovamarketplace', '@supremotrade', '@talamarkettt', '@tays56', '@teampayamanmarket',
    '@teiemart', '@telehub2', '@telemarketph', '@telemartph', '@telepromobuyselltrade',
    '@teleworldmarket', '@terramarket', '@tgmegamart', '@tgonlinemarket', '@thebloommartph',
    '@theboysmarketplace', '@thecloutmarket', '@theelfantasma', '@thekentmart', '@thenightmarket',
    '@thepeachymart', '@titanmarket', '@twiceujjangmarket', '@umbrellamarket',
    '@undergroundmarket1620', '@unholymarket', '@universalmarkettt', '@urbanmarketph',
    '@virgomarketplace', '@w0rldmarket', '@wasgmarket', '@wobblezmarket', '@wolf_market20',
    '@wysmarketingchat', '@xiomarkett', '@yamerokudasaiii', '@ycmmarket', '@yourshopfindmarket',
    '@ziamarket', '@discordtokengroup', '@marketofdiscord', '@sfsonlychat', '@SellingChat',
    '@keytodiamond', '@SecretMarketplace', '@socialmarketplace2021', '@instasfsmarket', '@nab_zana',
    '@fishygrinds', '@zourmarket', '@fireworksfsg', '@sfsgchat', '@groupchatsfs', '@sfsbabyshare',
    '@reqummarket', '@nighttimegains', '@trilldailymega', '@TalhaMarket', '@litdailymegas',
    '@Marshall_SMM', '@igmarketsfs', '@marketsfs', '@instasfsmarketchat', '@DrunkJunkMarket',
    '@elitemarkettt', '@mysterymart', '@powerpuffmarket', '@destroyermarket', '@mblmart',
    '@rmmarkett', '@marketmark3t', '@oonestopshop', '@maroonmarket', '@tgfreedommarket',
    '@tquantunanmarket', '@lsconlinemall', '@kmark3t', '@marketmarket26', '@tuffgongmarket',
    '@peachygamess', '@marketmarketxx'
]

async def join_group(client, group_link):
    try:
        await client(JoinChannelRequest(group_link))
        print(f"Successfully joined group: {group_link}")
        return True
    except Exception as e:
        print(f"Failed to join group {group_link}: {str(e)}")
        return False

async def login_accounts():
    accounts = []
    num_accounts = int(input("Enter the number of accounts: "))

    for i in range(num_accounts):
        print(f"\nEnter details for account {i + 1}:")
        api_id = int(input("Enter your Telegram API ID: "))
        api_hash = input("Enter your Telegram API Hash: ")
        phone_number = input("Enter phone number (with country code): ")

        client = TelegramClient(f'session_{phone_number}', api_id, api_hash)
        await client.start(phone_number)
        print(f"Account {i + 1} ({phone_number}) logged in successfully.")
        accounts.append(client)

    return accounts

async def join_groups(clients):
    total_groups = len(group_usernames)
    batch_size = 5
    group_status = {group: False for group in group_usernames}  # Track joined groups

    for idx, client in enumerate(clients):
        print(f"\nStarting to join groups with account {idx + 1}")
        group_index = 0
        while group_index < total_groups:
            # Get the next batch of groups to join
            group_batch = group_usernames[group_index:group_index + batch_size]
            tasks = [join_group(client, group) for group in group_batch if not group_status[group]]
            results = await asyncio.gather(*tasks)

            # Update the status of groups that were successfully joined
            for group, joined in zip(group_batch, results):
                if joined:
                    group_status[group] = True

            print(f"Account {idx + 1} finished joining groups {group_index + 1} to {group_index + batch_size}.")
            
            group_index += batch_size

        print("Waiting for 10 minutes before joining groups with the next account.")
        time.sleep(600)  # Sleep for 10 minutes

    print("All groups have been joined for all accounts.")

async def main():
    # Log in all accounts first
    clients = await login_accounts()
    
    # Join groups with the logged-in accounts
    await join_groups(clients)

if __name__ == "__main__":
    asyncio.run(main())