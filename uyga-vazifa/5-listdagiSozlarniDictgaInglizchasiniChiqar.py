from googletrans import Translator

data = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

translator = Translator()
translated_dict = {}

for item in data:
    if isinstance(item, str):
        translated = translator.translate(item, src='uz', dest='en')
        translated_dict[item] = translated.text.lower()

# Tagma-tag chiqarish
for key, value in translated_dict.items():
    print(f'"{key}": "{value}"')
