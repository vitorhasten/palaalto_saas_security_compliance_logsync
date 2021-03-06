# palaalto_saas_security_compliance_logsync (v1.0.0)
##### About
paloalto_saas_security_compliance_logsync is a utility written by me (Vitor Hastenrreinter) to enable fetching logs from Palo Alto SaaS Security API services and enabling customers to feed it to different SIEMs. Incremental updates will be published as we add more features. 

Ref: https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-api.html

---

##### Installation

- Make sure you are running python 3+ “python --version”
- Clone the github repository
- If you get error about setuptools, install it using “pip3 install setuptools”
- Refer the `Configuration` section below. You will need create `config.ini` file and fill out credentials for API in PaloAlto SaaS Security&Compliance section as well as other parameters if necessary
- Run the application using "python3 <complete/path/to/code.py> <complete/path/to/config.ini>"

---

##### Features

- 

---

##### Work in progress

- Output in Common Event Format (ArcSight)
- Output to Syslog destination
- Output to Splunk API

---

##### Configuration

- Check `template_config.ini` for an example and for extensive, in-depth config explanation
