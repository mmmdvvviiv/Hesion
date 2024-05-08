#cod py ZEFF_X
import os,sys,time,random,requests,re,telebot

from bs4 import BeautifulSoup as bs
from datetime import datetime

url='https://n.facebook.com'
xurl=url+'/login.php'

ua="Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
def login(user, pswd):
	try:
		req=requests.Session()
		req.headers.update({
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en_US','cache-control': 'max-age=0',
		'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
		'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
		'user-agent': ua})
		with req.get(url) as response_body:
			inspect=bs(response_body.text,'html.parser')
			lsd_key=inspect.find('input',{'name':'lsd'})['value']
			jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
			m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
			li_key=inspect.find('input',{'name':'li'})['value']
			try_number_key=inspect.find('input',{'name':'try_number'})['value']
			unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
			bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']
			data={
			'lsd':lsd_key,'jazoest':jazoest_key,
			'm_ts':m_ts_key,'li':li_key,
			'try_number':try_number_key,
			'unrecognized_tries':unrecognized_tries_key,
			'bi_xrwh':bi_xrwh_key,'email':user,
			'pass':pswd,'login':"submit"}
			response_body2=req.post(xurl,data=data,allow_redirects=True,timeout=300)
			cookie=str(req.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
			if 'checkpoint' in cookie:
			    return "• Account Checkpoint!! •"
			elif 'c_user' in cookie:
				return str(cookie).replace(' ', '')
			else:
				return '• Incorrect details!! •'
	except requests.exceptions.ConnectionError:sys.exit('No internet')
	except KeyboardInterrupt:sys.exit("[+] Stopped!")
token = "6419465759:AAEzLvHEr3S0u7bJeZNAFCq9PbGVmQOqy-c"
bot = telebot.TeleBot(token)
us = bot.get_me().username


@bot.message_handler(commands=["start"])
def start(message):
        bot.reply_to(message, """
↯︙ مرحبا بك عزيزي في بوت استخراج كوكيز  الفيسبوك[📣] 
عزيزي  المستخدم    عطي الحساب بصوره 
gmail:Password 
ا-----------------------------------------------------------
↯︙ Welcome, dear, to the Facebook cookie extractor bot [] Dear user, give the account in the form of gmail:Password [🎭]

  $& @lIIHII  &$  👈 اتواصل معه المبرمج

""")     
@bot.message_handler(func=lambda m: True)
def getAcc(message):
  try:
    msg = message.text.split(':')
    email = msg[0]
    passw = msg[1]
    bot.reply_to(message, '• انتظر...')
    cookies = login(email, passw)
    if 'datr' in cookies:
      if cookies.startswith('c'):
        c_user = cookies.split(';datr')[0]+';'
        datrAdd = 'datr'+cookies.split(';datr')[1]
        getDatr = re.findall('datr=.*?;', datrAdd)[0]
        Cok = datrAdd.replace(getDatr, getDatr+c_user)
        cookies = f'`{Cok}`'
    bot.reply_to(message, cookies, parse_mode='markdown')
  except:pass

bot.infinity_polling()
