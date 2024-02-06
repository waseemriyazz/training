# 8.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# google

# In case of input data being supplied to the question, it should be assumed to be a console input.

def get_company_name(email):
    company_name = ""
    flag = 0
    for i in range(0, len(email)):
        if email[i]==".":
            flag = 0

        if flag == 1:
            company_name = company_name + email[i]
            
        if email[i]=="@":
            flag = 1

        
    return company_name

print(get_company_name("john@google.com"))