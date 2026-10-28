# AWS Elastic Beanstalk Deployment

## Project Overview
This project demonstrates deploying a Python Flask web application on AWS Elastic Beanstalk. It includes application deployment, IAM role configuration, health checks, and environment monitoring.

## Technologies Used
- Python
- Flask
- AWS Elastic Beanstalk
- Amazon EC2
- AWS Identity and Access Management (IAM)
- Amazon CloudWatch / environment health monitoring, where configured

## Application Features
- Web page displaying application information
- Live UTC server timestamp
- Health-check endpoint at /health
- HTTP 200 response with JSON status for health checks

## Project Structure
- application.py — Flask application
- requirements.txt — Python dependencies
- screenshots — project and deployment evidence (screenshots currently stored in the repository root)

## Run Locally
1. Install Python 3.
2. Clone this repository:
   git clone https://github.com/yathish984/AWS-Elastic-Beanstalk-Deployment.git
3. Open the project directory:
   cd AWS-Elastic-Beanstalk-Deployment
4. Install dependencies:
   pip install -r requirements.txt
5. Start the application:
   python application.py
6. Open http://127.0.0.1:5000 in your browser.
7. Test the health endpoint at http://127.0.0.1:5000/health.

## AWS Deployment
1. Create an Elastic Beanstalk application and Python environment.
2. Configure the Elastic Beanstalk service role and EC2 instance profile as required.
3. Upload the application source bundle and deploy it.
4. Verify the application using the environment URL.
5. Check environment health and deployment events in the AWS console.

## Screenshots
The repository includes screenshots of the application, environment health, IAM roles, and AWS use case.

## Learning Outcomes
- Deploying a Python web application to AWS
- Understanding Elastic Beanstalk environments
- Configuring IAM roles and permissions
- Checking application health and deployment status

## Author
Yathish Gowda M.

## Repository
https://github.com/yathish984/AWS-Elastic-Beanstalk-Deployment
