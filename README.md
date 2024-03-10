# SCHEMA
![STUDENT MANAGEMENT SYSTEM SCHEMA](db_schema.png)

## REASON FOR DESIGNIN THE SCHEMA THIS WAY
Data Organization: The schema is designed to effectively organize the data for a student management system. Each entity, such as users, programs, courses, grades, and students, is stored in its own table. This ensures that data is well-segmented and structured, facilitating efficient data management.

Data Integrity and Relationships: The schema maintains data integrity through the use of foreign keys to establish relationships between tables. For example, the user_id in the students table references the id in the users table, linking each student to a user account. This ensures consistency and accuracy in the data.

Auditing and Tracking: The schema includes timestamp fields such as created_at and updated_at, allowing for easy tracking of data modifications. This audit trail provides valuable insights into the history of data changes, aiding in accountability and debugging.

Ease of Querying: With a well-defined schema, querying and retrieving data becomes straightforward. Developers can easily write SQL queries to extract relevant information, such as retrieving all courses enrolled by a student or fetching grades for a specific course.

Scalability and Flexibility: The schema is designed with scalability in mind, allowing for future expansion and modifications. New features can be seamlessly integrated, and additional entities can be added without disrupting existing functionality. This flexibility ensures that the system can adapt to evolving requirements.

Data Retention and Security: The schema incorporates mechanisms for data retention and security. Instead of outright deletion, records are soft-deleted by marking them as deleted and preserving their history. This approach enhances data security and enables compliance with regulatory requirements.

By adopting this schema, the student management system benefits from structured data organization, integrity maintenance, auditability, query efficiency, scalability, and security, laying a solid foundation for effective data management and system operations.


## STUDENT MANAGEMENT SYSTEM API

---

### Software Requirements

1. Python 3.9.6
2. Postgres Server

---

### Instructions
1. Clone the repository
2. Make a copy of **.env.example** in the root directory and save it as **.env in the root directory**
3. Configure the database name and password in the **.env** file as below
```dotenv
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=
JWT_SECRET_KEY=any_random_str
SECRET_KEY=any_random_str
```
4. Open alembic/alembic.ini file and update necessary values in the line below
```ini
sqlalchemy.url = postgresql://your_db_username:your_db_password@your_db_host:your_db_port/your_db_name
```
---

### Commands
Open a terminal in the project's root directory and run the following commands 
1. Create a virtual environment
```shell
python -m venv path_to_virutal_env
```
2. Activate virtual environment
Unix
```shell
source path_to_virutal_env/bin/activate 
```
Windows (command prompt)
```shell
source path_to_virutal_env\bin\activate.bat
```
3. Install dependencies
```shell
pip install -r requirements.txt
```
4. Run migrations
```shell
alembic upgrade head
```
5. Seed data
```shell
flask seed db
```
6. Run application
```shell
flask run
```
---

### API Documentation
1. Click [here](https://documenter.getpostman.com/view/12044508/2sA2xh3tTt) to view the API documentation

---

### Sample Credentials
1. Email: ***super@admin.com***, Password: ***password***
