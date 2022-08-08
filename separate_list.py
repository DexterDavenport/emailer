'''
The connection WILL crash, it can be started every 4-6 minutes

With this version, there is less reliablity of keeping track
of the sent emails. The emails are added the sent list before 
they are sent. This may be fixable with a larger testing list. 
'''
cur_path = '/Users/dexterdavenport/Desktop/Random Projects/emailer/'

import smtplib
import time
from email.message import EmailMessage
from multiprocessing import Pool

# define start time to keep track of time elapsted
start = time.time()

# Email sending the messages
e_address = ''
# Application password for email created for project
e_password = ''

def main(list):
    for i in list:
        # split up the item
        info = i.split(' ')
        contact = info[0]
        f_name = info[1]
        l_name = info[2]

        count = 0

        # Create a for loop so email is not sent as a chain (All emails send individually)
        msg = EmailMessage()
        msg['Subject'] = 'This email was sent using Python 3.10.3'
        msg['From'] = e_address
        msg['To'] = contact
        msg.set_content('This email is sent through a python scripts. The script was created by following allong with this video: https://www.youtube.com/watch?v=JRCJ6RtE3xU')

        # This is a way to send html emails (create html file and send it as is as an email)
        msg.add_alternative(f"""

        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:slateblue;">The content of this email is writen in HTML</h1>
                <p>This email was sent using python to {f_name + ' ' + l_name} at {contact}</p>
                <img src="https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/a1ecd58015f4fd4e86296872a9ce8969~c5_100x100.jpeg?x-expires=1659819600&x-signature=IB7IW8jyUGJwjsWSRQ02oDJkTqs%3D" alt="card"
                width="100" 
                height="100" >
            </body>
            <footer>
            <p>
            this is the footer
            </p>
            </footer>
        </html>

        """
        , subtype='html')

        # create the connection to the gmail application and send the message
        with smtplib.SMTP_SSL('smtp.gmail.com', 465 ) as smtp:
            smtp.login(e_address, e_password)
            smtp.send_message(msg)

        count +=1
        print(f'Message sent to {f_name} {l_name} sucessfully!!\n')

def make_list(list):
    for i in range(20):
        # get the first line
        with open(cur_path + "email_list.txt") as email:
            lines = email.read() 
            line = lines.split('\n', 1)[0]
        if line != '':
            # split up the line into email first and last name
            info = line.split(' ')
            contact = info[0]
            f_name = info[1]
            l_name = info[2]

            list.append(line)

            # rewrite the file without that item in it
            with open(cur_path + 'email_list.txt', 'r') as just_read:
                data = just_read.read().splitlines(True)
            with open(cur_path + 'email_list.txt', 'w') as rewrite:
                rewrite.writelines(data[1:])

            # place the sent email in the send_emails file
            with open(cur_path + 'sent_emails.txt', 'a') as add_sent:
                add_sent.write(contact + ' ' + f_name + ' ' + l_name + '\n')

if __name__ == '__main__':
    with smtplib.SMTP_SSL('smtp.gmail.com', 465 ) as smtp:
        smtp.login(e_address, e_password)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    make_list(list1)
    make_list(list2)
    make_list(list3)
    make_list(list4)
    make_list(list5)
    with Pool(5) as p:
        p.map(main, [list1,list2,list3,list4,list5])
        end = time.time()
        print(f"\nCompleted in {round(end - start, 2)} seconds!!!\n")

# '''
# 5 = 107, 109 emails
# 6 = 114, 114, 117 emails
# 7 = 103, 122, 124 emails
# 8 =  99, 116 emails
# '''

