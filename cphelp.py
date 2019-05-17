from selenium import webdriver
from pynput import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
def func():
    f1=open("/home/aryan/Documents/input.txt","w")
    f2=open("/home/aryan/Documents/prog.txt","r")
    s=f2.read()
    options=webdriver.FirefoxOptions()
    options.add_argument('--headless')
    #s=input("Enter problem name")
    s1="https://www.codechef.com/problems/"
    s1=s1+s
    print("Visiting"+s1)
    driver = webdriver.Firefox(options=options)
    driver.get(s1)
    str=driver.find_element_by_xpath("//body//*[@id='problem-statement']").text;
    print(str[0:str.find('Author')]);
    print(str[str.find("Sample Input")+13:str.find("Sample Output")],file=f1)
    f1.close()
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if(key==keyboard.Key.f4):
            print("Work donebac")
            func()

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

