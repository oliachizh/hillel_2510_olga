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






