- text: |
    CONECTION_URI="redis://root:m42ploz2wd@google.com:5434/thegift"
  host: google.com
  port: "5434"
  username: root
  password: m42ploz2wd
  scheme: redis
  database: thegift
  connection_uri: redis://root:m42ploz2wd@google.com:5434/thegift

- text: |
    CONECTION_URI="rediss://root:m42ploz2wd@google.com:5434/thegift"
  host: google.com
  port: "5434"
  username: root
  password: m42ploz2wd
  scheme: rediss
  database: thegift
  connection_uri: rediss://root:m42ploz2wd@google.com:5434/thegift

# Test special characters in password
- text: |
    CONECTION_URI="rediss://root:m42p!o@2wd@google.com:5434/thegift"
  host: google.com
  port: "5434"
  username: root
  password: m42p!o@2wd
  scheme: rediss
  database: thegift
  connection_uri: rediss://root:m42p!o@2wd@google.com:5434/thegift

# Test detection in md files
- text: |
    CONECTION_URI="rediss://root:m42p!o@2wd@google.com:5434/thegift"
  host: google.com
  port: "5434"
  username: root
  password: m42p!o@2wd
  scheme: rediss
  database: thegift
  connection_uri: rediss://root:m42p!o@2wd@google.com:5434/thegift

