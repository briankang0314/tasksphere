Scenario
During our initial consultation on October 15, 2024, Mr. K, a project coordinator at TechCo in South Korea, described his challenge of managing 5-6 concurrent projects across multiple departments. "My biggest challenge," he stated, "is keeping track of about 20-30 different tasks and 8-10 meetings per week while coordinating with development, design, and marketing teams."

Mr. K demonstrated his current system, which relies on physical notebooks, post-it notes, and company emails. "Just last week," he shared, "I missed an important client meeting because the reminder was buried in my email, and last month, I had to work overtime twice due to overlooked project deadlines." Our examination of his workflow revealed significant issues:
- Three missed deadlines in the past month due to lost paper notes
- Double-booked meetings occurring 2-3 times weekly
- Approximately 45 minutes daily spent searching for information across platforms
- Frequent interruption of work to check various sources for upcoming deadlines

During our follow-up meeting on October 18, Mr. K emphasized his need for a centralized solution. "I need a system that can help me track everything in one place," he explained. He specified that the solution must be accessible from both his Windows 11 office computer and company-issued iPhone, as he frequently updates his schedule during client meetings. "The ability to quickly add tasks and set reminders during meetings would save me significant time," he noted. This scenario presents a clear opportunity for a structured digital solution that addresses Mr. K's organizational challenges while accommodating his technical requirements and workflow preferences.



Rationale For the Proposed Solution

Following extensive consultations with Mr. K, we determined that a web-based task and scheduling application would best address his organizational challenges. During our October 15 meeting, he emphasized, "I need something I can access anywhere, especially during client meetings." This requirement, combined with his need to use both Windows 11 at the office and an iPhone on the go, made a web-based solution the most practical choice.

The proposed technology stack has been carefully selected based on the client's specific needs. We will use Python with the Flask framework for the backend, as discussed with Mr. K on October 18. When presented with different options, he expressed concern about data security, noting, "I often deal with confidential project information." Python's robust security features and extensive library support make it ideal for handling sensitive project data securely. Additionally, Flask's built-in authentication system addresses his concern about unauthorized access to project information.
The solution will be developed as a Progressive Web Application (PWA), offering several advantages over commercial tools:
- Cross-platform compatibility for seamless desktop/mobile switching
- Custom task categorization aligned with his departmental structure
- Automated priority assignment based on deadline patterns
- Real-time synchronization to prevent double-booking
- Offline access for checking deadlines during offsite meetings

This tailored solution will eliminate the 45 minutes he currently spends searching for information by centralizing all task data in one secure, accessible platform. The technology choice ensures scalability while maintaining the quick task entry performance he requested during our discussions. As Mr. K noted in our follow-up meeting, "The ability to quickly add tasks during meetings would significantly improve my workflow."



Success Criteria

Task Management and Organization
- The system must support categorization of a minimum of 30 concurrent tasks across 6 project departments.
- Tasks must be tagged with multiple categories (project, department, priority, deadline).
- Task entry must take less than 30 seconds during meetings.
- The task dashboard must display current tasks sorted by priority and deadline.

Meeting and Schedule Management
- The system must prevent double-booking by showing real-time conflicts.
- Automated reminders must be sent 24 hours and 1 hour before meetings.
- The meeting scheduling interface must show availability across departments.

Cross-Platform Accessibility
- The web application must load within 3 seconds.
- Offline mode must provide access to tasks and schedules from the previous 7 days.
- The interface must adapt to both desktop and mobile screens.
- Real-time synchronization across devices within 30 seconds.

Security and Authentication
- Automatic session timeout after 15 minutes of inactivity.
- Encrypted storage for all project-related data.

Search and Information Retrieval
- Search results must appear within 2 seconds.
- Advanced filtering by date range, project, department, and priority.
- A recent items quick access list showing the last 10 accessed items.
- Export functionality for task lists and project reports.
