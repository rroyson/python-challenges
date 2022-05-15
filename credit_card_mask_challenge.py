credit_card_number = "444444444444444444444444"

def mask_card_number(credit_card):
    new_number = ''
    for i, num in enumerate(credit_card):
        if i < len(credit_card) - 4:
            num = "*"
            num.join(new_number)
            return new_number 
        else:
            num.join(new_number)
            return new_number
new_card = mask_card_number(credit_card_number)
print(new_card)
