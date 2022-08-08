cur_path = '/Users/dexterdavenport/Desktop/Random Projects/emailer/'
count = 0

for i in range(200):
    count += 1
    with open(cur_path + 'email_list.txt', 'a') as add_sent:
        user = 'dex.davenport1@gmail.com Our Friend' + f'{count}'
        add_sent.write(user + '\n')
        print(f'{user} added')
print('\nCompleted!!!\n')
