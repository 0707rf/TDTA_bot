from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import sys



Target_Time = ""  # 設定電腦啟動時間 格式00:00:00


url = "https://www.mvdis.gov.tw/m3-emv-trn/exm/locations#anchor&gsc.tab=0"



Date_of_Test = "1150204" #考試日期
my_id = "" #生份證號碼
Birthday = "" #生日
name = "" #名子
contactTel = "" #電話號碼
email="" #電子信箱



def clear_console(): #清除console函式
    os.system('cls' if os.name == 'nt' else 'clear')

stage = 0 #控制階段
local1on_str = ["臺北市區監理所（含金門馬祖）","臺北區監理所（北宜花）","新竹區監理所（桃竹苗）","臺中區監理所（中彰投）","嘉義區監理所（雲嘉南）","高雄市區監理所","高雄區監理所（高屏澎東）"]
local1on = [20,40,50,60,70,30,80]
local2on_str = [ 
    ["士林監理站(臺北市士林區承德路5段80號)","基隆監理站(基隆市七堵區實踐路296號)","金門監理站(金門縣金湖鎮黃海路六之一號)","連江監理站(連江縣南竿鄉津沙村155號)"],
    ["臺北區監理所(新北市樹林區中正路248巷7號)","板橋監理站(新北市中和區中山路三段116號)","宜蘭監理站(宜蘭縣五結鄉中正路二段9號)","花蓮監理站(花蓮縣吉安鄉中正路二段152號)","玉里監理分站(花蓮縣玉里鎮中華路427號)","蘆洲監理站(新北市蘆洲區中山二路163號)"],
    ["新竹區監理所(新竹縣新埔鎮文德路三段58號)","新竹市監理站(新竹市自由路10號)","桃園監理站(桃園市介壽路416號)","中壢監理站(桃園縣中壢市延平路394號)","苗栗監理站(苗栗市福麗里福麗98號)"],
    ["臺中區監理所(臺中市大肚區瑞井里遊園路一段2號)","臺中市監理站(臺中市北屯路77號)","埔里監理分站(南投縣埔里鎮水頭里水頭路68號)","豐原監理站(臺中市豐原區豐東路120號)","彰化監理站(彰化縣花壇鄉南口村中山路二段457號)","南投監理站(南投縣南投市光明一路301號)"],
    ["嘉義區監理所(嘉義縣朴子市朴子七路29號)","東勢監理分站(雲林縣東勢鄉新坤村新坤路333號)","雲林監理站(雲林縣斗六市雲林路二段411號)","新營監理站(臺南市新營區大同路55號)","臺南監理站(臺南市崇德路1號)","麻豆監理站(臺南市麻豆區北勢里新生北路551號)","嘉義市監理站(嘉義市東區保建街89號)"],
    ["高雄市區監理所(高雄市楠梓區德民路71號)","苓雅監理站(高雄市三民區建國一路454號)","旗山監理站(高雄市旗山區旗文路123-1號)"],
    ["高雄區監理所(高雄市鳳山區武營路361號)","臺東監理站(臺東市正氣北路441號)","屏東監理站(屏東市忠孝路222號)","恆春監理分站(屏東縣恒春鎮草埔路11號)","澎湖監理站(澎湖縣馬公市光華里121號)"]
]
local2on = [ #各個監理站的點擊數值
    [21,25,26,28],
    [40,41,43,44,45,46],
    [50,51,52,53,54],
    [60,61,62,63,64,65],
    [70,71,72,73,74,75,76],
    [30,31,33],
    [80,81,82,83,84]
]

