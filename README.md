# watchlist
Simple Python Flask Websapp to Show Stock Prices using Alpaca API 



## Localhost using Anaconda

### Create and activate new environment
```
conda create -n watchlist python=3.7 anaconda
conda activate watchlist
```
### Install all Python Dependencies

```
pip install python-dotenv
pip install alpaca-trade-api
pip install Flask
```

## Webhosting

To install on shared webhosting (like Dreamhost) 

Use this Link: https://www.brettsbeta.com/blog/2020/07/flask-on-dreamhost-shared-website-hosting/

### Custom Troubleshooting Steps:
Then edit .htaccess file:
```
vi .htaccess
```

Development Mode: And add the following:
```
PassengerFriendlyErrorPages on
```

Production Mode: And add the following:
```
PassengerFriendlyErrorPages off
```
