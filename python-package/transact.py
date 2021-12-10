#import amount,payer,payment,redirect_urls,transaction
import json
import webbrowser

import requests


class Payer:
    def getPaymentMethod():
        paymentMethod="Default"
        return paymentMethod

    def getUserEmail():
        userEmail="pytesting@gmail.com"
        return userEmail
    def getAutoLogin():
        AutoLogin="Enabled"
        return AutoLogin
    def getFirstName():
        firstName="Jane"
        return firstName
    def getLastName():
        lastName="Doe"
        return lastName
            
class RedirectUrls:
    def getSuccessUrl():
        successUrl='http://masstarg.com/demo/example-success.php'
        return successUrl
    def getCanceUrl():
        cancelUrl='http://masstarg.com/demo/example-cancel.php'
        return cancelUrl
class Amount:
    
    def getAmount():
        total=3
        return total
    def getCurrency():
        currency='USD'
        return currency


class OrderId:
    def getOrderId():
        orderId=1
        return orderId
class Transaction():
    def getAmount():
        Total=3
        return Total
    def getOrderId():
        orderId=1
        return orderId
        

payload=[]                   
class Payment:
    def getAcessToken():
        client_id=''
        client_secret=''
        payload={"client_id":client_id,"client_secret":client_secret}
    
        res= requests.post('https://avalanchepay.com/merchant/api/verify',data = payload)
        response=res.json()
       # response=json.loads(res)
        token=response['data']['access_token']
        return token

   


def sendTransactionInfo(token):
     #trans= Transaction.getTransaction()
     payer= Payer.getPaymentMethod()
    
     amount= Amount.getAmount()
     currency=Amount.getCurrency()
     orderId=OrderId.getOrderId()
     successUrl= RedirectUrls.getSuccessUrl()
     cancelUrl= RedirectUrls.getCanceUrl()
     paymentMethod = Payer.getPaymentMethod()
     userEmail = Payer.getUserEmail()
     autoLogin = Payer.getAutoLogin()
     firstName = Payer.getFirstName()
     lastName = Payer.getLastName()
     req={}
     req['payer']= paymentMethod
     req['amount']=amount
     req['currency']=currency
     req['orderId']=orderId
     req['successUrl']=successUrl
     req['cancelUrl']=cancelUrl
     req['userEmail']=userEmail
     req['firstName']=firstName
     req['lastName']=lastName
     req['autoLogin']=autoLogin
     req = json.dumps(req) 
     print(req)
     
     
     
auth_token=Payment.getAcessToken()
hed = {'Authorization': 'Bearer ' + auth_token}

def create():
    response = requests.post('https://avalanchepay.com/merchant/api/transaction-info', json = { 'payer': 'Default','amount':4.33,'currency':'USD','orderId':1,
    'successUrl':'http://masstarg.com/demo/example-success.php',
    'cancelUrl':'http://masstarg.com/demo/example-cancel.php',
    'userEmail':'testuser@gmail.com',
    'firstName':'Jane',
    'lastName':'Doe',
    'autoLogin':'Enabled'}, headers = hed)
   
    res = json.loads(response.text)
    res_data=res.get('data')
    approvedUrl=res_data.get('approvedUrl')
    print(approvedUrl)
    webbrowser.open(approvedUrl)
try :
    create()
except Exception as e:
    print(e)