from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement




class TableHandler:
    TABLE_LOCATOR = ("xpath", "//div[@class='table-mobile-wrapper']")
    ROWS_LOCATOR = ("xpath", ".//tbody/tr")
    CHECK_BOX_LOCATOR = ("xpath", "//input[@type='checkbox']")
    CELLS_LOCATOR = ("xpath", ".//td")
    EDIT_LOCATOR = ("xpath", ".//tbody//div[@class='tools'] //a[@data-original-title='редактировать']")
    DROPDOWN_MENU_LOCATOR = ("xpath", ".//tbody//a[@data-toggle='dropdown']")
    TOGGLE_LOCATOR = ("xpath", ".//td//div[contains(@class, 'toggle-switch')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self.TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self.ROWS_LOCATOR)

    @property
    def row_count(self) -> int:
        return len(self._rows)

    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]
        return row.text

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
        return cell.text



    def get_column_content(self, column_number):
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)
            column_content.append(cells[column_number - 1].text)
        return column_content


    def select_row(self, row_number):
        row = self._rows[row_number - 1]
        if "Test" in self.get_row_content(row_number)[2]:
            raise Exception("Don't for sell")
        else:
            cell = row.find_elements(*self.CELLS_LOCATOR)[0]
            cell.click()

    def status_check(self, row_number):
        row = self._rows[row_number - 1]
        cell = row.find_element(*self.TOGGLE_LOCATOR).get_attribute("class")
        if "on" in cell:
            return "switch ON"
        else:
            return "switch OFF"