while True:
    clear_console()

    print("      此軟體可能隨時會失效，請確保是最新版本。")
    print("可連結下載新版本:https://github.com/0707rf/TDTA_bot \nv0.8.0 - bata")
    print("目前選擇:普通重型機車")
    if stage>=2:
        print(r"如果下方地區錯誤請關閉程式重新選擇")
        print(f"------\n您顯擇的是 地區:{local1on_str[local1_in]}({local1on[local1_in]}) 監理站:{local2on_str[local1_in][local2_in]}({local2on[local1_in][local2_in]})")
        if stage>=3:
            print(f"考試日期:{Date_of_Test}")
        print("------")
    if stage == 0:
        print("請選擇地區:")
        print("1.臺北市區監理所（含金門馬祖）\n2.臺北區監理所（北宜花）\n3.新竹區監理所（桃竹苗）\n4.臺中區監理所（中彰投）\n5.嘉義區監理所（雲嘉南）\n6.高雄市區監理所\n7.高雄區監理所（高屏澎東）")
        try:
            local1_in = int(input("輸入編號:"))-1  #透過此數字查詢"local1on"陣列獲得數值
            if local1_in >=0 and local1_in<=7:
                stage+=1
        except:
            pass  

    elif stage == 1:
        print("請選擇地區:")
        for index,i in enumerate(local2on_str[local1_in]):
            print(f"{index+1}.{i}")
        print("重新選擇地區輸入0")
        try:
            local2_in = int(input("輸入編號:"))-1 #透過此數字跟"local1_in"查詢"local2on"陣列獲得數值
            if local2_in <= index and local2_in>=-1:
                if local2_in == -1:
                    stage = 0
                else:
                    stage+=1
        except:
            pass

    elif stage == 2:
        print("***資料請填寫正確否則會無效***")
        print("建議先去駕照網站上看時間再按照格式填入 例:1150204")

        Date_of_Test = str(input("設定考試日期(報名考試日期):"))

        my_id = str(input("生份證號(英文大寫):"))

        Birthday = str(input("生日(例如:0960530):"))

        name = str(input("名子:")) 

        contactTel = str(input("電話號碼:"))

        email = str(input("電子信箱:")) 
        stage+=1

    elif stage == 3:
        print("***請確認個人資料是否正確***")
        print(f"考試日期:{Date_of_Test}\n生份證號:{my_id}\n生日:{Birthday}\n名子:{name}\n電話:{contactTel}\n電子信箱:{email}\n********")
        print("確認正確輸入1")
        print("重新輸入個人資料請輸入0\n")
        
        try:
            user_in = int(input("輸入編號:"))
            if user_in ==1:
                stage +=1
            elif user_in ==0:
                stage -=1
        except:
            pass
    elif stage ==4:
        print("請照格式輸入 00:00:00 其中':'必須保留，建議先前往網頁  https://time.is/  \n查看左上角你的電腦時間是否快了還是慢了病自由的修正他 \n晚上12.網頁會刷新，啟動時間要填寫00:00:00 並且加入修正時間 如果塊5秒那就輸入23:59:55以此類推 建議延後個一秒\n")
        
        Target_Time = str(input("請輸入啟動時間:"))

        user_in = str(input("請再輸入一次:"))
        if Target_Time == user_in:
            stage+=1
        else:
            print("兩個時間不相同，請重新輸入!")
            time.sleep(1)
        
    elif stage == 5:
        print(f"時間已開始監控啟動時間{Target_Time}")
        break




key_word = [ 
    ["本場次為初考生","本場次為初考生","初考領者","場次"],
    ["初考機車者","本場次為初考生","初次報考機車駕照","初次報考機車","初次考領考生","本場次為初考"],
    ["僅提供初次報考","僅提供初次報考","僅供初次報考","本場次為初次報考","本場次僅供初次報考"],
    ["僅提供第一次報考","請先完成體檢","請做好體檢","僅供第一次報考","僅提供第一次報考","僅提供第一次報考"], #還沒完成
    ["機車報到完先講習後考試","初次考照請於考試日前完成體檢","先講習後考照","請於考照日前完成體檢","限筆試+路考者報名","僅供初考生預約","報名前，請先完成體檢表"],
    ["本場次供所有考生預約","本場次供所有考生預約","僅供初考者報名"],
    ["初考生","考試","初考領講習","機車初考生","完成報名"]
]




