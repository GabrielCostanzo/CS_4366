# CS_4366: Senior Capstone Project (Drink Trader)

## Listing Service API

* Manages auction any buy now listings

### getNumberOfListings
Returns the number of products you want 

#### Request
| Parameters| URL |
|-----------|--------|
| **int** num | http://127.0.0.1:5000/getNumberOfListings?num=3 |

#### Response 

```yaml
{
  "Success": true, 
  "data": [
    {
      "Expiration": "12/12/2022", 
      "Product": {
        "AlcoholPercentage": "72", 
        "AlcoholType": "Cognac", 
        "CountryOfOrigin": "France", 
        "Description": "X.O. is a blend of 100 eaux-de-vie that ranges in age from six to 30 years old. The liquid inside is excellent, warm, and a little bit spicy.", 
        "DrinkBrand": "Hennessey", 
        "DrinkName": "XO", 
        "Volume": "1500", 
        "_id": 4
      }, 
      "Seller": "Redbear", 
      "StartPrice": 25.0, 
      "Status": "Open", 
      "TerminatingPrice": 12.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 8067628
    }, 
    {
      "Expiration": "05/04/2022", 
      "Product": null, 
      "Seller": "Idontknow", 
      "StartPrice": 30.0, 
      "Status": "Open", 
      "TerminatingPrice": 15.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 7804093
    }, 
    {
      "Expiration": "02/04/2023", 
      "Product": {
        "AlcoholPercentage": "40", 
        "AlcoholType": "Whiskey", 
        "CountryOfOrigin": "France", 
        "Description": "This is a very special cognac with deep, fruity notes that call to mind a rum or aged whiskey.", 
        "DrinkBrand": "Hennessy", 
        "DrinkName": "Paradis Imperial", 
        "Volume": "750ml", 
        "_id": 2
      }, 
      "Seller": "gressy", 
      "StartPrice": 25.0, 
      "Status": "Open", 
      "TerminatingPrice": 18.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 9831368
    }
  ]
}      
```

### getOpenListing
Returns all open status listing 

#### Request
| Parameters| URL |
|-----------|--------|
| No Parameters | http://127.0.0.1:5000/getOpenListing |

#### Response 

```yaml
{
  "Success": true, 
  "data": [
    {
      "Expiration": "12/12/2022", 
      "Product": {
        "AlcoholPercentage": "72", 
        "AlcoholType": "Cognac", 
        "CountryOfOrigin": "France", 
        "Description": "X.O. is a blend of 100 eaux-de-vie that ranges in age from six to 30 years old. The liquid inside is excellent, warm, and a little bit spicy.", 
        "DrinkBrand": "Hennessey", 
        "DrinkName": "XO", 
        "Volume": "1500", 
        "_id": 4
      }, 
      "Seller": "Redbear", 
      "StartPrice": 25.0, 
      "Status": "Open", 
      "TerminatingPrice": 12.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 8067628
    }, 
    {
      "Expiration": "05/04/2022", 
      "Product": null, 
      "Seller": "Idontknow", 
      "StartPrice": 30.0, 
      "Status": "Open", 
      "TerminatingPrice": 15.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 7804093
    }, 
    {
      "Expiration": "02/04/2023", 
      "Product": {
        "AlcoholPercentage": "40", 
        "AlcoholType": "Whiskey", 
        "CountryOfOrigin": "France", 
        "Description": "This is a very special cognac with deep, fruity notes that call to mind a rum or aged whiskey.", 
        "DrinkBrand": "Hennessy", 
        "DrinkName": "Paradis Imperial", 
        "Volume": "750ml", 
        "_id": 2
      }, 
      "Seller": "gressy", 
      "StartPrice": 25.0, 
      "Status": "Open", 
      "TerminatingPrice": 18.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 9831368
    }
  ]
     
```

### getListingbyID
Returns all open status listing 

#### Request
| Parameters| URL |
|-----------|--------|
| **int** reqID | http://127.0.0.1:5000/getListingbyID?reqId=8067628 |

#### Response 

