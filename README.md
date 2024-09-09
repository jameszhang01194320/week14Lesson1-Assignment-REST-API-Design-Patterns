<<<<<<< HEAD
Lesson 2: Assignment
________________________________________

Task 1: Implement Pagination for Orders
•	Modify the existing endpoint /orders find_all to support pagination by adding query parameters for page and per_page.
•	Implement pagination logic in the backend to retrieve orders in batches based on the provided parameters.

Task 2: Implement Pagination for Products
•	Update the /products find_all endpoint to incorporate pagination functionality similar to the orders endpoint.
•	Adjust the backend logic to fetch products in paginated form based on the specified parameters.

Task 3: Test Pagination Endpoints
•	Test the pagination endpoints /orders and /products using various combinations of page and per_page parameters.
•	Verify that the endpoints return the expected results and handle edge cases such as out-of-range page numbers gracefully.
For added challenge incorporate a search_term route that is also paginated (BONUS)
________________________________________
Expected Outcomes:
Upon completing this assignment, students should achieve the following outcomes:
•	Implementation of pagination functionality for retrieving orders and products, improving system performance and user experience.
•	Integration of pagination logic into the existing factory management system, ensuring seamless interaction with large datasets.
•	Successful testing of pagination endpoints to validate correct functionality and handle edge cases effectively.

=======
Assignment | REST API Design Patterns

Task 1: Implement Factory Application Pattern
•	Configure the Flask application using the Factory Application Pattern to enable easy configuration and instantiation of the application.
•	Organize the application structure into modules for better code organization and maintainability.

Task 2: Utilize Flask Blueprints for Modular Design
•	Create Flask Blueprints to modularize different aspects of the factory management system, such as customer management,  product additions and removal, and the creation of orders.
•	Register these Blueprints with the Flask application to enable modularity and separation of concerns.

ask 3: Implement API Throttling and Rate Limiting
•	Integrate Flask-Limiter into the application to implement API throttling and rate limiting functionality.
•	Configure rate limits for different API endpoints to prevent abuse and ensure fair usage of resources.

Task 4: Create Endpoints for CRUD Operations
•	For the models (Product, Order, Customer), create CRUD Operations.
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
