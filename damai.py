"""
基于python和selenium实现的大麦网自动刷新抢票脚本
用户要提前添加好个人信息和收货地址
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 设置抢票链接和开票时间

URL = "https://blpw.polyt.cn/show/18030000000004370"# PC页面

#URL = 'http://m.damai.cn/damai/perform/item.html?projectId=146290'#手机页面
# HOUR = 19
MIN  = 0
USERNAME = "15900933065"

driver = webdriver.Chrome()
# 设置等待时间
wait = WebDriverWait(driver, 5)
print('sleep 30 start')

driver.get(URL)
time.sleep(35)
print('sleep finish')
"""
PC端网页抢票操作
"""
def choose(seletor):
    print('get in choose', seletor)
    try:
        # 控件可点击时才选
        choice = wait.until(EC.element_to_be_clickable((By.XPATH, seletor)))
        print('choosing :', choice)
        return choice
    except TimeoutException as e:
        print("Time out!", seletor)
        return None
    except Exception:
        print("Not found!", seletor)
        return None

def login():
    # 点击登录
    print('login start')
    ##commonLoginUser login = choose('<a id="commonLoginUser" style="" href="javascript:void(0)" onclick="loginDivShow()">登录</a>')
    #login = driver.find_element_by_xpath('//*[@id="commonLoginUser"]').click()
    login = choose('//*[@id="commonLoginUser"]')
    time.sleep(5)
    print('logining: seccess', login)
    login.click()
    print('login clicked')
    username = choose('//*[@id="loginForm"]/div[2]/input')
    username.send_keys(USERNAME)
    """
    由于密码框控件被设置为不可见
    先自行输入密码并记住密码
    方便刷新
    （也可用cookie实现）
    """
    password = choose('//*[@id="pwd"]')
    try:
        password.click()
        password.send_keys("yifyang29bl")
    except Exception:
        print(password)
        print("Password Can't click")
    #user_rem = choose('//*[@id="loginForm"]/div[5]/div[1]/input')
    #user_rem.click()
    
    submit = choose('//*[@id="loginForm"]/div[4]/button')
    submit.click()

    print('login in func finish successfly')

def buy():
    # 点击价格
    print('start buying')
    try:
        price = None
        plus = None
        buybtn = None
        submit = None
        booker = None
        select = None
        confirm = None
        driver.get(URL)
        # 选择价格
        while None == price:
            # 这里选的是580票面的，如果选其他票面，修改最后的li[*]即可
            #price = choose('//*[@id="priceList"]/div/ul/li[3]')
            price = choose('/html/body/div[3]/div[2]/dl/dd[2]/div[3]/div[1]/dl/dd/div[2]')
            print('click time', price)
        price.click()
        # 数量加1
        while None == plus:
            plus = choose(r'//*[@id="itemValue1"]')
            print('click money', plus)
        plus.click()
        # 立即抢购
        while None == buybtn:
            buybtn = choose(r'//*[@id="submitTicket"]')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        print("buybtn finish", buybtn)
        buybtn.click()
        time.sleep(5)
        # 选择购票人
        while None == booker:
            booker = choose('//*[@id="35_42"]')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 选择、确定
        while None == select:
            select = choose('//*[@id="commitSeat"]')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        time.sleep(5)
        while None == confirm:
            confirm = choose('//*[@id="commitForm"]/div/div[1]/ul/li[2]')
        driver.execute_script("arguments[0].scrollIntoView();", confirm) 
        confirm.click()
        # 提交订单
        while None == submit:
            submit = choose('//*[@id="submit"]')
        driver.execute_script("arguments[0].scrollIntoView();", submit) 
        submit.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy()

def test():
    login()
    time.sleep(30)
    print("开始抢票")
    buy()
    print("抢票成功")


"""
移动端抢票操作
"""

def login_mobile():
    """
    点击购买进入登录界面
    自行输入帐号密码
    """
    # 立即购买
    buybtn = None
    while None == buybtn:
        buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
    buybtn.click()
    # 默认已经选好时间了，再点击立即购买
    buy = None
    while None == buy:
        buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buy) 
    buy.click()

def buy_mobile():
    try:
        # 立即购买
        buybtn = None
        while None == buybtn:
            buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 默认已经选好时间了，再点击立即购买
        buy = None
        while None == buy:
            buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buy) 
        buy.click()
        # 580票面
        price = None
        while None == price:
            price = choose('//*[@id="35_19"]')
        driver.execute_script("arguments[0].scrollIntoView();", price) 
        price.click()
        # 数量+1
        count = None
        while None == count:
            count = choose('/html/body/div[1]/div/div[3]/ul/li/div/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", count) 
        count.click()
        # 选好了
        select = None
        while None == select:
            select = choose('/html/body/div[1]/div/div[4]/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        # 购票人
        booker = None
        while None == booker:
            booker = choose('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/ul/li/div')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 去付款
        pay = None
        while None == pay:
            pay = choose('/html/body/div[1]/div[2]/div[2]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", pay) 
        pay.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy_mobile()

def test_mobile():
    login_mobile()
    time.sleep(30)
    print("开始抢票")
    buy_mobile()
    print("抢票成功")

def main():
    print('login begin')
    # 默认PC网页，手机网页对应修改即可
    login()
    print('login success')
    # 30秒等待用户输入密码后再开始刷
    time.sleep(10)
    while 1:
        if MIN == time.localtime().tm_min:
            print("开始抢票")
            buy()
            print("抢票成功")

if __name__ == '__main__':
    # test()
    #est_mobile()
    main()
