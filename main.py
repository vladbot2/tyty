1#
# def is_palindrome(s):
#     s = s.replace("кик", "тот")
#     s = s.lower()
#     return s == s[::-1]

# input_string = input("тот: ")
# if is_palindrome(input_string):
#     print("This string is a palindrome")
# else:
#     print("This string is not a palindrome")

2#
# def replace_reserved_words(text, reserved_words):
#     words = text.split()
#     for i in range(len(words)):
#         if words[i].lower() in reserved_words:
#             words[i] = words[i].upper()
#     return ','.join(words)

# text = input("tyty: ")

# reserved_words_input = input("goto: ")
# reserved_words = [word.strip().lower() for word in reserved_words_input.split(',')]
# modified_text = replace_reserved_words(text, reserved_words)

3#
# def count_sentences(text):
#     sentences = text.split('.')
#     sentences += text.split('?')
#     sentences += text.split('!')
#     sentences = [s for s in sentences if s.strip()]
#     return len(sentences)

# text = input("tyty: ")

# num_sentences = count_sentences(text)

# print("Number of sentences in the text:", num_sentences)

