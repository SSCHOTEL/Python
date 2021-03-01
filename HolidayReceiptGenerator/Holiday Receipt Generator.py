#Variables declared that are used for the reciept generation. 
cost = 199.99
subtotal = {"Item 7": 149.99,
            "Item 14": 30.00,
            "Item 18": 20.00}
discount = 40.00
totalCost = cost + discount 
currency = "£"

def validateInput(inp, check=""):
    """Fetch and validate a user input.

    Parameters
    ---------------
    inp : str
        Prompt for the input.
    check : str (default="")
        Validate the input against criteria based on the value of this variable.
        - Use "number" to check if the input is a float.
        - Use "date" to check if the input is formatted as a date.
        - Use "email" to check if the input is formatted as an email.

    Returns
    ---------------
    str
        Validated user input.
    """
    out = False
    while out == False: 
        out = True
        val = input(f"Enter your {inp}: ")

        if check == "stringvalcheck":
            numError = False
            if len(val) > 3:
                out = True
            else:
                print("Please enter into field.")
                out = False


        if check == "pncheck":
            numError = False
            if len(val) < 5:
                print("Enter Valid Number")
                out = False
            else:
                out = True

        if check == "budgetc":
            numError = False
            if len(val) < 3:
                out = False
                print("Enter Whole Number")
            else:
                out = True



        if check == "number": 
            numError = False
            for i in val.split("."):
                if not i.isdigit: 
                    numError = True
                out = False 
            if numError:
                print("You have to input a decimal number.")

        #Check if input is a date.
        if check == "date":
            if len(val) == 10:
                if val[:2].isdigit() or val[3:5].isdigit() or val[5:].isdigit(): 
                    out = True
                if not val[2] == "/" or not val[5] == "/":
                    print("You have to use '/' as the date separator.")
                    out = False
            else:
                print("The date has to be in the format DD/MM/YYYY")
                out = False

        #Check if input is an email.
        if check == "email" and not val.count("@") == 1: 
            out = False
            print("An email address must contain one @ symbol")
    
    return val

def currencyFormatting(value):
    """Format a float to be outputted as a currency."""
    splitValue = str(value).split(".")
    if len(splitValue) == 2: 
        while len(splitValue[1]) > 2:
            splitValue[1] += "0"
    else:
        print("Error: value for currency should only have one decimal point.")
    return currency + splitValue[0] + "." + splitValue[1]

#Get customer details.
customerDetails = []
customerDetails.append(validateInput("Name", "stringvalcheck"))
customerDetails.append(validateInput("Address", "stringvalcheck"))
customerDetails.append(validateInput("Phone Number", "pncheck"))
customerDetails.append(validateInput("Departure Date (DD/MM/YYYY)", "date"))
customerDetails.append(validateInput("Return Date (DD/MM/YYYY)", "date"))
customerDetails.append(validateInput("Email", "email"))
customerDetails.append(validateInput("Destination", "stringvalcheck"))
budget = validateInput("budget", "budgetc")
extraItem = validateInput("additional items")

#Reciept generation.
out = f"Name:           {customerDetails[0]}\n" 
out += f"Address:        {customerDetails[1]}\n"
out += f"Phone Number:   {customerDetails[2]}\n"
out += f"Departure Date: {customerDetails[3]}\n"
out += f"Return Date:    {customerDetails[4]}\n"
out += f"Email:          {customerDetails[5]}\n"
out += f"Destination:    {customerDetails[6]}\n"
out += "="*40 + "\n"
out += f"Cost:" + " "*28 + f"{currencyFormatting(cost)}\n"
for i in subtotal:
    out += f"    {i}:" + " "*(28-len(i)) + f"{currencyFormatting(subtotal[i])}\n"
if discount != 0:
    out += f"Discount:" + " "*23 + f"-{currencyFormatting(discount)}\n"
out += f"Total:" + " "*27 + f"{currencyFormatting(totalCost)}\n"
print(out)
 
with open("reciept.txt", "w") as txt:
    txt.write(out)