
is_valid_input = False

while not is_valid_input:
    salary_gross_input = input("Enter your gross salary: ")
    try:
        test_input = float(salary_gross_input)
    except ValueError:
        print("Your input was not a number")
        continue
    salary_gross = float(salary_gross_input )
    if salary_gross > 0:
        break
    else:
        print("Your value must be larger than 0!")

print(f"You typed £{salary_gross_input} as your salary.")

th_1 = 12570
th_2 = 50270
th_3 = 150000

rt_1 = 20
rt_2 = 30
rt_3 = 40

def calc_after_tax(gross):
    if gross < th_1:
        return gross
    elif th_1 <= gross < th_2:
        return ((1 - (rt_1/100)) * (gross - th_1)) + th_1
    elif th_2 <= gross < th_3:
        return ((1 - (rt_2/100)) * (gross - th_2)) + \
               ((rt_2/100) * (th_2 - th_1)) + th_1
    elif gross >= 150000:
        return ((1 - (rt_3/100)) * (gross - th_3)) + \
               ((rt_3/100) * (th_3 - th_2)) + \
               ((rt_2/100) * (th_2 - th_1)) + th_1

def calc_after_tax_nic(gross):
    return  round((90/100) * calc_after_tax(gross), 2)


def format_exit_sentence(gross):
    aftr_tax = calc_after_tax(gross)
    aftr_tax_nic = calc_after_tax_nic(gross)
    sentence = "\n"
    sentence += f"Your salary after tax deductions is {round(aftr_tax, 2)}.\n"
    sentence += f"Your net salary after tax and NI deductions is {round(aftr_tax_nic, 2)}.\n"
    return sentence

print(format_exit_sentence(salary_gross))


