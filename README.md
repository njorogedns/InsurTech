# InsurTech Web Application

This is a web application built with Flask for managing car insurance policies. Users can register, log in, view their dashboard, select insurance policies, make payments, and manage their loyalty program.

## Features

- **User Authentication:** Users can register and log in securely to access their accounts.
- **Dashboard:** Users can view their profile information, active policies, and other relevant details on their dashboard.
- **Insurance Policy Selection:** Users can choose from various car insurance policies, including comprehensive, personal, and accident coverage.
- **Payments:** Users can make payments for selected insurance policies securely through Square's payment API.
- **Loyalty Program:** Users can enroll in a loyalty program, accrue points, and redeem rewards.
- **Database Integration:** User and order information is stored in a database for persistence and retrieval.
- **Square API Integration:** The application integrates with Square's APIs for payment processing, loyalty program management, and order management.

## Project Structure

- `app.py`: Main Flask application file containing routes and logic.
- `templates/`: Directory containing HTML templates for rendering views.
- `static/`: Directory containing static files such as CSS and JavaScript.
- `models.py`: File containing database models for users and orders.
- `README.md`: Documentation file for the project.

## Installation and Setup

1. Clone the repository to your local machine:

```bash
git clone <repository_url>
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up a virtual environment (optional but recommended).

4. Configure your database connection in `app.py` and `models.py`.

5. Set up your Square developer account and obtain API credentials.

6. Update the configuration variables in `app.py` with your Square credentials.

7. Run the application:

```bash
python app.py
```

8. Access the application in your web browser at `http://localhost:5000`.

## Usage

- Register a new account or log in with existing credentials.
- View your dashboard to manage insurance policies, make payments, and track loyalty program points.
- Select insurance policies based on your preferences and make payments securely.
- Enroll in the loyalty program to earn points and redeem rewards.

## Technologies Used

- Flask: Python web framework for building the application.
- SQLAlchemy: Python SQL toolkit and Object-Relational Mapping (ORM) library for database integration.
- HTML/CSS/JavaScript: Frontend technologies for user interface and interactivity.
- Square API: Integration for payment processing, loyalty program management, and order management.

## License

This project is licensed under the [MIT License](LICENSE).
