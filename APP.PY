import requests
import re
def get_steam_price(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price_info = data.get(str(app_id), {}).get("data", {}).get("price_overview", {})
        discount = data.get(str(app_id), {}).get("data", {}).get("discount_percent", 0)
        if price_info and discount > 0:
            print(f"Price on Steam: {price_info['final_formatted']}")
            print("Its on sale on Steam!!")
        elif discount == 0:
            print(f"Price on Steam: {price_info['final_formatted']}")
            print("Retail price btw")
        else:
            print("No price information found.")
        return data
                
    print("Failed to fetch data from Steam API.")
    return None

# Call the function
get_steam_price(2336885)


