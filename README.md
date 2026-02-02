Student Management System
A simple, web-based Student Management System built using the Flask web framework. This application allows users to log in, view a dashboard of students, and add new student records including their roll numbers, marks, and subjects.

->Features-
Secure Login: Restricted access via a login system (Default: username: anshul, password: pass).

Student Dashboard: View a complete list of all registered students in a tabular format.

Add Student Records: Easily add new student details such as Name, Roll Number, Marks, and Subject.

Session Management: Uses Flask sessions to maintain user login states and provides a logout functionality.

Responsive Styling: Styled with a custom CSS theme and a consistent base layout using Jinja2 templates.

->File Structure
app.py: The main Flask application file containing routes and logic.

templates/: Directory containing HTML templates.

base.html: The base layout used by all other pages.

login.html: The user login page.

dashboard.html: Displays the list of students.

add_students.html: Form for adding new student data.

static/: Directory for static assets.

style.css: Custom CSS for application styling.

->Prerequisites
To run this project, you need to have Python and Flask installed:

->Bash
pip install flask
How to Run
Clone the repository:

Bash
git clone <your-repository-url>
cd <repository-folder>
Organize files: Ensure your directory structure looks like this:

Plaintext
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── login.html
    ├── dashboard.html
    └── add_students.html
Run the application:

Bash
python app.py
Access the app: Open your browser and navigate to http://127.0.0.1:5000/.

Usage
Login: Use the default credentials mentioned above to access the system.

Dashboard: Once logged in, you will be directed to the dashboard where the student list is displayed.

Add Student: Click on the "add student" link in the navbar to enter new student details.
