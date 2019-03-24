# telegram-notify

This project was created on vanhackaton 2019.
It's a simple api build with flask that accepts json posts and send the data to a telegram channel.
The application have one endpoint called tgmessage tha only supports the POST method.

The ideia behind the project it's to create a simple integration between traction guest and telegram
using GuestConnect.

# Required environment variables
* SECRET_KEY
* TOKEN - this token will be used to allow the access to the endpoint (on the future is better to use jwt)
* TELEGRAM_TOKEN - get this token creating a bot. Click [HERE](https://core.telegram.org/bots) to see how to create bots
* TELEGRAM_CHATID - the id or channel name that the bot will send the messages.

# CI/CD
I'm using [circleci](https://circleci.com) to run the tests and deploy the code on heroku (https://tractionguest-telegram-notify.herokuapp.com/tgmessage)
Here are the pipelines of this application on circleci (https://circleci.com/gh/drael/telegram-notify-vanhack)

# Public telegram channel
Here are the public channel (https://t.me/tractionguestalerts) where the production app on heroku are sending the messages.
If you want to try the version running on heroku, send me a message draelmaster@gmail.com and I send you the access token.

# How To send a message
You should send a post with a valid json data and the correct content-type **application/json** and a valid **token** header

Example of a http post:

```sh
curl -X POST -k -H 'Content-Type: application/json' -H 'token: TOKENHERE' -i 'https://tractionguest-telegram-notify.herokuapp.com/tgmessage' --data '"{'\''name'\'': '\''Rafael'\'', '\''company'\'': '\''Traction Guest'\''}"'
```
