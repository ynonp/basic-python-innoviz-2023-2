# Exercises 1
#
# 1. Write a program that takes a user's age in years
#    and print back the age in months
#
# 2. Write a program that takes a user's age in months
#    and print back the age in years
#
# 3. Write a program that takes an amount of money in NIS
#    and convert it to USD
#
# age_in_years = int(input("how old are you (in years) ?"))
# age_in_months = age_in_years * 12
# print(f"Wow you are {age_in_months} months old")
#
#
# age_in_months = int(input("how old are you (in months) ?"))
# age_in_years = age_in_months / 12
# # f-string guide / tutorial
# # http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
# print(f"what's {age_in_years:.2f} years old")



from py_currency_converter import convert
print(convert(base='ILS', amount=10, to=['USD']))




