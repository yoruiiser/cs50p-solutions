
import requests
import sys

def main():
    amount=get_number()*get_price()
    print(f"${amount:,.4f}")


def get_number():
    try:
      if len(sys.argv)==2:
       n=sys.argv[1]
       n=float(n)
       return n
      else:
         sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


def get_price():
         try:
            response=requests.get("rest.coincap.io/v3/assets/bitcoin?apiKey=dc13f8e57a34c1a782ccfd979af171d89aaae12659191c93b062ee23e2afe795")
            i=response.json()
            return float(i["data"]["priceUsd"])
         except requests.RequestException:
              sys.exit()

if __name__ == "__main__":
    main()
