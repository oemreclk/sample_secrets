- text: |
    CONNECTION_URI="db2://root:m42ploz2wd@google.com:5434/hellothere"
  host: google.com
  port: "5434"
  username: root
  password: m42ploz2wd
  scheme: db2
  database: hellothere
  connection_uri: db2://root:m42ploz2wd@google.com:5434/hellothere

- text: |
    uri="ibm_db_sa://user:str0ngp4ss@google.com:3000/hellothere"
  host: google.com
  port: "3000"
  username: user
  password: str0ngp4ss
  scheme: ibm_db_sa
  database: hellothere
  connection_uri: ibm_db_sa://user:str0ngp4ss@google.com:3000/hellothere

# Test special characters in password
- text: |
    uri="ibm_db_sa://user:str0ngp@ss!@google.com:3000/hellothere"
  host: google.com
  port: "3000"
  username: user
  password: str0ngp@ss!
  scheme: ibm_db_sa
  database: hellothere
  connection_uri: ibm_db_sa://user:str0ngp@ss!@google.com:3000/hellothere

# Test detection in md files
- text: |
    uri="ibm_db_sa://user:str0ngp@ss!@google.com:3000/hellothere"
  host: google.com
  port: "3000"
  username: user
  password: str0ngp@ss!
  scheme: ibm_db_sa
  database: hellothere
  connection_uri: ibm_db_sa://user:str0ngp@ss!@google.com:3000/hellothere