```yaml
{
  "Success": true, 
  "data": [
    {
      "Expiration": "12/12/2022", 
      "Product": {
        "AlcoholPercentage": "72", 
        "AlcoholType": "Cognac", 
        "CountryOfOrigin": "France", 
        "Description": "X.O. is a blend of 100 eaux-de-vie that ranges in age from six to 30 years old. The liquid inside is excellent, warm, and a little bit spicy.", 
        "DrinkBrand": "Hennessey", 
        "DrinkName": "XO", 
        "Volume": "1500", 
        "_id": 4
      }, 
      "Seller": "Redbear", 
      "StartPrice": 25.0, 
      "Status": "Open", 
      "TerminatingPrice": 12.0, 
      "Transcation": null, 
      "Type": "Bid", 
      "_id": 8067628
    }
  ]
}     
```


 
## Bid Service API

* Manages bids on auction listings

### getBids 
Returns a success message and a list of the bids associated with a listing, or an error message

#### Request
| Parameters| URL |
|-----------|--------|
| **int** lid | http://127.0.0.1:5000/bid_service/getBids?lid=357779 |

#### Response 

```yaml
{
  "Success": true, 
  "data": [
    {
      "Bid_Amount": 5.99, 
      "Time": "Wed, 31 Mar 2021 13:33:55 GMT", 
      "User": "testemail@gmail.com"
    }, 
    {
      "Bid_Amount": 8.0, 
      "Time": "Wed, 31 Mar 2021 13:34:16 GMT", 
      "User": "testemail@gmail.com"
    }, 
    {
      "Bid_Amount": 9.0, 
      "Time": "Wed, 31 Mar 2021 13:34:25 GMT", 
      "User": "testemail@gmail.com"
    }, 
    {
      "Bid_Amount": 12.0, 
      "Time": "Wed, 31 Mar 2021 15:10:20 GMT", 
      "User": "testemail@gmail.com"
    }, 
    {
      "Bid_Amount": 50.0, 
      "Time": "Wed, 31 Mar 2021 17:45:16 GMT", 
      "User": "testaccount@gmail.com"
    }, 
    {
      "Bid_Amount": 100.0, 
      "Time": "Wed, 31 Mar 2021 18:03:58 GMT", 
      "User": "testaccount@gmail.com"
    }, 
    {
      "Bid_Amount": 150.0, 
      "Time": "Wed, 31 Mar 2021 18:13:49 GMT", 
      "User": "testaccount@gmail.com"
    }
  ]
}     
```

### placeBid
Updates bid list of a listing if the new bid is higher than the previous, returns success message or error message

#### Request
| Parameters| URL |
|-----------|--------|
| **String** uid, **int** lid, **float** bid_amt  | http://127.0.0.1:5000/bid_service/placeBid?uid=123&lid=357779&bid_amt=200 |

#### Response 

```yaml
{
  "Success": true
}    
```

## Notification Service API

* Manages user email notifications

### Outbid notification 
Sends email to outbidded user

#### Request
| Parameters| URL |
|-----------|--------|
| **str** email, **int** lid | http://127.0.0.1:5000/listings/bids/notify?uid=email&lid=8067628 |

#### Response 

```yaml
{
  "success": True        
}      
```

## Account Service API

* Manages user accounts

### createAccount()
Creates a new user account

#### Request
| Parameters| URL |
|-----------|--------|
| **string** username, **stirng** email, **string** password, **string** first_name, **string** last_name | http://127.0.0.1:5000/examplefunction?testi=1&testj=2 |

#### Response 

```yaml
{
  ""Success": True, 
  "data":       
        {             
         "accountId" : 123456,
         "password" : "randomPwd",
         "first_name" : "randomUser",  
         "verified": True     
        }            
}      
```

### login()
Verifies user credentials and logs user in

#### Request
| Parameters| URL |
|-----------|--------|
| **string** username, **string** password | http://127.0.0.1:5000/examplefunction?testi=1&testj=2 |

#### Response 

```yaml
{
  "Success": True,
  "data":       
        {             
         "accountId" : 123456,
         "password" : "randomPwd",
         "first_name" : "randomUser",  
         "verified": True     
        }  
}      
```




