# flask
Empezando... y más,  con flask


Al hacer POST con Postman y pulsar SEND:
========================================

WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
[2019-11-19 11:23:18,722] ERROR in app: Exception on /users [POST]

Traceback (most recent call last):
  File "C:\Users\Gonzalo\AppData\Local\Programs\Python\Python36\lib\site-packages\flask\app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
    
  File "C:\Users\Gonzalo\AppData\Local\Programs\Python\Python36\lib\site-packages\flask\app.py", line 1952, in full_dispatch_request
    return self.finalize_request(rv)
    
  File "C:\Users\Gonzalo\AppData\Local\Programs\Python\Python36\lib\site-packages\flask\app.py", line 1967, in finalize_request
    response = self.make_response(rv)
    
  File "C:\Users\Gonzalo\AppData\Local\Programs\Python\Python36\lib\site-packages\flask\app.py", line 2097, in make_response
    "The view function did not return a valid response. The"
    
TypeError: The view function did not return a valid response. The function either returned None or ended without a return statement.
127.0.0.1 - - [19/Nov/2019 11:23:18] "POST /users HTTP/1.1" 500 -
