
print("Welcome to Tip Calculator\n")
total_amt = input("Enter the total amount of bill ₹ ")
no_of_people = input("Between how many people this amount should be divided? ")
tip_percent = input("How much would you like to tip? 10, 20, 30 ")

final_sum = float(total_amt) + float(total_amt)*int(tip_percent)/100

each_contri = final_sum/int(no_of_people)
print("Each person has to pay ₹ {}".format(each_contri))
