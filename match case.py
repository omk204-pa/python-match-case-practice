#Write a function get_http_status(code) that takes an integer HTTP status code and returns a human-readable string
get_http_status = int(input("enter your code :"))
match get_http_status:
    case 200:
        print("ok")
    case 400:
        print("bad request")
    case 404:
        print("not found")
    case 500:
        print("internal server error")
    case _:
        print("unknown status")


#Create a function classify_age(age) that uses match-case alongside conditional if guards to categorize a person's life stage

classify_age = 13
match classify_age:
    case int()if (classify_age < 0):
        print("invalid age !")
    case int()if classify_age<=12:
        print("child")
    case int()if classify_age<=19:
        print("teenager")
    case int()if classify_age<=64:
        print("adult")
    case int()if classify_age >65:
        print("senior")

#Write a program using match-case that checks if a person is eligible for a bank loan based on their monthly salary.
salary = 20000
match salary:
    case int()if salary >=50000:
        print("eligible for premium loan")
    case int()if salary<=20000:
        print("eligible for standard loan")
    case int()if salary<20000:
        print("not eligible for loan (salary too low!)")

#Write a program using match-case that checks a user's security role string
role = "developer"
match role:
    case "admin":
        print("full access, can view and edit all databases")
    case "data analyst":
        print("standard access: can read and genetate reports")
    case "guest":
        print("limited access: read only access to files")
    case _:
        print("access denied ! invalid role")




#Write a program using match-case that looks at a customer's delivery
delivery_type = input("enter your order type: ")
match delivery_type:
    case "premium":
        print("shipping cost 100$, delivered on same day when ordered !")
    case "express":
        print("shipping cost 15$, Delivred in 1-2 days")
    case "standard":
        print("shipping cost 5$, delivered in 3-5 days")
    case "free":
        print("shipping cost free!, delivered in 7-10 days")
    case _:
        print("invalid type please check your delivery type..")







    

