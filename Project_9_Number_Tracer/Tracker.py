import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

countrycode = input("Enter your country code of mobile number: \n")
number = input("Enter mobile number: \n")
number_countrycode = countrycode+number

# To check country location
ch_number = phonenumbers.parse(number_countrycode, "CH")
print(f"The country name is: {geocoder.description_for_number (ch_number, 'en')}")

# To find service provider
service_number = phonenumbers.parse(number_countrycode, "RO")
print(f"Service provider name: {carrier.name_for_number(service_number, 'en')}")
