from collections import OrderedDict

favourite_Languages = OrderedDict()

favourite_Languages['jean'] = 'python'
favourite_Languages['sean'] = 'c'
favourite_Languages['billy'] = 'ruby'
favourite_Languages['sia'] = 'python'

for name, language in favourite_Languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}. ")
