#######
### Scientific Computing with Python Projects 
### Budget App
### https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
#######


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.withdraw_all = list()

    """
    When the budget object is printed it should display:
    A title line of 30 characters where the name of the category is centered in a line of * characters.
    A list of the items in the ledger. Each line should show the description and amount. 
    The first 23 characters of the description should be displayed, then the amount. 
    The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    A line displaying the category total."""

    def __str__(self) -> str:
        first_row = self.name.center(30, "*")
        n = 0
        result_list = []
        for dict in self.ledger:
            for values in dict:
                x = dict["amount"]
                y = dict["description"]
            result_list.append(list(dict.values()))
        n = n + 1
        result_str = ""
        for l in result_list:
            number = str(f"{(float(l[0])):.02f}")
            result_str = (
                result_str
                + f"{l[1][0:23]}{number[0:7].rjust(30-len(l[1][0:23]))}"
                + "\n"
            )

        last_row = f"Total: {float(self.get_balance()):.02f}"
        return first_row + "\n" + result_str + last_row

    """A deposit method that accepts an amount and description. 
    If no description is given, it should default to an empty string. 
    The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    """

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    """
    A withdraw method that is similar to the deposit method, 
    but the amount passed in should be stored in the ledger as a negative number. 
    If there are not enough funds, nothing should be added to the ledger. 
    This method should return True if the withdrawal took place, and False otherwise."""

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            self.withdraw_all.append({"amount": amount, "description": description})
            return True
        else:
            return False

    """A get_balance method that returns the current balance of the budget category 
    based on the deposits and withdrawals that have occurred.
    """

    def get_balance(self):
        self.funds = 0
        n = 0
        for _ in self.ledger:
            self.funds = self.funds + self.ledger[n]["amount"]
            n = n + 1
        return self.funds

    """
    A transfer method that accepts an amount and another budget category as arguments. 
    The method should add a withdrawal with the amount and the description 
    "Transfer to [Destination Budget Category]". 
    The method should then add a deposit to the other budget category 
    with the amount and the description "Transfer from [Source Budget Category]". 
    If there are not enough funds, nothing should be added to either ledgers. 
    This method should return True if the transfer took place, and False otherwise.
    """

    def transfer(self, amount, obj):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {obj.name}")
            obj.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    """A check_funds method that accepts an amount as an argument. 
    It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
    This method should be used by both the withdraw method and transfer method.
    """

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


"""
Besides the Category class, create a function (outside of the class) called create_spend_chart 
that takes a list of categories as an argument. It should return a string that is a bar chart.
The chart should show the percentage spent in each category passed in to the function. 
The percentage spent should be calculated only with withdrawals and not with deposits. 
Down the left side of the chart should be labels 0 - 100. 
The "bars" in the bar chart should be made out of the "o" character. 
The height of each bar should be rounded down to the nearest 10. 
The horizontal line below the bars should go two spaces past the final bar. 
Each category name should be written vertically below the bar. 
There should be a title at the top that says"""


