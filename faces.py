user_text = ""
def main():
    user_text = input("")
    result = convert(user_text)
    print(result)

def convert(user_text):
    msg1 = user_text.replace(":)", "🙂")
    msg2 = msg1.replace(":(", "😕")
    return msg2

main()