World of Games (WOG)
Welcome to World of Games! Enjoy three entertaining games: Memory Game, Guess Game, and Currency Roulette. Each game offers different difficulty levels to challenge your skills.

How to Run
To get started with the game, simply run main.py:

bash
Copy code
python main.py
End-to-End Testing
To run the end-to-end tests, execute the e2e.py script:

bash
Copy code
python test/e2e.py
This script will test the web service and ensure that the game scores are within the correct range.

Jenkins Pipeline
The Jenkins pipeline is set up to automate the testing and deployment process. It includes the following stages:

Checkout - Fetches the latest code from the repository.
Build - Builds the Docker image for the application.
Run - Runs the Docker container for the application.
Test - Executes the end-to-end tests using e2e.py.
Finalize - Cleans up the Docker containers.
Enjoy playing the World of Games and happy coding!