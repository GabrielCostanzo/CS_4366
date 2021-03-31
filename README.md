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

### Example Function Name 
Returns the sum of two parameters

#### Request
| Parameters| URL |
|-----------|--------|
| **int** testi, **float** testj | http://127.0.0.1:5000/examplefunction?testi=1&testj=2 |

#### Response 

```yaml
{
  "valid: True,
  "data":       
        {             
         "testi": 1,  
         "testj": 2,  
         "sum": 3     
        }            
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
| **int** testi, **float** testj | http://127.0.0.1:5000/examplefunction?testi=1&testj=2 |

#### Response 

```yaml
{
  ""Success": True, 
  "data":       
        {             
         "accountId" : 123456, 
         "first_name" : "randomUser"  
         "verified": True     
        }            
}      
```

### login()
Verifies user credentials and logs user in

#### Request
| Parameters| URL |
|-----------|--------|
| **int** testi, **float** testj | http://127.0.0.1:5000/examplefunction?testi=1&testj=2 |

#### Response 

```yaml
{
  "Success": True,
  "data":       
        {             
         "accountId" : 123456, 
         "first_name" : "randomUser"  
         "verified": True     
        }  
}      
```




