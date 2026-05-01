from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
co.set_address('127.0.0.1:9222')  # 指定调试地址和端口

page = ChromiumPage(addr_or_opts=co)
page.get('https://linux.do')
print(page.title)
page.quit()