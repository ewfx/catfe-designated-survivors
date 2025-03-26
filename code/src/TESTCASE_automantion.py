import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tqdm import tqdm  # Progress bar

# Define path to test case file
TEST_CASE_FILE = "C:\\Users\\91868\\Downloads\\generated_test_cases.xlsx"

# Selenium WebDriver setup (Ensure ChromeDriver is installed)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (remove if debugging)
driver = webdriver.Chrome(options=options)

# Function to load test cases
def load_test_cases():
    df = pd.read_excel(TEST_CASE_FILE)
    return df

# Function to perform login
def login(username, password):
    driver.get("http://localhost:5000/login")  # Update URL if needed

    try:
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.TAG_NAME, "button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        time.sleep(2)  # Allow time for login

        # Check if login was successful
        if "index" in driver.current_url:
            print("✅ Login Successful!")
            return True
        print("❌ Login Failed!")
        return False
    except Exception as e:
        print(f"❌ Login error: {str(e)}")
        return False

# Function to execute a single test case
def execute_test_case(test_case):
    print(f"\n📝 Executing: {test_case['Test Case']}")

    driver.get("http://localhost:5000")  # Ensure login before proceeding

    if "foreign exchange transaction with incorrect details" in test_case["Test Case"]:
        try:
            driver.get("http://localhost:5000/calculate_fee")

            # Simulating API call manually (for UI-based tests, implement actual form filling)
            data = {"amount": 100, "from_currency": "USD", "to_currency": "EUR"}
            driver.execute_script(f"fetch('/calculate_fee', {{method: 'POST', headers: {{'Content-Type': 'application/json'}}, body: JSON.stringify({data})}}).then(res => res.json()).then(console.log);")

            time.sleep(2)  # Wait for response

            # Validate system behavior
            if "error" in driver.page_source:
                print("✅ Test Passed!")
                return "Pass"
            else:
                print("❌ Test Failed!")
                return "Fail"
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return "Fail"

    elif "unauthorized access" in test_case["Test Case"]:
        try:
            driver.get("http://localhost:5000/calculate_fee")  # Try accessing without login

            if "Method Not Allowed" in driver.page_source:
                print("✅ Test Passed!")
                return "Pass"
            else:
                print("❌ Test Failed!")
                return "Fail"
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return "Fail"

    return "Not Implemented"

# Function to run all test cases and update the Excel file
def run_tests():
    df = load_test_cases()
    
    if not login("admin", "password123"):
        print("🚨 Login failed. Tests aborted.")
        return

    results = []
    
    print("\n🚀 Running Tests...\n")
    for index, test_case in tqdm(df.iterrows(), total=len(df), desc="Executing Test Cases", unit="test"):
        result = execute_test_case(test_case)
        df.at[index, "status"] = result  # Update test case with Pass/Fail

    # Save updated test case results
    df.to_excel(TEST_CASE_FILE, index=False)
    print("\n✅ Test execution complete. Results updated in test_cases.xlsx\n")

# Watchdog event handler
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(TEST_CASE_FILE):
            print("\n📄 Test case file updated. Running tests...")
            run_tests()

# Set up watchdog observer
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=False)
observer.start()

# Initial test execution
run_tests()

try:
    while True:
        time.sleep(10)  # Keep script running
except KeyboardInterrupt:
    observer.stop()

observer.join()
driver.quit()
