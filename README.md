# University of Zimbabwe BEM Chatbot Assistant

![Chatbot Image](https://storage.googleapis.com/intellixbot-jqcj.appspot.com/chatbot.jpeg)

This chatbot assistant for the Business Enterprise Management (BEM) program at the University of Zimbabwe is created using Rasa, an open-source machine learning framework for building conversational AI.

## Getting Started

To get started with the chatbot, you will need to clone the repository. You can do this by running the following command:

`git clone https://github.com/TinasheMashaya/BEM`

Once you have cloned the repository, navigate to the BEM directory using the following command:

`cd BEM`

## Training the Chatbot

To train the chatbot, run the following command:

`rasa train`

This will train the chatbot using the training data provided in the repository.

## Running the Chatbot In An Interactive Environment

To run the chatbot in interactive mode, run the following command:

`rasa interactive --debug`

This will start the chatbot in interactive mode, allowing you to chat with it and test its functionality.

## Serving the Bot Through Twilio And Ngrok
Prerequisites: CONFIGURED TWILIO WHATSAPP ACCOUNT AND NGROK INSTALLED ON LOCAL MACHINE

Open credential.yml file and change the following to your twilio credentials:

```twilio:
    account_sid: "ACbc2dxxxxxxxxxxxx19d54bdcd6e41186"
    auth_token: "e231c197493a7122d475b4xxxxxxxxxx"
    twilio_number: "whatsapp:+440123456789"
```
Run the server:
`rasa run --model models --enable-api --cors "*"`

In another terminal run the action server:
`rasa run actions`

Open a ngrok http tunnel at port 5005 in another terminal:
`ngrok http 5005`

Copy and paste the ngrok_generated_https_url/webhooks/twilio/webhook to the Twilio webhooks on your twilio web dashboard eg `https://cac1-196-4-80-2.eu.ngrok.io/webhooks/twilio/webhook`

Check the status of your local server using:
`ngrok_generated_https_url/webhooks/twilio`

If you get {"status":"ok"} you are ready to test the bot on whatsapp

## Contributing

If you'd like to contribute to the development of the chatbot, feel free to fork the repository and submit a pull request with your changes.
