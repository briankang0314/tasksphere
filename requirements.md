# Project Overview

The objective of this project is to develop a web-based task and scheduling application for Mr. K, a project coordinator at TechCo in South Korea. Mr. K manages 5-6 concurrent projects across multiple departments, coordinating tasks with development, design, and marketing teams. He currently handles 20-30 different tasks and 8-10 meetings per week using physical notebooks, post-it notes, and company emails. This fragmented system has led to missed deadlines, double-booked meetings, and significant time wasted searching for information.

By creating a centralized and secure platform accessible from both his Windows 11 office computer and company-issued iPhone, we aim to streamline Mr. K's workflow. The application will be developed as a Progressive Web Application (PWA) using Python with the Django framework for the backend. This choice addresses Mr. K's concerns about data security and provides robust authentication mechanisms to protect confidential project information.

The proposed solution will enhance efficiency by reducing administrative overhead, preventing scheduling conflicts, and providing quick access to critical project data. It will enable Mr. K to quickly add tasks during meetings, set reminders, and synchronize information across devices in real-time.

# Feature Requirements

## 1. Task Management and Organization

- **Concurrent Task Support**: Manage at least 30 concurrent tasks across 6 project departments.
- **Multi-Category Tagging**: Allow tasks to be tagged with multiple categories such as project, department, priority, and deadline.
- **Fast Task Entry**: Enable task entry within 30 seconds to facilitate quick additions during meetings.
- **Task Dashboard**: Provide a dashboard displaying current tasks sorted by priority and deadline for quick overview.

## 2. Meeting and Schedule Management

- **Conflict Detection**: Implement real-time detection to prevent double-booking of meetings and tasks.
- **Automated Reminders**: Send reminders 24 hours and 1 hour before meetings to ensure timely attendance.
- **Department Availability**: Show availability across departments in the scheduling interface for coordinated meeting planning.

## 3. Cross-Platform Accessibility

- **Quick Loading Time**: Ensure the web application loads within 3 seconds on both desktop and mobile devices.
- **Offline Mode**: Provide access to tasks and schedules from the previous 7 days when offline.
- **Responsive Design**: Adapt the interface seamlessly to both desktop and mobile screen sizes.
- **Real-Time Synchronization**: Synchronize data across devices within 30 seconds to maintain up-to-date information.

## 4. Security and Authentication

- **Session Timeout**: Automatically log out users after 15 minutes of inactivity to enhance security.
- **Data Encryption**: Encrypt all stored project-related data to protect sensitive information.

## 5. Search and Information Retrieval

- **Fast Search Results**: Deliver search results within 2 seconds to improve efficiency.
- **Advanced Filtering**: Offer filtering options by date range, project, department, and priority.
- **Recent Items Access**: Include a quick access list showing the last 10 accessed items for easy retrieval.
- **Data Export**: Provide functionality to export task lists and project reports for sharing and backup purposes.

## 6. Additional Features

- **Automated Priority Assignment**: Assign task priorities automatically based on deadline patterns.
- **Real-Time Notifications**: Notify users of task updates and schedule changes promptly.
- **User-Friendly Interface**: Design an intuitive interface to reduce the learning curve and improve user adoption.
- **Scalability**: Ensure the application can scale to accommodate more users and tasks as needed.

# Technical Requirements

- **Progressive Web Application**: Develop as a PWA to utilize offline capabilities and enhance mobile accessibility.
- **Performance Optimization**: Optimize code and database queries to meet performance criteria for loading times and responsiveness.

# Project Goals

- **Improve Efficiency**: Reduce the 45 minutes per day Mr. K spends searching for information by centralizing data.
- **Eliminate Errors**: Prevent missed deadlines and double-booked meetings through real-time conflict detection and reminders.
- **Enhance Workflow**: Allow quick task additions during meetings to streamline Mr. K's coordination efforts.
- **Ensure Security**: Protect confidential project data with robust encryption and secure authentication mechanisms.




# Tech Stack for High School Project

## 1. Frontend

### **HTML5 & CSS3**
- **Description**: The foundational technologies for creating web pages.
- **Advantages**:
  - **HTML5** structures the content of your web application.
  - **CSS3** styles your application, making it visually appealing.
  - Easy to learn with abundant resources and tutorials available.

### **JavaScript**
- **Description**: A scripting language that enables interactive features on your web pages.
- **Advantages**:
  - Allows you to add dynamic behavior to your application.
  - Widely supported and essential for frontend development.

### **Bootstrap**
- **Description**: A popular CSS framework for building responsive and mobile-first websites.
- **Advantages**:
  - Provides pre-designed components and utilities, speeding up the design process.
  - Ensures your application looks good on all devices without extensive custom CSS.

## 2. Backend

### **Flask (Python)**
- **Description**: A lightweight web framework for Python.
- **Advantages**:
  - Simpler and more flexible than larger frameworks like Django, making it ideal for smaller projects.
  - Easy to set up and get started with minimal configuration.
  - Extensive documentation and community support.

## 3. Database

### **SQLite**
- **Description**: A simple, file-based relational database.
- **Advantages**:
  - No need for a separate database server; the database is stored in a single file.
  - Easy to integrate with Flask.
  - Perfect for small to medium-sized applications.

## 4. Authentication

### **Flask-Login**
- **Description**: A user session management library for Flask.
- **Advantages**:
  - Simplifies the process of handling user authentication.
  - Integrates seamlessly with Flask applications.
  - Provides essential features like login, logout, and session management out of the box.

## 5. Deployment

### **Heroku (Free Tier)**
- **Description**: A cloud platform that allows you to deploy web applications easily.
- **Advantages**:
  - User-friendly interface suitable for beginners.
  - Supports Python and Flask applications.
  - Offers a free tier, which is sufficient for small projects.

## 6. Version Control

### **Git & GitHub**
- **Description**: Git is a version control system, and GitHub is a platform for hosting Git repositories.
- **Advantages**:
  - Keeps track of changes in your codebase.
  - Facilitates collaboration if you're working with others.
  - Provides a cloud backup of your project.