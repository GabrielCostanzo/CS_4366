# CS_4366: Senior Capstone Project (Drink Trader)

## Listing Service API

* Manages auction any buy now listings

### GetNumberProducts
Returns the number of products you want 

#### Request
| Parameters| URL |
|-----------|--------|
| **int** num | http://127.0.0.1:5000/GetNumberProducts?num=3 |

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

### getOpenListing
Returns all open status listing 

#### Request
| Parameters| URL |
|-----------|--------|
| No Parameters | http://127.0.0.1:5000/getOpenListing |

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

### getListingbyID
Returns all open status listing 

#### Request
| Parameters| URL |
|-----------|--------|
| **int** reqID | http://127.0.0.1:5000/getListingbyID?reqId=218278 |

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

## Account Service API

* Manages user accounts

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
