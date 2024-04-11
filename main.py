if __name__ == '__main__':
    def menu():
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode:")
            encoded_pass = encoder(password)
            print("Your password has been encoded and stored.")
        elif option == 2:
            pass
        elif option == 3:
            pass
    def encoder(numbers):
        output_list = []
        output = ""
        for i in numbers:
            output_list.append(int(i) + 3)
        for i in output_list:
            output = output + str(i)
        return output
