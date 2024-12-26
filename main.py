import hashlib


def convert(password):
    return hashlib.sha1(password.encode()).hexdigest()


def main():
    user_sha1 = input("Enter the SHA1 hash: ")
    cleaned_sha1 = user_sha1.strip().lower()
    
    with open('./passwords.txt') as file:
        for line in file:
            password = line.strip()
            converted = convert(password)
            if cleaned_sha1 == converted:
                print(f"Password found: {password}")
                return
    print("Password not found")





if __name__ == "__main__":
    main()