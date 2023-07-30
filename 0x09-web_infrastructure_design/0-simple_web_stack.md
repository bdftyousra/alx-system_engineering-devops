# Simple Web Stack


![Alt Text](https://github.com/bdftyousra/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png?raw=true)

[Visit Board](https://miro.com/app/board/uXjVOfJwct0=/)


## Description

This is a simple web infrastructure that hosts a website that is reachable via `www.foobar.com`. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.

## Specifics About This Infrastructure

+ What a server is.<br/>A server is a computer hardware or software that provides services to other computers, which are usually referred to as *clients*.

+ The role of the domain name.<br/>To provide a human-friendly alias for an IP Address. For example, the domain name `www.wikipedia.org` is easier to recognize and remember than `91.198.174.192`. The IP address and domain name alias is mapped in the Domain Name System (DNS)

+ The type of DNS record `www` is in `www.foobar.com`.<br/>`www.foobar.com` uses an **A record**. This can be checked by running `dig www.foobar.com`.<br/>**Note:** the results might be different but for the infrastructure in this design, an **A** record is used.<br/>
<i>Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.</i>

+ The role of the web server.<br/>The web server is a software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

+ The role of the application server.<br/>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

+ The role of the database.<br/>To maintain a collection of organized information that can easily be accessed, managed and updated

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## User Request:
A user wants to access the website, so they type www.foobar.com into their web browser.

## Domain Registration and DNS:
First, you need to register the domain name "foobar.com" through a domain registrar (e.g., GoDaddy, Namecheap). Once registered, you will configure the domain's DNS settings to point to your server's IP address. This DNS configuration tells the internet where to find your website when someone types in www.foobar.com.

## Web Server:
You'll need a server to host the website. For this one-server infrastructure, we'll use a single physical or virtual server to handle all the requests. This server will contain the necessary software to serve web pages, commonly achieved using a web server software like Apache, Nginx, or Microsoft IIS.

## HTTP Requests and Responses:
When a user types www.foobar.com into their browser and hits Enter, their web browser sends an HTTP request to your server.

## Load Balancer (Optional - for Scalability):
In a one-server setup, we don't have multiple servers to distribute the load, but if you expect significant traffic growth in the future, it's a good idea to include a load balancer. A load balancer can be a hardware device or software-based and helps distribute incoming traffic across multiple servers, ensuring better performance and high availability.

## Web Server Processing:
The web server (e.g., Apache, Nginx) receives the HTTP request from the user's browser and processes it. It then fetches the requested web page, processes any dynamic content, and generates an HTTP response.

## Application Code and Content:
If your website is dynamic and requires data processing or access to a database, the web server will pass the request to the relevant application code running on the server. This code can be written in programming languages like PHP, Python, Node.js, etc. The application code interacts with databases or other services to gather the necessary data and generate a dynamic response.

## Static Content (Optional - for Efficiency):
Static content like images, CSS, JavaScript, and other media files can be served directly by the web server, without going through the application code. This improves efficiency and reduces the load on the server.

## Database (Optional - for Dynamic Websites):
If your website requires a database to store and retrieve data (e.g., user accounts, blog posts), you'll need to set up a database server. Popular choices include MySQL, PostgreSQL, MongoDB, etc.

## HTTP Response:
Once the web server has processed the request and gathered all the necessary data, it generates an HTTP response and sends it back to the user's browser.

## User Receives Website:
The user's browser receives the HTTP response, which contains the website's HTML, CSS, and other assets. The browser then renders the web page and displays it to the user.

## Security Measures (Important):
In a real-world scenario, security is crucial. You should implement SSL/TLS certificates to enable HTTPS, ensuring secure communication between the server and the user's browser. Additionally, consider implementing firewalls, intrusion detection systems, and regular security updates to protect your server from potential threats.

## This basic one-server web infrastructure will handle user requests and serve your website accessible via www.foobar.com. As your website grows and traffic increases, you may need to consider scaling your infrastructure by adding more servers, employing content delivery networks (CDNs), or using cloud services for improved performance and reliability.
