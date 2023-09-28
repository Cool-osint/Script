import argparse
import re
from tools.num_scripts import *
from tools.email_scripts import *

banner = """
888b     d888          888      d8b 888                .d88888b.   .d8888b. 8888888 888b    888 88888888888 
8888b   d8888          888      Y8P 888               d88P" "Y88b d88P  Y88b  888   8888b   888     888     
88888b.d88888          888          888               888     888 Y88b.       888   88888b  888     888     
888Y88888P888  .d88b.  88888b.  888 888  .d88b.       888     888  "Y888b.    888   888Y88b 888     888     
888 Y888P 888 d88""88b 888 "88b 888 888 d8P  Y8b      888     888     "Y88b.  888   888 Y88b888     888     
888  Y8P  888 888  888 888  888 888 888 88888888      888     888       "888  888   888  Y88888     888     
888   "   888 Y88..88P 888 d88P 888 888 Y8b.          Y88b. .d88P Y88b  d88P  888   888   Y8888     888     
888       888  "Y88P"  88888P"  888 888  "Y8888        "Y88888P"   "Y8888P" 8888888 888    Y888     888     
                                                                                                            
                                                                                                                                                                                                              
https://github.com/viralvaghela/OSINT_MOBILE @ViralVaghela
"""

 
services_num = {
    "swiggy": check_swiggy,
    "flipkart": check_flipkart,
    "upstox": check_upstox,
    "instagram": check_instagram,
    "snapdeal": check_snapdeal
}

# Create a dictionary to map service names to functions
services_num = {
    "twitter":check_twitter,
    
}

def is_valid_phone_number(identifier):
    # You can customize this regular expression to match your phone number format
    phone_number_pattern = r"^\d{10}$"
    return re.match(phone_number_pattern, identifier) is not None

def is_valid_email(identifier):
    # Basic email format validation 
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, identifier) is not None

def main():
    print(banner)  # Print the ASCII banner

    parser = argparse.ArgumentParser(description="Check various services with a phone number or email address.")
    parser.add_argument("identifier", type=str, help="Phone number or email address to use")
    args = parser.parse_args()
    identifier = args.identifier

    if is_valid_phone_number(identifier):
        for service_name, service_function in services_num.items():
            print(f"Checking {service_name} for phone number {identifier}...")
            service_function(identifier)
            print()

    elif is_valid_email(identifier):
        for service_name, service_function in services_num.items():
            print(f"Checking {service_name} for phone number {identifier}...")
            service_function(identifier)
            print()
    else:
        print("Invalid input. Please provide a valid phone number or email address.")

if __name__ == "__main__":
    main()