options = Options()
options.add_experimental_option("detach", True)
options.page_load_strategy = 'eager' 
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 啟動時設定 timeout，避免無限期等待
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(30) 


# 取得今日日期並結合目標時間字串
now = datetime.datetime.now()
target_dt_str = now.strftime("%Y-%m-%d") + " " + Target_Time
target = datetime.datetime.strptime(target_dt_str, "%Y-%m-%d %H:%M:%S")

# 如果設定的時間已經過了，則加一天
if now > target:
    target += datetime.timedelta(days=1)

# 靜默等待至目標時間
if Target_Time != 0:
    while datetime.datetime.now() < target:
        time.sleep(0.1)


try:
    driver.get(url)
except Exception as e:
    print("載入逾時，但可能已經可以操作了。")

wait = WebDriverWait(driver,10) 




main_forms = wait.until(EC.presence_of_element_located((By.ID,"form1"))) #等待表單出現

car = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'select[id="licenseTypeCode"]')))
opj_sel = Select(car)
opj_sel.select_by_value("3")  #選擇 普通重型機車

input_data = wait.until(EC.presence_of_element_located((By.ID,"expectExamDateStr")))
input_data.clear()
input_data.send_keys(Date_of_Test)  #輸入 考試日期

Place1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select[id="dmvNoLv1"]')))
opj_sel1 = Select(Place1)
opj_sel1.select_by_value(f"{local1on[local1_in]}")

wait.until(EC.presence_of_element_located((By.XPATH, f'//select[@id="dmvNo"]/option[@value="{local2on[local1_in][local2_in]}"]'))) #等 "臺南監理站(臺南市崇德路1號) #74 出現

Place2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select[id="dmvNo"]')))
opj_sel2 = Select(Place2)
opj_sel2.select_by_value(f"{local2on[local1_in][local2_in]}")

btn = driver.find_element(By.CSS_SELECTOR,'a[href="#anchor"].std_btn')
driver.execute_script("arguments[0].click();", btn)

btn1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[onclick="$.unblockUI();"]')))
driver.execute_script("arguments[0].click();", btn1)


try:
    
    target_xpath = f"//tbody/tr[contains(., '{key_word[local1_in][local2_in]}')]//a[contains(text(), '報名 SignUp')]"  #限筆試+路考者報名
    
    apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", apply_btn)
    driver.execute_script("arguments[0].click();", apply_btn)
    
    print("成功進入報名頁面！")

except Exception as e:
    print(f"目前無法報名：可能是名額已滿（顯示額滿）或尚未釋出。")
    driver.quit()
    sys.exit()


btn2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[onclick="$.unblockUI();	return false;"]')))
driver.execute_script("arguments[0].click();", btn2)

try:
    id_in = wait.until(EC.presence_of_element_located((By.ID,"idNo")))
    id_in.clear()
    id_in.send_keys(my_id)

    birthdayStr_in = wait.until(EC.presence_of_element_located((By.ID,"birthdayStr")))
    birthdayStr_in.clear()
    birthdayStr_in.send_keys(Birthday)
    birthdayStr_in.send_keys(Keys.TAB) 

    name_in = wait.until(EC.presence_of_element_located((By.ID,"name")))
    name_in.clear()
    name_in.send_keys(name)

    contactTel_in = wait.until(EC.presence_of_element_located((By.ID,"contactTel")))
    contactTel_in.clear()
    contactTel_in.send_keys(contactTel)

    email_in = wait.until(EC.presence_of_element_located((By.ID,"email")))
    email_in.clear()
    email_in.send_keys(email)
    email_in.send_keys(Keys.TAB)

except Exception as e:
    print(f"目前無法報名：可能是名額已滿（顯示額滿）或尚未釋出。")
    driver.quit()
    sys.exit()


target_xpath = "//a[contains(@onclick, 'add()')]"

apply_btn = wait.until(EC.presence_of_element_located((By.XPATH, target_xpath)))

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", apply_btn)
time.sleep(0.3)

driver.execute_script("arguments[0].click();", apply_btn)
print("成功報名")