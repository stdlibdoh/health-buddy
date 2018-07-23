# health-buddy

## Intro

This project was made by Wilson Tolentino da Silva and Bevis Halsey-Perry for "Hack Your FoFo", a hackathon held on the 19th and 20th of July, 2018.

## Concept

We focused on creating dynamic communities, with the goal of promoting communication between folks suffering from a common illness or with a particular goal, such as improving an area of their health. 

We theoreised that, by doing this, an individual would better take control of their health by communicating with like minded individuals and, in turn, be better equipped to deal with issues that they're facing. 

We also believe that, while direct communication is a good step, certain automation of tasks could also be advantageous, with certain chat-ops taking place in the backgroung. 

An example of this could be having a bot messaging the individual inquiring whether they have visited the GP recently or made their scheduled appointments. 

## Implementation

While group messaging can be implemented on different stacks, we focused on SMS, as we believe it has the highest level of impact/adoption as everyone has access to such a technology.

In order to do that, we leveraged the Twilio API that allows developers to create a phone number and send/receive sms messages. This API could also be used for voice communication, which would be required for purposes of accessibility, yet this aspect wasn't explored.

Our application wasn't completed. Created was:
*  a custom API with a database in SQLite, with simple CRUD operations for users 
*  an onboarding application that asked a series of questions that collected information on the new user. This could then be used to communicate with the previously mentioned API.

Both applications were created with Python3, Flask.

## Usage

### Onboard & API

Two folders hold each app, with _hb-backend_ holding the API and _hb-onboard_ holding the onboarding application. 

* Create and activate new virtual environment.
* Install required modules from _requirements.txt_.

* Initialise the database by running:

```
> export FLASK_APP=flask-twilio-frontend.py
> flask db init
> flask db migrate
> flask db upgrade
```

Replace _flask-twilio-frontend_ with _health-buddy_ for API backend.

* A list of questions for the onboarding process can be found in the _hb-onboard/onboarding.json_ file. Populate the database with JSON questions by running:

```
> python flask-twilio-frontend.py dbseed
```

* Run the flask server by running:

```
> flask run
```

This will be accessible on localhost:5000. In order to communicate with Twilio, we need to have a discoverable URL. We recommend _ngrok_ to do this.

### Twilio

A Twilio account is required. Once registered, you'll need to create a Twilio number and configure it so that the message URL is pointing to the location of our exposed ngrok URL. 

## Presentation

[See our presentation](https://slides.com/bevishalsey-perry/health-buddy#/)

## References

* [Flask Documentation](http://flask.pocoo.org/docs/1.0)
* [Twilio Home](https://www.twilio.com/)
* [Twilio Survey](https://www.twilio.com/docs/voice/tutorials/automated-survey-python-flask)