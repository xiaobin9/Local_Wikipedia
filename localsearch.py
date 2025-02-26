# from baidusearch.baidusearch import search
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
class SearchWrapper:
    def __init__(self):
       
        pass

    # def perform_search(self, query: str):
    #     """
    #     执行百度搜索的方法

    #     :param query: 搜索的关键词
    #     :return: 搜索结果
    #     """
    #     try:
    #         # 调用 baidusearch 库的 search 函数进行搜索
    #         results = search(query)
    #         abstract_string = '\n'.join([item['abstract'] for item in results])
    #         return abstract_string
    #     except Exception as e:
    #         # 若搜索过程中出现异常，打印错误信息并返回 None
    #         print(f"搜索过程中出现错误: {e}")
    #         return None
        
    def shoudon(self, query: str):
        user_input = input("请输入查询结果: ")
        return user_input
    
    def clean_query(self,query: str):
        str=query.replace(" ", "_")
        return str
    
    def kiwix_wikipedia(self, query: str):
        query=self.clean_query(query)
        url = "http://your_url/viewer#wikipedia_en_all_nopic_2024-06/A/"+query

        # 设置 Chrome 选项
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument('--no-sandbox')  # 必需的参数，避免沙箱错误
        chrome_options.add_argument('--disable-dev-shm-usage')  # 共享内存不足问题

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        iframe = driver.find_element(By.ID, 'content_iframe')
        driver.switch_to.frame(iframe)

        try:
            # 查找类名为 mf_section0 的 div 元素
            target_div = driver.find_element(By.CSS_SELECTOR, 'div.mf-section-0')
            # 查找该 div 下的第一个 p 元素
            first_p = target_div.find_element(By.TAG_NAME, 'p')
            # 获取 p 元素的文本内容
            text_content = first_p.text
            print(f"Answer:{text_content}")
            return text_content
        except Exception as e:
            print(f"出现错误: {e}")
        finally:
            # 关闭浏览器
            driver.quit()
            return ""

    

        

# 使用示例
if __name__ == "__main__":
    # 创建 SearchWrapper 类的实例
    search_wrapper = SearchWrapper()
    # 调用 perform_search 方法进行搜索
    print("Question:Romeo and Juliet")
    search_results = search_wrapper.kiwix_wikipedia('Romeo and Juliet')
    if search_results:
        # 若搜索结果不为 None，则打印搜索结果
        print(search_results)
