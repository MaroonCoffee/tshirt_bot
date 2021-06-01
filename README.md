# T-Shirt Bot

Simple email bot I made to automatically email colleges to give me free stuff. Mostly for t-shirts.

You can find the latest release of the program [here](https://github.com/erose524/tshirt_bot/releases)

[This website](https://freecollegeshirts.weebly.com/) is a great resource to find out how to get started as well as which colleges are most likely to send you shirts back.

## Setting up your Gmail to work with the program
1. Create a Gmail account [here](https://accounts.google.com/SignUp) if you don't already have one. You may want to make a new one regardless for sending emails with the program as you'll see below.

### For users without 2fa enabled
Enable *less secure apps* to access your account [here](https://myaccount.google.com/u/2/lesssecureapps?pli=1&rapt=AEjHL4Nhwqo5YU9RfN7Q_tQV-Wg71VdgMdRuC6CcSx4nP7DolMzITP4l8FsaN3OWf2_ADM4ITKu1urpSWRML9cJAX6dvWD-fJQ) as otherwise the program will be unable to send emails through your account. This is why you might consider creating a new account for this process.
### For users with 2fa enabled
Gmail users with 2fa enabled have to make an app password in order for their account to be compatible with the bot. You can find out more about making an app password [here](https://support.google.com/accounts/answer/185833?hl=en). This app password lets the program bypass your 2fa, thus posing a security risk (again you may consider creating a new Gmail account for security reasons). Despite what the site tells you, take note of the app password you're supplied with as you'll have to provide it each time you use the program.

## Using the program
1. You will want to keep the executable in its own folder as it will create text documents you will need for the program to run correctly.
### For users with 2fa enabled
When the program asks for your password, type your app password as your regular password will not work.
### Setting up message.txt
1. To supply the program with the email you want to send, open the message.txt file (created on program startup the first time) or create one if it's not already there.
2. The first line of this document will be the subject of the email you're sending. After the first line break (enter), all text in the document will be read as the body of the email you're sending. 
3. Your message can be customized through the use of two tags, \[College Name\] and \[Short College Name\]. By inserting those tags throughout your message, you can make your email appear personalized for the college you're emailing. 
 * For example, by typing 
   * "\[College Name\] is the best university! Go \[Short College Name\]!"
 * and supplying the following names into the program
   * "Harvard University" and "Harvard"
 * your email will be sent like this
   * "Harvard University is the best university! Go Harvard!"
4. Finally, it is important that you test this message out by sending it to yourself through the program before attempting to send it to colleges.
### Using logs.txt
After sending your first email using the program, a file called logs.txt will save the name and email of the college you messaged. Make sure to record this information to avoid accidentally messaging the same college twice.
