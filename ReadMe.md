# What it does

Send emails that are on file email.json.

## Configuration

Configure on main.py the following variables:
    HOST=""#example: smtp.gmail.com
    PORT="" #example: 587
    MAIL=""#example: example@example.com
    PASSWORD=""#example: password

Format of email.json:
    {"email": "email@email.com","subject": "Funny subject","body": "Super funny body"}

Only one email json per line.
## Usage

```
python3 main.py
```
