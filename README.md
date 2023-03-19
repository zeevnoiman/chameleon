We will create here a simple project to play the chameleon game online using python on backend and react on frontend

The chameleon game is a basic group game. On every turn every participant receives a word, but one receives the chameleon. On each turn all participants insert a word that can be connected to the received word, and after looking into all the words the group has to decide who is the chameleon and vote. The end of each turn the chameleon can guess the word
The system of the points is:
1) For every vote that the real chameleon receives, he loses 1 point
2) Everyone that votes on the real chameleon receives 1 point
3) Everyone that is not a chameleon loses 2 point for every vote received
4) Everyone who is not a chameleon and dit not receive any votes receives one point
5) if the chameleon guesses the word he receives 3 points and the rule number 4 is not applied

installing and running instructions
 - To run the environment, create and activate a virtual environment inside the backend directory
 - activate the virtual env
 - Makefile targes:
    - install-requirements - will install all requirements using pip3
    - run-backend
    - run-backend-debug

 Technical path
 - build service to get words from public api
 - implement logic to every connected people receive the word
 - implement logic to receive a word from every people
 - implement logic to show every connected people with the last chosen word
 - implement logic to receive a suspect from every participant
 - implement pontuation logic
