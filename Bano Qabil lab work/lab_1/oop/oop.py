class student:

    def __init__(self, name,phone):
        self.name = name
        self.phone_number = phone

    def speak(self, says):
        return f"{self.name} says {says}!"

rafay = student(phone=467483256 , name="rafay")
junaid= student("junaid", 1458465654)

# name = rafay.name
# phone_number = rafay.phone_number
rafay_says = rafay.speak("kese ho")
junaid_says = junaid.speak("me theek")

print(rafay_says)
print(junaid_says)

