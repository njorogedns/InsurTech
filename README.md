# InsurTech Web Application

InsurTech is a simple web application built using Flask, a lightweight Python web framework, that allows users to select a car insurance policy and proceed to make payments. This README provides an overview of the project structure, functionality, and instructions for running the application.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
### User Authentication
- Users can register for an account by providing a username, password, email, given name, and family name.
- Registered users can log in securely using their credentials.
- User authentication is handled using industry-standard security practices.

### Policy Selection
- Users can choose from a variety of car insurance policies, including comprehensive, personal, and accident policies.
- Each policy offers different coverage options and pricing.

### Payments
- Users can securely make payments for their selected insurance policies using Square's Payment API.
- Payment processing is seamless and ensures the security of users' financial information.

### Dashboard
- Registered users have access to a personalized dashboard where they can view details of their insurance policies and payment history.
- The dashboard provides users with a convenient way to manage their insurance policies and track their payment activities.

### Loyalty Program Integration (New Feature)
- Implemented a loyalty program using Square's Loyalty API to reward customers for their loyalty.
- Users are automatically enrolled in the loyalty program upon registration.
- Users can earn points for purchasing insurance policies, which can be redeemed for rewards or benefits.

## Square API Integrations

### Square Payment API
- Integrated Square's Payment API to enable secure payment processing for insurance policy purchases.
- Users can make payments using various payment methods supported by Square, including credit/debit cards and digital wallets.

### Square Loyalty API
- Implemented Square's Loyalty API for managing a loyalty program within the application.
- Users earn loyalty points for purchasing insurance policies, and these points can be redeemed for rewards or benefits.
- The Loyalty API provides a seamless way to manage and track customer loyalty within the application.

## Project Structure

The project directory structure is as follows:

```
InsurTech/
│
├── app.py            # Flask application file containing routes and server configuration
├── templates/        # HTML templates for different pages
│ ├── dashboard.html # Dashboard template
│ ├── index.html # Homepage template
│ ├── login.html # Login page template
│ ├── register.html # Registration page template
│ └── select_policy.html # Policy selection page template
└── README.md         # Project documentation
```

## Installation

To run the InsurTech web application locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/njorogedns/InsurTech.git
```

2. Navigate to the project directory:

```bash
cd InsurTech
```

3. Install Flask (if not already installed):

```bash
pip install Flask
```

## Usage

To start the Flask development server and run the application, execute the following command:

```bash
python app.py
```

Once the server is running, you can access the InsurTech web application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
