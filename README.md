# Vehicle Rental System

A web-based application that allows users to create accounts, enter customer details, rent vehicles, and calculate rental charges based on hours and driver selection.

## Features

- User Account Creation and Sign In
- Customer Details Form
- Vehicle Rental Form
- Automatic Rental Cost Calculation
- Driver Option Handling
- Terms and Conditions Page
- Responsive and Clean UI

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Database**: MySQL

## Project Structure

vehicle_rental_system/
│
├── static/
│ └── styles.css
│
├── templates/
│ ├── index.html
│ ├── signin.html
│ ├── account_creation.html
│ ├── customer_details.html
│ ├── rental_form.html
│ ├── welcome.html
│ ├── terms-condition.html
│ └── main-page.html
│
├── app.py
└── requirements.txt

markdown
Copy
Edit

## Rental Cost Calculation

- Charges are calculated based on:
  - **Rental hours**
  - **Base hourly rate**
  - **Extra fee if driver is selected**

## Database Tables

- **account** – stores user login info
- **custom** – stores customer details
- **rents** – stores rental booking and cost

##  How to Run

1. **Clone the repo**  
2. **Install dependencies**  
   ```bash
  pip install -r requirements.txt
Set up MySQL database and tables

Run the Flask app

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser

## Screenshots



**Made By**
Ananya R
ananyark06@gmail.com
