# Emailer
This program allows anyone with a gmail to be able to send out large amounts of personalized emails for free. 

This current version can add the first and last name of each email to a custom HTML email. 

# Setting up Gmail

When using this program you will have to set up your gmail to allow the program to make a connection to send emails. This is easy to do and only takes a few steps. 

1. Sign in/Create a gmail
2. Make sure 2 Step Verification is TURNED ON
3. Follow [this link](https://myaccount.google.com/apppasswords?rapt=AEjHL4PPV--bCa1iaXPyE5ZtQYZTAqQA2pQGmpJQooNJUxQdudv9__08c2WmqJvqo1AfeoPdZlZz6h6W64q3k6KBclA8o6mbDg) and create an app password. 

    3a. Under Select App, choose other and create a custom name for it.

    3b. Click generate and copy the password that it provides for you.

Save this password for the next step.

# login.txt Setup

In the folder that this project is being saved to, create a file and save it as 'login.txt'. Fill in lines one through five with the following information. 


```
1 sender@gmail.com
2 password
3 /Your/current/path/to/project/
4 firstName
5 lastName
```

<details>
<summary>lines explained</summary>

* Do not include the numbers at the beginning of the line. 
* Do not include spaces before or after the lines

Line one is gmail that you set up at the beginning of this project

Line two is the password that was generated for you at the beginning of this project

Line three is the path to the folder you are saving this project in. Make sure that you include the '/' at the end of the path.

Line four and five will be your first and last name. This is only needed for the 'create_list.py' file which will be explaned later.

</details>

<br>

# create_list.py

The create_list.py file will generate a list of 200 unique names for testing the program. All of the emails will be sent to your personal email that is being used for this project. Each name though will have a number assigned to it. This is only to see that there are no repeats. 

# Run the Program

To run this program simply open the 'program1.py' file. 

BEFORE you do so make sure the email_list.txt is set up properly. This will be done like so:

```
1 email1@email.com Fname Lname1
2 email2@email.com Fname Lname2
3 email3@email.com Fname Lname3
```

<details>
<summary>lines explained</summary>

* Do not include the numbers at the beginning of the line. 

Each line NEEDS to have all three items in it (email, first name, last name). 

Make sure there are no extra spaces on each line, only one after email and one after first name

</details>

<br>

You can have any number of lines in this file but only 100 emails will be sent at a time. 


# WARNING

**Starting the file more than once in less than 4 minutes could result in emails being moved to the 'sent_emails.txt' that were NOT sent. To avoid this only run this program once every 4-6 minutes.**

<br>

NOTE: If program crashes WHILE emails are sending, not all emails in 'sent_emails.txt' were sent. If program crashes before any emails are sent, 'sent_emails.txt' and 'email_list.txt' should not be effected. 

<details>
<summary>NOTE Explained</summary>

When the program is started the emails that are going to be sent are automatically added to the 'sent_emails.txt' list. This is done to prevent data loss to make sure that your list of contacts will be reuseable. 

Work arounds will be added later but may be less secure.

</details>