# health-buddy

## Intro

This project was made by Wilson Tolentino da Silva and Bevis Halsey-Perry for "Hack Your FoFo", a hackathon held on the 19th and 20th of July, 2018.

## Concept

We focused on creating dynamic communities, with the goal of promoting communication between folks suffering from a common illness or with a particular goal, such as improving an area of their health. We theoreised that, by doing this, an individual would better take control of their health by communicating with like minded individuals and, in turn, be better equipped to deal with issues that they're facing. We also believe that, while direct communication is a good step, certain automation of tasks could also be advantageous, with certain chat-ops taking place in the backgroung. An example of this could be having a bot messaging the individual inquiring whether they have visited the GP recently or made their scheduled appointments. 

## Implementation

While group messaging can be implemented on several different stacks, for the hackathon, we focused on SMS as we believe it has the highest level of impact/adoption as everyone has access to such a technology.

In order to do that, we leveraged the Twilio API that allows developers to create a phone number and send/receive sms messages. This API could also be used for voice communication, which would be required for purposes of accessibility, yet this aspect wasn't explored.

Our application wasn't completed. Created was:
*  a custom API with a database in SQLite, with simple CRUD operations for users 
*  an onboarding application that asked a series of questions that collected information on the new user. This could then be used to communicate with the previously mentioned API.

Both applications were created with Python3, Flask.

## Usage

Two folders hold each app, with hb-backend holding the API and hb-onboard holding the onboarding application. A list of required modules is in each folder, named requirements.txt with the necessary Python modules to be installed.