d_age_in_h_year = int(input("Enter age of dog in human years: "))
d_age_in_d_years = 0
if d_age_in_h_year < 0:
    print("dog's age in human year must be in positive number")
elif d_age_in_h_year <=21:
    d_age_in_d_years = d_age_in_h_year/10.5
    print("dog's age in dog year", int(d_age_in_d_years))
elif d_age_in_h_year >21:
    d_age_in_d_years = 2+((d_age_in_h_year - 21)/4)
    print("dog's age in dog year", int(d_age_in_d_years))
