# What it does

Send emails that are on file email.json.

## Configuration

Configure on main.py the following variables:</br>
    HOST=""#example: smtp.gmail.com</br>
    PORT="" #example: 587</br>
    MAIL=""#example: example@example.com</br>
    PASSWORD=""#example: password</br>

Format of email.json:</br>
    {"email": "email@email.com","subject": "Funny subject","body": "Super funny body"}</br>

Only one email json per line.
## Usage

```
python3 main.py
```
