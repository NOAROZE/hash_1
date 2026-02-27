# answers:

# ----------------------- Questions (Version A):

# How many items will the set contain?
# --- 1
# Why?
#בגלל שהוא בודק לפי ה hash ורואה שזה אותו דבר כי יש פונקציה שתמיד מחזירה אותו דבר - 999 וגם הפונקציה שמשוואה תמיד מחזירה אמת אם מדובר באותו אוביקט לכן מתיחס לזה כאותו דבר ---
# How many items will the dict contain?
#גם 1 אותו רעיון כמו ב- SET הוא בודק מה ה- HASH רואה שזה אותו דבר וכשהוא משווה בפונקציה EQ הוא מקבל אמת כי מדובר באותו אוביקט ודורס את הערך הקיים ומכניס את החדש כלומר מתיחס לזה כאל אותו דבר ולכן סופר באורך רק 1 ---
# What will d[obj_a] return?
#הוא יחזיר "banan" כי הערך נדרס ---
# Did the second insert override the first value? Explain.
#כן כי בגלל הפונקציות מה שהסברתי למעלה הוא מזהה שקיים כבר אובייקט כזה ואז הוא מעדכן אותו לערך החדש ---

# ----------------------- Questions (Version B):

# How many items will the set contain now?
# --- 2

# Why?
# למרות שה-HASH מחזיר תמיד אותו ערך הפונקציה של EQ תמיד מחזירה שקר כלומר 2 האוביקטים שונים תמיד ולכן כשהוא בודק שיוויון ורואה שהם לא שווים הוא מוסיף ל- SET עוד אחד ---

# How many items will the dict contain now?
# --- 2

# What will d[obj_a] return now?
# --- "cat"

# Explain the difference between Version A and Version B.
# לא מספיק שה-HASH מחזיר תמיד אותו ערך צריך שכשמשווים הם יצאו זהים בשביל שה-DICT/SET יתיחס אליהם כאותו דבר


def has_duplicates(*args):
    for i in range(0, len(args) - 1):
        if args[i] in args[i+1::]:
            return True
    return False

def find_duplicates(*args):
    set1 = set()
    for i in range(0, len(args) - 1):
        if args[i] in args[i+1::]:
            set1.add(args[i])
    return set1


print(has_duplicates(1, 2, 3))
# expected: False
print(find_duplicates(1, 2, 3))

print(has_duplicates(1, 2, 2, 3))
# expected: True
print(find_duplicates(1, 2, 2, 3))

print(has_duplicates("a", "b", "a"))
# expected: True
print(find_duplicates("a", "b", "a"))

def pick_keys(prefix = "is_", **kwargs):
    dict1 = {}
    for key, value  in kwargs.items():
        if key.startswith(prefix):
            dict1[key] = value
    return dict1


result = pick_keys(name="Dana", is_admin=True, age=20, is_active=False)
print(result)
# expected:
# {'is_admin': True, 'is_active': False}
result1 = pick_keys(prefix="na", name="Dana", is_admin=True, age=20, is_active=False)
print(result1)

