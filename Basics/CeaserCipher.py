alphabates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher():
    
    encode_decode = input("Type 'encode' for encryption or 'decode' for decryption. ").lower()

    if encode_decode != "encode" and encode_decode != "decode":
        print("Invalid input.")
        further = int(input("Type '1' to continue the program or '0' to exit the program. "))
        if further == 1:
            cipher()
        else:
            return 0

    input_text = input("Type your massage : ").lower()
    shift_amount = int(input("Enter shift number : "))

    output_text = ""
    if encode_decode == "decode":
                shift_amount *= -1

    for letter in input_text :
        if letter not in alphabates:
            output_text += letter
        else:
            shifted_position = alphabates.index(letter) + shift_amount
            output_text += alphabates[shifted_position%len(alphabates)]
                 
    print(f"Your {encode_decode}d messaage is : {output_text}")

    further = int(input("Type '1' to continue the program or '0' to exit the program. "))
    if further == 1:
        cipher()
    else:
        return 0

cipher()
