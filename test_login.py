from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time


class TestLogin:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # Hàm kiểm thử đăng nhập
    def test_login(self, accounts):
        test_case_result=[]

        for account in accounts:
            
            # Thực hiện login
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.CSS_SELECTOR, '*[data-test="username"]').send_keys(account["username"])
            self.driver.find_element(By.CSS_SELECTOR, '*[data-test="password"]').send_keys(account["password"])
            self.driver.find_element(By.CSS_SELECTOR, '*[data-test="login-button"]').click()
            
            result = ""
            
            # Kiểm tra kết quả kiểm thử
            try:
                error_message = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
                if error_message == "Epic sadface: Sorry, this user has been locked out.":
                    result = "locked"
                elif error_message == "Epic sadface: Username is required":
                    result = "username_empty"
                elif error_message == "Epic sadface: Password is required":
                    result = "password_empty"
                elif error_message == "Epic sadface: Username and password are required":
                    result = "username_password_empty"
                elif error_message == "Epic sadface: Username and password do not match any user in this service":
                    result = "not_match"
            except:
                result = "valid"

            # Lưu kết quả kiểm thử
            test_case_result.append(account["result"] == result)

        # Thống kê kết quả kiểm thử
        passed = test_case_result.count(True)
        expected = len(accounts)
        print(f"Passed: {passed}/{expected}")

        # Đưa ra danh sách các test case không pass
        if passed != expected:
            print("Failed test cases:")
            for i in range(len(test_case_result)):
                if not test_case_result[i]:
                    print(f"Test case {i + 1} failed")
    
    # Hàm đọc file csv và thống kê kết quả mong muốn
    def read_csv(self, file_path):
        accounts = []

        # Đọc file csv
        with open(file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                accounts.append(
                    {
                        "username": row["username"],
                        "password": row["password"],
                        "result": row["result"],
                    }
                )

        return accounts

if __name__ == "__main__":
    test = TestLogin()
    test.setup_method(None)
    test.test_login(test.read_csv("./Kiểm Thử Phần Mềm/accounts.csv"))
    test.teardown_method(None)
