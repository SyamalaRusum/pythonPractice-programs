# regex for matching the gmail
import re


def regexp(email):
    return re.search("[a-z 0-9]\w+@[a-z]+\.[a-z]{1,3}$", email)
    # return re.search("^\w+@[a-z]+\.[a-z]{1,3}",email)


# email="rusumsai789@gmail.com"
email = "rusum_sai09@yahoo.com"
print(regexp(email))


# for matching the date
def regex1(date):
    return re.search("(18|19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", date)  # yyyy-mm-dd
    # return re.search("(0[1-9]|1[1,2])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d{2}",date)   #mm-dd-yyyy


date = "1999-10-17"
# date="11-17-2007"
print(regex1(date))


# regex for extracting hashtags# from the text(file-txtfile.txt)
def regex2(hashtxt):
    return re.findall("#\w\S*", hashtxt)


hashtxt = "hello planet - Behave setup and teardown #functions are implemented in a #file called the environment.py which is within the same directory that contains #thestepsfolder. The #setup functions of  #include #707 – browser open, database connection, configurations, and so on.The teardown functions include browser closure, database connection termination, reversing changes, and so on."
print(regex2(hashtxt))


# regex for matching ip address
def regex3(ipaddr):
    return re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ipaddr)


ipaddr = "192.168.7.222"
print(regex3(ipaddr))


# regex for matching words with hyphens(\,\n...)
def regex4(hyphenwords):
    return re.findall("[a-zA-Z]+-[a-zA-Z]+", hyphenwords)
    return re.findall()


hyphenwords = "hello planet-Behave setup and teardown #functions are implemented in a #file called the environment.py which is within the same directory that contains #thestepsfolder. The #setup functions of  #include #707 – browser open, database-connection, configurations, and so on.The teardown-functions include browser closure, database-connection termination, reversing changes, and so on."
print(regex4(hyphenwords))


def regex5(capitals):
    return re.findall("[A-z]+", capitals)


capitals = "Hello World"
print(regex5(capitals))
