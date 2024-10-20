# Secure Fair Voting System

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Secure Voting**: Ensures that voters can cast their votes securely.
- **User Authentication**: Voter registration and login functionality.
- **Candidate Management**: Add, update, and delete candidates.
- **Vote Counting**: Automated counting of votes with validation.
- **Vote History**: Track whether a voter has voted or not.
- **RESTful API**: Full API for integrating with frontend applications.

## Installation

To set up the Secure Fair Voting System on your local machine, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Django 5.1 or higher
- Django REST Framework
- Git

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/your-username/secure-fair-voting-system.git
cd secure-fair-voting-system

Step 2: Create a Virtual Environment

python -m venv venv

Activate the virtual environment:

venv\Scripts\activate

Step 3: Install the required packages using pip:

pip install -r requirements.txt

Step 4: Set Up the Database
Run the following commands to set up your database:

python manage.py makemigrations
python manage.py migrate

Step 5: Create a Superuser
To access the admin panel, create a superuser account:

python manage.py createsuperuser

Step 6: Run the Development Server
Start the server using:


python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

Usage
Navigate to the Admin Panel: Go to http://127.0.0.1:8000/admin/ and log in with the superuser account you created.
Manage Voting Rooms: Add voting rooms, candidates, and voters.
Voting Process: Voters can log in and cast their votes.
API Endpoints
Voting
POST /api/vote/: Cast votes for candidates.
Request Body:

json
Copy code
{
    "voter": 1,  // ID of the voter
    "votes": [
        {
            "candidate": 1,  // ID of the candidate
            "votes_count": 6  // Number of votes for this candidate
        },
        {
            "candidate": 2,
            "votes_count": 4
        }
    ]
}
Candidates
GET /api/candidates/: Retrieve all candidates.
POST /api/candidates/: Add a new candidate.
Voters
GET /api/voters/: Retrieve all voters.
POST /api/voters/: Register a new voter.