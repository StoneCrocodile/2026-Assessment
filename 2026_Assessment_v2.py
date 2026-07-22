def string_check(question, valid_answer=('yes', 'no', 'Kg', 'g', 'ml', 'L', 'each'),
                 num_letters=1):
    """Checks that users enter the full word
     or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answer:

            # check if the response is the entire word
            if response == item:
                return item

        # check if it's the first letter
            elif response == item[ :num_letters]:
                return item

        print(f"Please choose an option from {valid_answer}")


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''This program will ask you for... 
    - the program is made to compare 2 items at a time.
    - The name of the products you are comparing 
    - How many items you plan on comparing
    - The costs for each of the products you are comparing
      (variable expenses)
    - the unit of the item (kg,L, or each)


The data will be put into a table and tell you which item is 
the cheaper option 

    ''')


def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)



# Main Routine


print(make_statement("Price Comparison Calculator", "-"))

print()
want_instructions = string_check("Do you want to see the instructions?")
print()

if want_instructions == "yes":
    instructions()
print()

# Get Budget, more than $10...
print("Please Input A Budget $10 Or More")
while True:
    get_budget = num_check("Budget: $", "integer",)
    if get_budget <= 9:
        print("Budget Must Be $10 Or More")
        continue
    break

# Get items
print("Lets Get Your Two Items To Compare...")
get_items = not_blank("Item name: ")
unit_weight = string_check("Unit Of Measurement for Item: ","Kg, g, ml, L, or each")
get_weight = num_check("Total Weight Or Amount Of Items:", "float")
item_cost = num_check("Cost Of Items (per item or per kg / L):", "float")
total_cost_calc = get_weight * item_cost
total_cost = total_cost_calc

get_items_2 = not_blank("Second Item name:")
unit_weight_2 = string_check("Unit Of Measurement for Second Item: ", "Kg, g, ml, L, or each")
get_weight_2 = num_check("Total Weight Or Amount Of Items:", "float")
item_cost_2 = num_check("Cost Of Items (per item or per kg / L):", "float")
total_cost_calc_2 = get_weight_2 * item_cost_2
total_cost_2 = total_cost_calc_2

print("The Total Cost For Your First Items is:", total_cost)
print("The Total Cost For Your Second Items is:", total_cost_2)


