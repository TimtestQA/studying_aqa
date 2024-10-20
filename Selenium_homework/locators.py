
# Head

SEO_DESCRIPTION = ("xpath", "//head/meta[@name='description']")



# Header

LOGO_IN_HEADER = ("xpath", "//header//ul[@class='navbar-nav']")

EXPLORE_BUTTON = ("xpath", "//header//li/a[contains(text(),  'Explore')]")

PRISING_BUTTON = ("xpath", "//header//div//li[a[contains(text(), 'Pricing')] and @click-event-part='head']")

FOR_BUSINESS_BUTTON = ("xpath", "//header//div//li/a[@class='nav-link' and contains(text(), 'For B')]")

SIGHN_IN_BUTTON = ("xpath", "//header//button[span[text()=' Sign in ']]")

START_FOR_FREE_BUTTON = ("xpath", "//header//button/span[text()=' Start for free ']")



#Dropdown Explpre buttons

PYTHON_IN_EXPLORE = ("xpath", "//header//div//a[@click-event-target='Python']")

ALL_COURSES_IN_EXPLORE = ("xpath", "//header//div/a[@click-event-target='All courses' and text()='All courses']")



# Main
H1_IN_MAIN = ("xpath", "//main//h1[contains(text(), 'What do you want to do?')]")

START_BLOCK = ("xpath", "//main//div/a[@click-event-part= 'hero_section' and @click-event-target ='projects']")

SELECT_BLOCK = ("xpath", "//main//a[@click-event-part= 'hero_section' and @click-event-target='tracks']")

H2_PROJECT = ("xpath", "//main//h2[@id='projects']")

MOUSEWHELL_ANIMATION = ("xpath", "//main//span[contains(@class, 'mousewheel')]")

# Project_Selection

PYTHON_SELECT_BUTTON = ("xpath", "//main//div//a[text()= 'Python']")

JAVA_SELECT_BUTTON = ("xpath", "//main//div/a[@data-component-name='RouterLink' and text()='Java']")

KOTLIN_SELEC_BUTTON = ("xpath", "//main//div/a[@click-event-target='kotlin']")

JS_SELECT_BUTTON = ("xpath", "//main//div/a[@click-event-part='project_languages' and text()='JavaScript']")

# JS_projects

JS_MY_FIRST_PROJECT = ("xpath", "//main//div//a[@click-event-part='project_card' and @aria-label='My First Project (JavaScript)']")

CHALKBORAD_PRINTER_PROJECT = ("xpath", "//main//div/a[@aria-label='Chalkboard Printer']")


# COUSRE_SELECTION

ALL_COURSES_SELECT = ("xpath", "//main//div/a[normalize-space()='All courses']")

TOP_COURSES_SELECT = ("xpath", "//main//div/a[normalize-space()='Top courses' and @click-event-part='main']")


# COURSE
PYTHON_DEVELOPER_COURSE = ("xpath", "//main//div[h5[contains(text(), 'Python Developer')]]")

# FOOTER

FOOTER_BLOG_BUTTON = ("xpat", "//footer//div//a[@class='link !mt-1 !block' and contains(text(), 'Blog')]")

YOUTUBE_BUTTON = ("xpath", "//footer//div//a[@aria-label='Hyperskill on YouTube']")

BLOG_BUTTON_IN_RESOURCES = ("xpath", "//footer//div[a[@class='link !mt-1 !block' and contains(text(), 'Blog')]]")

#Support

HELP_CENTER = ("xpath", "//footer//div[a[@click-event-part='footer' and @click-event-target='help-center']]")

TERMS = ("xpath", "//footer//div/a[@class='link !mt-1 !block' and @click-event-target='terms']")

#STORES_BUTTONS
GOOGLE_PLAY_BUTTON = ("xpath", "//footer//div//a[@click-event-part='footer' and @click-event-target='google-play']")

APPSTORE_BUTTON = ("xpath", "//footer//div//a[@class='!ml-4 !mt-0 !block md:!ml-0 md:!mt-4']")





