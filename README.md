IIT Dining Bot
Overview

IIT Dining Bot is an AI-powered dining assistant built as a course project at Illinois Institute of Technology. The application helps students quickly find dining information by answering questions about available meals, nutrition information, dietary preferences, and dining schedules.

Instead of manually searching through dining menus, students can interact with the bot and receive instant answers about:

Available meals and menu items
Dining hall schedules
Calories and nutritional information
High-protein meal options
Vegetarian meals
Vegan meals
Halal food options

The system integrates directly with the university's official dining services API to ensure menu information remains current and accurate.
Features
Natural Language Question Answering

Students can ask questions such as:

What is available for lunch today?
What are the highest protein options?
What vegan meals are available tonight?
Is there any halal food available today?
How many calories are in a specific meal?
Real-Time Menu Data

The bot retrieves menu information from the official IIT Dining API and presents it in an easy-to-understand format.

Nutrition-Aware Recommendations

The system can filter and recommend meals based on:

Protein content
Calories
Vegetarian preferences
Vegan preferences
Halal dietary requirements
Automated Daily Updates

A scheduled background process automatically refreshes menu information each day by fetching the latest data from the dining API.

Architecture

Official IIT Dining API
            |
            v
    Data Ingestion Layer
            |
            v
      Menu Processing
            |
            v
      Scheduler Service
            |
            v
      Dining Bot API
            |
            v
         End Users

Technologies Used
Python
REST APIs
Scheduling/Automation Services
JSON Data Processing
Official IIT Dining API
How It Works
The application connects to the official IIT Dining API.
Menu and nutrition data are retrieved and processed.
A scheduled job refreshes menu information daily.
Users submit questions through the chatbot interface.
The system analyzes the query and returns relevant menu, nutrition, and dietary information.


Learning Outcomes

This project provided hands-on experience with:

API integration and data ingestion
Automated scheduling and background jobs
Building conversational interfaces
Nutrition and menu data processing
Backend application development
Working with real-world university data sources
Future Improvements
Personalized meal recommendations
User dietary profiles
Mobile-friendly interface
Historical nutrition tracking
Meal comparison and ranking
Multi-dining hall support


Academic Project

Developed as a course project at Illinois Institute of Technology to explore API-driven applications, automation workflows, and conversational interfaces for improving student access to dining information.
