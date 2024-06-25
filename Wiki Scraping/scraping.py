from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pandas as pd

def get_data(url) -> list: 
    browser_options = ChromeOptions()
    browser_options.headless = True

    driver = Chrome(options=browser_options)
    driver.get(url)
    
    data = []
    # Locate the table rows
    rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'wikitable')]/tbody/tr")
    for row in rows[1:]: 
        try:
            name = row.find_element(By.XPATH, "td[2]/b/a").text
            start_date = row.find_element(By.XPATH, "td[3]/span[1]").text
            end_date = row.find_element(By.XPATH, "td[3]/span[2]").text
            political_inclination = row.find_element(By.XPATH, "td[5]/a").text
            
            presidential_credentials = {
                'title': name,
                'start-date': start_date, 
                'end-date': end_date, 
                'Party': political_inclination
            }
            data.append(presidential_credentials)
        except Exception as e:
            continue
    
    driver.quit()
    return data

def save_to_excel(data, filename):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    # Save the DataFrame to an Excel file
    df.to_excel(filename, index=False)

def main():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    data = get_data(url)
    print(data)  # Print data to verify it's correct
    
    # Save the data to an Excel file
    save_to_excel(data, "presidents_of_usa.xlsx")

if __name__ == "__main__":
    main()
