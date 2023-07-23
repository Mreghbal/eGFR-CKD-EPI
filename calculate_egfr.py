def calculate_egfr(age, gender, serum_creatinine, race):
    # Validate input values
    if age <= 0 or serum_creatinine <= 0:
        raise ValueError("Age and serum creatinine must be greater than zero.")

    # Validate gender
    gender = gender.lower().strip()
    if gender not in ["male", "female"]:
        raise ValueError("Gender must be either 'male' or 'female'.")

    # Validate race
    race = race.lower().strip()
    if race not in ["white", "black"]:
        raise ValueError("Race must be either 'white' or 'black'.")

    # Calculate eGFR using CKD-EPI equation
    if gender == "female":
        if race == "black":
            a, b, c, k = 166, -0.329, -1.209, 0.7
        else:
            a, b, c, k = 144, -0.411, -0.329, 0.7
    else: # gender == "male"
        if race == "black":
            a, b, c, k = 163, -0.411, -1.209, 0.9
        else:
            a, b, c, k = 141, -0.411, -0.329, 0.9

    egfr = a * (serum_creatinine ** b) * (age ** c) * (k if serum_creatinine >= 0.9 else 1)
    return egfr

# Example usage
try:
    age = int(input("Enter age: "))
    gender = input("Enter gender (male/female): ")
    serum_creatinine = float(input("Enter serum creatinine level (mg/dL): "))
    race = input("Enter race (white/black): ")

    egfr = calculate_egfr(age, gender, serum_creatinine, race)
    print("eGFR:", egfr)

except ValueError as e:
    print("Error:", str(e))