def create_spend_chart(categories=list()):
    perc_results = []
    max_name = (
        []
    )  # lista nazw aby wybrać najdłuższą dla okręlsnia rozmiaru tabeli w dół
    # total withdraw in all categories
    total_withdraw_all_cat = 0
    for l in categories:
        total_withdraw_cat = 0
        for dict in l.withdraw_all:
            total_withdraw_cat += dict["amount"]
        total_withdraw_all_cat += total_withdraw_cat

    # percentage for category
    for l in categories:
        total_withdraw_cat = 0
        for dict in l.withdraw_all:
            total_withdraw_cat += dict["amount"]

        l.perc_withdraw = (total_withdraw_cat / total_withdraw_all_cat) * 100
        l.perc_withdraw = round(int(l.perc_withdraw / 10)) * 10

        # circle list
        l.circle_number = int(l.perc_withdraw / 10)
        l.circle_lst = []
        for _ in range(l.circle_number + 1):
            l.circle_lst.append("o")
        for _ in range(10 - l.circle_number):
            l.circle_lst.append(" ")

        l.circle_lst.reverse()
        max_name.append(len(l.name))
        perc_results += [{"name": l.name, "circle": l.circle_lst}]

    ####
    f_row = "Percentage spent by category" + "\n"

    circle_rows_full = ""
    perc_chart = [
        "100|",
        "90|",
        "80|",
        "70|",
        "60|",
        "50|",
        "40|",
        "30|",
        "20|",
        "10|",
        "0|",
    ]

    for x in range(11):
        circle_rows_p1 = f"{perc_chart[x].rjust(4)} "
        circle_rows_p2 = ""
        for y in range(len(perc_results)):
            circle_rows_p2 = circle_rows_p2 + f"{perc_results[y]['circle'][x]}  "

        circle_rows = circle_rows_p1 + circle_rows_p2 + "\n"
        circle_rows_full += circle_rows

    middle_row = "    -" + "---" * (len(perc_results)) + "\n"
    name_rows_all_lst = []
    name_rows_all = ""
    for a in range(max(max_name)):
        name_row = ""
        name_row_lst = []
        for b in range(len(perc_results)):
            try:
                name_row = name_row + f"{perc_results[b]['name'][a]}  "
            except IndexError:
                name_row = name_row + "   "
        name_row = "     " + name_row
        name_row_lst.append(name_row)
        name_rows_all = name_rows_all + name_row + "\n"
    name_rows_all = name_rows_all.rstrip("\n")
    name_rows_all_lst.append(name_rows_all)
    chart = f_row + circle_rows_full + middle_row + name_rows_all
    return chart


## END ################
#####
### EXAMPLES

# full_list = []
# full_list.append(f_row)
# full_list.append(circle_rows_full)
# full_list.append(middle_row)
# full_list.append(name_rows_all)
# print(full_list)
# print(f_row)
# print(circle_rows_full)
# print(middle_row)
# print(name_rows_all)
# print(name_rows_all_lst)
# food = Category("Food")
# #print(food)
# food.deposit(100.45, "banany")
# food.deposit(50.12, "banany")
# food.withdraw(10.99, "banany")
# food.withdraw(60.98)
# #food.deposit(100)
# #print(food.funds)
# #print(food.ledger, "food.ledger")
# #print(food.deposit, "food.deposit")
# #print(food.funds)
# #print(food.get_balance(), " food funds przed")

# #print(food.name)

# cloth = Category("Cloth")
# #print(food)
# cloth.deposit(100, "kurtka")
# cloth.deposit(90, "buty")
# cloth.withdraw(60, "spodnieeeeeeeeeeeeeeeeeeeeeeeeee")
# cloth.withdraw(10000)
# cloth.deposit(1000, "depozyt111111")
# #print(cloth.ledger)
# #print(cloth.get_balance(), "cloth funds przed" )


# cloth.transfer(100, food)
# # print(cloth.ledger, " CLOTH LEDGER")
# # print(cloth.get_balance(), "cloth funds")
# # print(food.ledger, "FOOD ledger")
# # print(food.get_balance(), "food funds")

# food.transfer(14, cloth)
# # print(cloth.ledger, " CLOTH LEDGER")
# # print(cloth.get_balance(), "cloth funds")
# # print(food.ledger, "FOOD ledger")
# # print(food.get_balance(), "food funds")

# entert = Category("Entertainment")
# #print(food)
# entert.deposit(500, "dep 1")
# entert.deposit(500, "dep 1")
# entert.withdraw(10, "lololo")
# entert.withdraw(1100)
# entert.withdraw(100, "elloello")


# # print(food)
# # print(cloth)
# # print(entert)

# print(create_spend_chart([food, cloth, entert]))

business = Category("Business")
food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))

#print(business)
