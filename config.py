HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["2016487075:AAHSrlYXi2I8nuEg38Kdb2AG_M_S6sJKS-w"]
    ARQ_API_KEY = environ["GJRBXI-VJSVII-BKPOJT-LYMVEE-ARQ"]
    LANGUAGE = environ["en"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "2016487075:AAHSrlYXi2I8nuEg38Kdb2AG_M_S6sJKS-w"
    ARQ_API_KEY = "GJRBXI-VJSVII-BKPOJT-LYMVEE-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"





# Leave it as it is
ARQ_API_BASE_URL = "https://thearq.tech"
