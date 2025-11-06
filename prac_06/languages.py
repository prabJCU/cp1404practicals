"""
CP1404 - Languages
"""
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


print(f"The dynamically typed languages are:")
programming_languages = [python, visual_basic, ruby]
for language in programming_languages:
    if language.is_dynamic():
        print(language.language)