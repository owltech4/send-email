import datetime
from emailer import send_email

# Main function 
def main():
    start_time = datetime.datetime.now()
    print(f"Program started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Insert the main logic of your program here
    receiver_email = "input.email@here.com"
    subject = "Test email"
    body = "Hi! :)"
    send_email(receiver_email, subject, body)

    end_time = datetime.datetime.now()
    print(f"Program finished in: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Calculates and prints the duration of the program
    duration = end_time - start_time
    print(f"Execution duration: {duration}")

if __name__ == "__main__":
    main()
