# NAME:Abdul_Rafay 
# ID: 59308
# EMAIL:rafaya4321@gmail.com 
# SOLUTION: Currecny conversion plays an important plays around the Globe like cross border payments,
# international travels and more. ao i have made a user-friendly easy to use currecny converter to help resolve issues.

# making request to get the data 
import requests

# creating a function for the exchange rates

def get_exchange_rates(to_currecny, from_currecny):
# creating a api url for exchange rates 
    url= f"https://api.exchangerate-api.com/v4/latest/{to_currecny}"
# making a get request from the api to fetch some amount of data 
    response= requests.get(url)

    # checking if the request is succesfull the status code==200
    if response.status_code == 200 :
        # parse the JSON  response 
        data=response.json()
        # retreaving the exchange rate for the currecny to be converted (from_currecny) from the response
        return data["rates"].get(from_currecny)
    else:
        # return none if the request was unsuccesfull 
        return None

# creating function for the currecny coverter 
def convert_currency (amount, to_currecny, from_currecny) :
    # getting the exchange rate for the specific currencies 
    exchange_rate=get_exchange_rates(to_currecny, from_currecny)

    # checking if the exchange rate was succesfull 
    if exchange_rate is not None :
        # then perform the currecny conversion 
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        # return None if the exchange rate could not be fetched 
        return None 

def main(): 
    print ("Welcome to Rafay's Currency Converter!")
#Getting user input for the conversion 
    amount = float(input("Kindly enter the amount: "))
    to_currecny = input("Kindly enter the country code to convert (e.g, USD):").upper()
    from_currecny= input("Kindly enter the country code that you wish to convert (e.g,PKR):").upper()

    # performing the currecny converstion 
    converted_amount = convert_currency(amount,to_currecny, from_currecny)

    # displaying the result or an error meesage if occured 
    if converted_amount is not None:
        print(f"{amount} {to_currecny} is equals to {converted_amount:.2f}  {from_currecny}")
    else:
        print("Unable to fetch exchange rate. Kindly check your input currecncies ")

if __name__ == "__main__" :
    main()      
