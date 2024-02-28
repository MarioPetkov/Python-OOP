import re

text = "единствен единичен Единствено ЕДИН"
pattern = re.compile(r'ЕДИН\w*', re.IGNORECASE)  # или re.compile(r'ЕДИН\w*', re.I)
matches = pattern.findall(text)

print(matches)  # Извежда: ['единствен', 'единичен', 'Единствено', 'ЕДИН']
