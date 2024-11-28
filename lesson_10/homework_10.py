def sum_of_list_elements(lst):
    if len(lst) == 0:
        print("List is empty")
        return
    for i in lst:
        try:
            print(sum([int(j) for j in i.split(",")]))
        except ValueError:
            print(f"Не можу це зробити")
        except Exception:
            print("Інша помилка")


def check_age_more_than_30(people_records, *indexes):
    for i in indexes:
        if i> len(people_records)-1:
            return "Write correct indexes"

    age_indexes = [people_records[i][2] for i in indexes]
    return all(age >= 30 for age in age_indexes)

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            print("Can't be > 25")
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

def find_longest_word(list_of_words):
    if len(list_of_words) == 0:
        raise ValueError("list cant be empty")
    try:
        return max(list_of_words, key=lambda word:len(word))
    except ValueError as e:
        return f"Error {e}"
    except TypeError:
        return "Must be str"

print(find_longest_word([1]))







