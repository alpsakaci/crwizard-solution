## Running app with Docker

### Create .env file in the base directory.  (the same directory where docker-compose.yaml resides)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='your-oauth-key'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='your-oauth-secret'

EMAIL_HOST_USER='your-email'

EMAIL_HOST_PASSWORD='your-email-password'


### $ docker build -t crwizard_solution .
### $ docker-compose build
### $ docker-compose up -d
