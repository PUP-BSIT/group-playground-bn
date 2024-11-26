import getpass

def get_password():

  password = getpass.getpass("Enter password: ")
  return password

password = get_password()
print("Your password is:", password)
