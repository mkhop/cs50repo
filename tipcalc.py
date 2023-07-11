def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dnodollar = d.replace("$", "")
    return (float(dnodollar))

def percent_to_float(p):
    pnopercent = p.replace("%", "")
    pconvert = float(pnopercent)/100
    return pconvert

main()