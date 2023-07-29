
# PYTHON PROGRAMMING QAP 4 - Program 1

# Written By: Janeil Carroll
# Date Written: July 26-28, 2023

# PROGRAM DESCRIPTION:
# A program used to process customer insurance policy information for OneStop Insurance Company.

# Import Libraries
import time
import datetime
from tqdm import tqdm

# Open and read values from defaults file.

f = open("OSICDef.dat")
NextPolicyNum = int(f.readline())
BasicPremium = float(f.readline())
AddCarDiscount = float(f.readline())
ExLiabFee = float(f.readline())
GlassCoverageFee = float(f.readline())
LoanerCoverageFee = float(f.readline())
HstRate = float(f.readline())
ProFeeMonPay = float(f.readline())
f.close()

# Program user inputs with validations.

while True:

    while True:
        FirstName = input("Enter the customer's first name (Type END to quit.): ").title()
        if FirstName == "":
            print("Please try again. Customer name cannot be empty.")
        else:
            break

    if FirstName.upper() == "END":
        print("""
        Thank you for using the One Stop Insurance Company policy program!
        All information has been successfully processed. See you soon! :)
        """)
        break

    while True:
        LastName = input("Enter the customer's last name: ").title()
        if LastName == "":
            print("Please try again. Customer's last name cannot be empty.")
        else:
            break

    FullName = FirstName + " " + LastName

    while True:
        StAdd = input("Enter the customer's street address: ").title()
        if StAdd == "":
            print("Please try again. Street address cannot be empty.")
        else:
            break

    while True:
        city = input("Enter the customer's city: ").title()
        if city == "":
            print("Please try again. City cannot be empty.")
        else:
            break

    provinces = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
    while True:
        province = input("Enter the customer's province (Ex: NL): ").upper()

        if province == "":
            print("Please try again. Province cannot be empty.")
        elif len(province) > 2:
            print("Please try again. Enter province abbreviation. (Ex: NL)")
        elif province not in provinces:
            print("Please try again. Entry is not a valid response.")
        else:
            break

    while True:
        PostCode = input("Enter the Customer's Postal Code (X1X1X1): ").upper()

        if PostCode == "":
            print("Please try again. Customer name cannot be empty.")
        else:
            break

    while True:
        PhoneNum = input("Enter the customer's phone number (9999999999): ")

        if PhoneNum == "":
            print("Please try again. Phone number cannot be empty.")
        elif not PhoneNum.isdigit():
            print("Please try again. Phone number must be entered with digits only.")
        else:
            break
    PhoneNum = "(" + PhoneNum[0:3] + ")" + " " + PhoneNum[3:6] + "-" + PhoneNum[6:]

    while True:
        NumCars = int(input("Enter the number of cars being insured: "))

        if NumCars == "":
            print("Please try again. Number of cars cannot be empty. Enter at least 1 vehicle.")
        else:
            break

    YNlist = ["Y", "N"]
    while True:
        ExLiabCoverage = input(
            "Would the customer like to purchase extra liability? (Y/N): ").upper()

        if ExLiabCoverage == "":
            print("Please try again. Entry cannot be empty.")
        elif ExLiabCoverage not in YNlist:
            print("Please try again. You must type Y for Yes or N for No.")
        else:
            if ExLiabCoverage == "Y":
                ExLiabCoverageDsp = "Yes"
            else:
                ExLiabCoverageDsp = "No"
            break

    while True:
        GlassCoverage = input(
            "Would the customer like to purchase extra glass coverage? (Y/N): ").upper()

        if GlassCoverage == "":
            print("Please try again. Entry cannot be empty.")
        elif GlassCoverage not in YNlist:
            print("Please try again. You must type Y for Yes or N for No.")
        else:
            if GlassCoverage == "Y":
                GlassCoverageDsp = "Yes"
            else:
                GlassCoverageDsp = "No"
            break

    while True:
        LoanerCoverage = input("Does the customer need rent a loaner car? (Y/N): ").upper()

        if LoanerCoverage == "":
            print("Please try again. Entry cannot be empty.")
        elif LoanerCoverage not in YNlist:
            print("Please try again. You must type Y for Yes or N for No.")
        else:
            if LoanerCoverage == "Y":
                LoanerCoverageDsp = "Yes"
            else:
                LoanerCoverageDsp = "No"
            break

    PayOptions = ["F", "M"]
    while True:
        PayOptions = input("Enter M for Monthly payment or F for full payment: ").upper()

        if PayOptions == "":
            print("Please try again. Entry cannot be empty.")
        elif PayOptions not in PayOptions:
            print("Please try again. You must enter M for Monthly payment or F for full payment.")
        else:
            if PayOptions == "F":
                PayOptionsDsp = "Paid in Full."
            else:
                PayOptionsDsp = "Monthly Payment."
            break

    # Program Calculations:

    ExCostOne = 0
    if NumCars == 1:
        ExCostOne = BasicPremium
    else:
        ExCostOne = BasicPremium + (NumCars - 1) * BasicPremium * AddCarDiscount

    ExCostTwo = 0
    if ExLiabCoverage == "N":
        ExCostTwo = 0
    else:
        ExCostTwo = ExLiabFee * NumCars

    ExCostThree = 0
    if GlassCoverage == "N":
        ExCostThree = 0
    else:
        ExCostThree = GlassCoverageFee * NumCars

    ExCostFour = 0
    if LoanerCoverage == "N":
        ExCostFour = 0
    else:
        ExCostFour = LoanerCoverageFee * NumCars

    TotalExtra = ExCostOne + ExCostTwo + ExCostThree + ExCostFour

    TotalPremium = BasicPremium + TotalExtra
    HstCost = TotalPremium * HstRate
    TotalCost = TotalPremium + HstCost
    CurDate = datetime.datetime.now()
    InvDate = CurDate.date()

    if PayOptions == "F":
        Payment = TotalCost
    else:
        Payment = (TotalCost + ProFeeMonPay) / 8
        NextMonth = CurDate.month % 12 + 1
        NextYear = CurDate.year if NextMonth != 1 else CurDate.year + 1
        NextPayDate = CurDate.replace(month=NextMonth, year=NextYear, day=1)

        # Progress bar to display while information is saving in program.

        print("Please be patient. Insurance Claim being processed...")
        for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="\033[36m{desc}  {bar}"):
            time.sleep(.1)
        print("Insurance claim information saved successfully.")
        time.sleep(1)


    # Formatted Outputs to display:

    TotalExtraDsp = "${:,.2f}".format(TotalExtra)
    TotPremiumDsp = "${:,.2f}".format(TotalPremium)
    HstCostDsp = "${:,.2f}".format(HstCost)
    TotalCostDsp = "${:,.2f}".format(TotalCost)

    print()
    print(" =======================================================")
    print(" =======================================================")
    print("               One Stop Insurance Company")
    print("                    Customer Invoice")
    print(" =======================================================")
    print(" =======================================================")
    print()
    print(f" Invoice Date:                    {InvDate}")
    print(f" Customer Name:                   {FullName}")
    print()
    print(f" Address:                         {StAdd:<20s}")
    print(f"                                  {city}, {province}, {PostCode}")
    print()
    print(f" Phone Number:                    {PhoneNum:<10s}")
    print(f" Number of cars insured:          {NumCars}")
    print(f" Extra Liability:                 {ExLiabCoverageDsp}")
    print(f" Glass Coverage:                  {GlassCoverageDsp}")
    print(f" Optional Loaner:                 {LoanerCoverageDsp}")
    print(f" Total Extra Charges:             {TotalCostDsp}")
    print(f" Total Premium Cost:              {TotPremiumDsp}")
    print(f" HST Cost:                        {HstCostDsp}")
    print(f" Total Cost:                      {TotalCostDsp}")
    print(f" Payment:                         {PayOptionsDsp}")

    if PayOptions == "M":
        print(f" Monthly Payment:             ${Payment:,.2f}")
        print(f" Next Payment Date:            {NextPayDate.strftime('%B %d, %Y')}")
    print()
    print(" =======================================================")
    print(" =======================================================")
    print()
    print("   Thank you for choosing One Stop Insurance Company.")
    print("            We hope to see you again soon!")
    print()
    print("               www.onestopinsurance.com")
    print()
    print(" =======================================================")
    print(" =======================================================")


    # Write the values to a file for future reference.

    f = open("Policies.dat", "w")
    f.write(f"{NextPolicyNum}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{FullName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{city}, ")
    f.write(f"{province}, ")
    f.write(f"{PostCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{ExLiabFee}, ")
    f.write(f"{GlassCoverageFee}, ")
    f.write(f"{LoanerCoverageFee}, ")
    f.write(f"{PayOptionsDsp}, ")
    f.write(f"{TotalPremium}\n")
    f.close()

    # Increase policy number by 1 and write the current values back to the defaults file.

    NextPolicyNum += 1
    f = open("OSICDef.dat", "a")
    f.write(f"{NextPolicyNum}\n")
    f.write(f"{BasicPremium}\n")
    f.write(f"{AddCarDiscount}\n")
    f.write(f"{ExLiabCoverage}\n")
    f.write(f"{GlassCoverage}\n")
    f.write(f"{LoanerCoverage}\n")
    f.write(f"{HstRate}\n")
    f.write(f"{ProFeeMonPay}\n")
    f.close()






