#convert input strings to lowercase without any surrounding whitespace



def lower_case(text):

    text = text.lower()
    text = text.strip()
    return text


print(lower_case(' Chloe    '))

# def lower_case(text):
#     text = text.lower()
#     text = text.strip()
#     return text
#
# print(lower_case("SUPER"))