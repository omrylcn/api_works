# Mini Notes

## API

- API stands for application programming interface; it is an interface for the website (or mobile application) to communicate with the backend logic.

- A metaphor for this is a waiter/waitress, who can understand different customers' orders. They will then act as a middleman between the customers and the chefs in the kitchen.
  
- In computer science, one of the key benefits of having API is encapsulation.We encapsulate the logic so that people outside won't be able to see it.

## RESTful API

- REST stands for Representational State Transfer. It was first defined in Dr. Roy Fielding's dissertation (Architectural Styles and the Design of Network-Based Software Architectures) back in 2000.

- REST is not a standard or protocol; it is more like a software architectural style. Many engineers follow this architectural style to build their applications, such as eBay, Facebook, and Google Maps. 

- There are five important constraints/principles for the REST architecture style:

  - ``Client-server``: There is an interface between the client and the server. The client and server communicate through this interface and are independent of each other. Either side can be replaced as long as the interface stays the same. Requests always come from the client-side.
  - ``Stateless``: There is no concept of state for a request. Every request is considered to be independent and complete. There is no dependence on the previous request nor dependence on a session to maintain the connection status.
  - ``Cacheable``: Things are cacheable on the server or client-side to improve performance.
  - ``Layered system``: There can be multiple layers in the system, and the goal here is to hide the actual logic/resources. These layers can perform different functions, such as caching and encryption.
  - ``Uniform interface``: The interface stays the same. This helps to decouple the client and server logic.

## HTTP Protocol

- HyperText Transfer Protocol and is the standard protocol used on the worldwide web. 
- HTTP is an implementation of the REST architecture style. I
- When the frontend interface interacts with the backend API through a URL, they need to, at the same time, define the HTTP method for this request. 

- HTTP methods.
  - ``GET``: For reading data
  - ``POST``: For creating data
  - ``PUT``: For updating data by completely replacing data with new content
  - ``PATCH``: For updating data, but by partially modifying a few attributes
  - ``DELETE``: For deleting data

## JSON Format

- JavaScript Object Notation (JSON) is a simple plaintext format that is capable of representing complex data structures. 
- Few notes on JSON syntax:
  - Arrays are enclosed by []
  - Objects can be represented by {}
  - Names/values always exist in pairs, and are delimited by ":"
  - Strings are enclosed by ""

## HTTP Status Codes

- A status code is a code that is returned in the HTTP protocol. 
- Construct our RESTful API, we need to comply with the HTTP protocol. The status code helps the frontend client understand the status of their request, that is, whether it is a success or failure.

![alt text](https://miro.medium.com/max/2400/1*MmsyWBBpUZ7QBHF7bn3tPA.png)

