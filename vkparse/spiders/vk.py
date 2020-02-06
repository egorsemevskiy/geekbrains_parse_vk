# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from selenium import webdriver
import time
from vkparse.items import VkparseItem
from selenium.webdriver.common.keys import Keys


class VkSpider(scrapy.Spider):
    name = 'vk'
    allowed_domains = ['vk.com']
    start_urls = ['https://vk.com/']

    browser = webdriver.Firefox()

    def parse(self, response: HtmlResponse):
        self.browser.get('https://vk.com/mashinnoe_obuchenie_ai_big_data')
        self.login()
        time.sleep(5)
        self.members()
        time.sleep(5)
        self.followers_id()

    def login(self):
        input_mail = self.browser.find_element_by_css_selector('#quick_email')
        input_mail.click()
        input_mail.send_keys('jumbojet@pisem.net')
        input_pass = self.browser.find_element_by_css_selector('#quick_pass')
        input_pass.click()
        input_pass.send_keys('567Vkontakte')
        submit = self.browser.find_element_by_css_selector('#quick_login_button')
        submit.click()

    def members(self):
        action = self.browser.find_element_by_css_selector('a.module_header span.header_label.fl_l')
        action.click()
        body = self.browser.find_element_by_css_selector('body')
        time.sleep(5)
        for _ in range(10):
            time.sleep(0.3)
            body.send_keys('Keys.PAGE_DOWN ')

    def followers_id(self):
        followers = [itm.get_attribute('data-id') for itm in
                     self.browser.find_elements_by_css_selector('div.fans_rows div.fans_fan_row')]
        for follower in followers:
            self.save_item_to_mongogb(follower)

    def save_item_to_mongogb(follower):
        item = ItemLoader(VkparseItem())
        item.add_value('vk_id', follower)
        yield item.load_item()