import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class OrangeHRM {
    public static void main(String[] args) {
        // Create a new instance of the ChromeDriver
        WebDriver driver = new ChromeDriver();

        try {
            // Maximize the browser window
            driver.manage().window().maximize();

            // Navigate to the login page
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
            
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(40));

            // Log in
            WebElement username = driver.findElement(By.name("username"));
            WebElement password = driver.findElement(By.name("password"));
            WebElement loginButton = driver.findElement(By.cssSelector("button[type='submit']"));

            username.sendKeys("Admin");
            password.sendKeys("admin123");
            loginButton.click();

            // Navigate to the Leave section
            WebElement leaveMenu = driver.findElement(By.xpath("//span[text()='Leave']"));
            leaveMenu.click();

            // Click on 'Apply'
            WebElement applyLeave = driver.findElement(By.xpath("//a[text()='Apply']"));
            applyLeave.click();

            // Click on 'LeaveType'
            WebElement leaveType = driver.findElement(By.xpath("//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"));
            leaveType.click();

            WebElement optionCAN = driver.findElement(By.xpath("//*[contains(text(),'CAN')]"));
            optionCAN.click();

            // Enter Dates
            WebElement fromDate = driver.findElement(By.xpath("//input[@class='oxd-input oxd-input--focus']"));
            WebElement toDate = driver.findElement(By.xpath("//input[@class='oxd-input oxd-input--focus']"));
            WebElement applyButton = driver.findElement(By.xpath("//button[@type='submit']"));

            fromDate.sendKeys("2024-09-16"); // Enter from date
            toDate.sendKeys("2024-09-20");   // Enter to date
            applyButton.click();             // Click on the apply button

            // Wait for a few seconds to observe the result
            Thread.sleep(3000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Close the browser
            driver.close();
        }
    }
}
