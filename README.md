# telegram-notify

This project was created on vanhackaton 2019.
It's a simple api build with flask that accepts json posts and send the data to a telegram channel.

The ideia behind the project it's to create a simple integration between traction guest and telegram
using GuestConnect.

# Required environment variables
* SECRET_KEY
* TOKEN - this token will be used to allow the access to the endpoint (on the future is better to use jwt)
* TELEGRAM_TOKEN - get this token creating a bot. Click [HERE](https://core.telegram.org/bots) to see how to create bots
* TELEGRAM_CHATID - the id or channel name that the bot will send the messages.
