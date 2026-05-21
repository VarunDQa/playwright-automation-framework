class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_title(self):
        return self.page.title()