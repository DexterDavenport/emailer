'''
This file is for testing purposes. It will generate
a list of two contacts. The contacts will all be 
your email. All of the last names will be numbered.
The numbers are to assure that the emails being sent 
are unique
'''

with open("login.txt") as pf:
    lines = pf.read() 
    login = lines.split('\n')

print(login)

email = login[0]
cur_path = login[2]
f_name = login[3]
l_name = login[4]
count = 0

for i in range(200):
    count += 1
    with open(cur_path + 'email_list.txt', 'a') as add_sent:
        user = email + ' ' + f_name + ' ' + l_name + f'{count}'
        add_sent.write(user + '\n')
        print(f'{user} added')
print('\nCompleted!!!\n')
