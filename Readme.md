# Sample Python codebase for GitHub Copilot

This repository contains the sample code base for the Github Copilot. This is a Python `Flask API` project that uses the `MongoDB` as the database. Repository contains two folders - `starter` and `finished`. The `finished` directory contains the completed project and the `starter` directory contains the incomplete code. You need to use the `starter` project and complete the project by generating code using `GitHub Copilot`.

### Steps to execute
- Clone the repository to local machine. Use `git clone https://github.com/sonusathyadas/github-copilot-codebase`.
- Open the Command Terminal in `starter` directory.
- Create a Python virtual environment using `python -m venv .venv` command.
- Activate the virtual environment bu using the `.venv\Scripts\Activate`.
- Install the required packages using the `pip install -r requirements.txt` command.
- Open the `apis\books_api.py` file and use the given comments in file to generate code.
- Open the `app.py` file and use the given comments in file to generate code.
- Update the `.env` file need to change the MongoDB connection settings if required.
- Run the project using `python app.py` or `flask run --port 5000 --debug` command. 