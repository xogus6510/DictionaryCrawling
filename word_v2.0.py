from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import tkinter as tk
import json
#time.sleep(1) # 1초간 대

Englishaa = ""
Koreanaa = ""
Word = ""

def open_webpage(event=None):
    word = entry.get()
    driver = webdriver.Chrome()
    driver.get(
        f"https://dict.naver.com/search.dict?dicQuery={word}&query=&target=dic&ie=utf8&query_utf=&isOnlyViewEE=")
    
    print("██████████████████")
    단어 = driver.find_element(
        by=By.XPATH, value='//*[@id="content"]/div[1]/ul/li[1]/p[1]/a[1]/span/strong')
    print("입력한 단어 : " + 단어.text)
    print("██████████████████")
    print("네이버 국어사전 :")
    print("https://ko.dict.naver.com/#/search?range=word&query=" +
          word + "&autoConvert=&shouldSearchOpen=false")
    print("네이버 영어사전 :")
    print("https://en.dict.naver.com/#/search?range=meaning&query=" +
          word + "&autoConvert=")
    
    print("다음 국어사전 :")
    print("https://dic.daum.net/search.do?q=" +
          word + "&dic=kor")
    print("다음 영어사전 :")
    print("https://dic.daum.net/search.do?q=" +
          word + "&dic=eng")
    print("====================================================")

    for i in range(1, 11):
        try:
            xpath = f'//*[@id="content"]/div[1]/ul/li[{i}]/p[1]/span'
            element = driver.find_element(by=By.XPATH, value=xpath)
            text = element.text[1:-1] + "."
            xpath2 = f'//*[@id="content"]/div[1]/ul/li[{i}]/p[2]'
            element2 = driver.find_element(by=By.XPATH, value=xpath2)
            text2 = element2.text
            result = ""
            inside_bracket = False
            for char in text2:
                if char == '[':
                    inside_bracket = True
                elif char == ']':
                    inside_bracket = False
                elif not inside_bracket:
                    result += char   
            print(text + " " + result.strip())
            
            # Define the URL
            # url: str = "https://ko.dict.naver.com/#/search?range=word&query=" + word + "&autoConvert=&shouldSearchOpen=false"
            # urlTitle = word +"_국어사전.url"

            

            # # Create the .URL file
            # with open(urlTitle, "w") as file:
            #         file.write("[InternetShortcut]\n")
            #         file.write(f"URL={url}\n")

            # # Define the URL
            # url2: str = "https://en.dict.naver.com/#/search?range=meaning&query="+ word +"&autoConvert="
            # urlTitle = word + "_영어사전.url"

            # # Create the .URL file
            # with open(urlTitle, "w") as file:
            #     file.write("[InternetShortcut]\n")
            #     file.write(f"URL={url2}\n")

        except NoSuchElementException:
            # Element not found, move on to the next iteration
            continue

    driver.get(
        f"https://en.dict.naver.com/#/search?range=meaning&query={word}&autoConvert=")
    print("============영어단어=============")
    for j in range(1, 11):    
        xpath3 = f'//*[@id="searchPage_mean"]/div[1]/div[{j}]/div[1]'
        element3 = driver.find_element(by=By.XPATH, value=xpath3)
        text3 = element3.text

        xpath4 = f'//*[@id = "searchPage_mean"]/div[1]/div[{j}]/ul'
        element4 = driver.find_element(by=By.XPATH, value=xpath4)
        text4 = element4.text
        
        print(text3 + " " + text4)
        print("---------------------------------")
    
    # with open(f"{word}.txt", "w", encoding="utf-8") as file:
    #     file.write(
    #         f"https://dict.naver.com/search.dict?dicQuery={word}&query=&target=dic&ie=utf8&query_utf=&isOnlyViewEE=")
    #     file.write(f"\n\n")
    #     file.write(
    #         f"https://en.dict.naver.com/#/search?query={word}&range=all")
    #     file.write(f"\n\n")
    #     file.write(f"{Korean}\n\n\n\n")
    #     file.write(f"{EnglishWord.text}\n\n\n\n")
    #     file.write(f"{English}\n")
        

    # print("============== 단어사전 ================")
    # print(
    #     f"https://dict.naver.com/search.dict?dicQuery={word}&query=&target=dic&ie=utf8&query_utf=&isOnlyViewEE=")
    # print(f"https://en.dict.naver.com/#/search?query={Word}&range=all")
    # print(Korean)
    # print("=====================================")
    # print(EnglishWord.text)
    # print("=====================================")
    # print(English)
    # print("============== 마지막 ================")
    #
    driver.quit()
    #root.destroy()

root = tk.Tk()
root.title("Word Lookup")
root.geometry("500x300")
root.config(bg="lightgray")

entry_label = tk.Label(root, text="네이버 사전단어 검색",
                       bg="lightgray", font=("맑은고딕", 30))
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)
entry.bind("<Return>", open_webpage)

lookup_button = tk.Button(root, text="단어 찾기", font=(
    "Helvetica", 16), command=open_webpage)
lookup_button.pack(pady=10)

result_label = tk.Label(root, text="제작 : WILLIE / 유지보수 : ILA, SEAN",
                        bg="lightgray", font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()





#pip install selenium
#https://chromedriver.chromium.org/downloads
#pip install pyinstaller
#pyinstaller --onefile word.py
