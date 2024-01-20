### smtpAPI Python Example
The provided code is an example of how to use the SMTP API in Python to send emails.

#### smtpOperation.py:
The `smtpOperation.py` contains the code related to sending emails:

1. **Importing Libraries:**
   - The required libraries are imported:
     - `dotenv`: For loading environment variables.
     - `os`: For accessing environment variables.
     - `smtplib`: For sending emails.
     - `email.mime.text`: For creating plain text email messages.
     - `email.mime.multipart`: For creating multipart email messages.

2. **Loading Environment Variables:**
   - The `load_dotenv()` function is used to load environment variables from a `.env` file.
   - This file should contain the following variables:
     - `EMAIL_ID`: Your SMTP username (email address).
     - `PASSWORD`: Your SMTP password.
     - `DEFAULT_USER`: The default recipient email address.

3. **`send_mail()` Function:**
   - This function takes one optional argument, `text`, which defaults to "choco".
   - It builds a multipart email message with the following components:
     - `From`: The sender's email address (specified by `smtp_username`).
     - `To`: The recipient's email address (specified by `receiver_email`).
     - `Subject`: The subject of the email ("Gift Choose").
     - `text`: The body of the email, which is a plain text message containing the value of the `text` argument.

4. **Sending the Email:**
   - The email is sent using the SMTP protocol.
   - It connects to the SMTP server (`smtp.gmail.com`) on port 587.
   - It logs in using the credentials specified in the environment variables.
   - It sends the email using the `sendmail()` method.
   - If the email is sent successfully, a confirmation message is printed.
   - If there is an error while sending the email, an error message is printed.

#### main.py:
The `main.py` contains the FastAPI application:

1. **Importing Libraries:**
   - `FastAPI`: For creating the FastAPI application.
   - `CORSMiddleware`: For enabling CORS (Cross-Origin Resource Sharing) in the application.
   - `smtpOperation`: The module containing the `send_mail()` function.

2. **FastAPI Application:**
   - An instance of the FastAPI application is created.
   - The `add_middleware()` method is used to add the `CORSMiddleware` middleware to the application. This allows the API to accept requests from any origin.

3. **Root Page:**
   - The root page (`/`) is defined. When a GET request is made to this endpoint, it returns a simple message indicating that the project is for checking TensorFlow operations.

4. **`predict()` Function:**
   - The `/gift/` endpoint is defined to accept a GET request with a `gift` query parameter.
   - The `gift` query parameter is required and represents the gift chosen by a person.
   - The function tries to send an email using the `send_mail()` function, passing the value of the `gift` parameter as the email body.
   - If the email is sent successfully, it returns "successful"; otherwise, it returns "unsuccessful."


To use this code, you need to follow these steps:

1. Create a `.env` file and populate it with the necessary environment variables:
   ```
   EMAIL_ID=your_smtp_username
   PASSWORD=your_smtp_password
   DEFAULT_USER=default_recipient_email
   ```

2. Run the `smtpOperation.py` script to ensure that the email sending functionality is working properly.

3. Run the `main.py` script to start the FastAPI application.

4. You can now visit the root page at `http://localhost:8000/` to see the project description.

5. To test the email sending functionality, visit `http://localhost:8000/gift/?gift=YOUR_GIFT_CHOICE`. Replace `YOUR_GIFT_CHOICE` with the gift you want to send in the email.

6. If the email is sent successfully, you should see a "successful" response. Otherwise, you will see an "unsuccessful" response.

7. Check your email inbox to verify that you have received the email with the gift choice