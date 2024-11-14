adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
By the time There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
new_text_1 = adwentures_of_tom_sawer.replace("\n", " ")
print(new_text_1)

# task 02 ==
""" Замініть .... на пробіл
"""
new_text_2 = new_text_1.replace("....", "")
print(new_text_2)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
splited_text = new_text_2.split()
new_text_3 = " ".join(splited_text)
print(new_text_3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for letter in new_text_3:
    if letter == 'h':
        count +=1
print(f"Літера 'h' зустрічаєтьься {count} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_words = 0
for word in splited_text:
    if word.istitle():
        count_words += 1

print(count_words)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_index = new_text_3.find('Tom')
second_index = new_text_3.find('Tom', first_index+1)
print(second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer_sentences = re.split(r'(?<!\.)\.(?!\.)\s+(?=[A-Z])',adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
new_text_4 = (adwentures_of_tom_sawer_sentences[3]).lower()

print(f"\nHere is the lowercase text:\n\n {new_text_4}\n")
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for i in adwentures_of_tom_sawer_sentences:
    if i.strip().startswith("By the time"):
        print(True)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(f"\nThe length of the last sentence is: {len(adwentures_of_tom_sawer_sentences[-1].split())}")
