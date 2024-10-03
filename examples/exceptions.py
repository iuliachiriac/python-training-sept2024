def parse_email(email_address):
    username, domain = email_address.split("@")
    if "." not in domain:
        raise ValueError("invalid domain")
    return username, domain


addresses = [
    "john.doe@gmail.com",
    "test.com",
    "hello@@world",
    "jane@test.com",
    100,
    "maya@test",
]


for address in addresses:
    try:
        user, dom = parse_email(address)
    except (AttributeError, ValueError) as ex:
        print(f"Invalid address: {address} ({ex})")
    else:
        print(f"Welcome, {user}!")
    finally:
        print("Executes every time", end="\n\n")
