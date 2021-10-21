import requests

def main():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    try:
        response = requests.get(coindesk_url)
        response.raise_for_status()

        data = response.json()
        current_bitcoin_value_in_usd = data['bpi']['USD']['rate_float']
        print(current_bitcoin_value_in_usd)

        bitcoin_amount = get_amount()
        user_bitcoin = get_input_value(bitcoin_amount)
        total_bitcoin_in_usd = user_bitcoin * current_bitcoin_value_in_usd
        show_results(bitcoin_amount, total_bitcoin_in_usd)
    except Exception as e:
        print(e)
        print('There was an error trying to access the url')


def get_amount():
    amount = input('How many bitcoins do you want to convert? ')
    return amount

def get_input_value(amount):
    try:
       return float(amount)
    except ValueError as err:
        print('Wrong data type')

def show_results(bitcoins, total_in_usd):
    print(f'Your {bitcoins} bitcoins are equal to ${total_in_usd} dollars')

if __name__ == "__main__":
    main();