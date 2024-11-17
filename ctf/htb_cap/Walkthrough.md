
# 🎩 **Cap | Hack The Box Walkthrough**

Written By @[Mohamed haneef](https://www.linkedin.com/in/mohamed-haneef22).

Welcome to the walkthrough for the **Cap** challenge on Hack The Box! 🚀 Let’s dive into uncovering the flags step by step. 🕵️‍♂️

---

## 🛠️ **Step 1: Aggressive Port Scan**

We start with an aggressive **nmap** scan to identify open ports and services:

```bash
nmap [IP] -A
```

### Results 🎯  
After the scan, we observe that the following ports are open:  
- **21 (FTP)**  
- **22 (SSH)**  
- **80 (HTTP)**  

📄 [Check out the full scan report here!](./nmapscan.txt)

---

## 🌐 **Step 2: Exploring the HTTP Port**

Navigating to the HTTP service in a browser, we find an interesting page.  
> ⚡ The "Security Snapshot" redirects us to `/data/[rand_value]`.

🖼️ [View the page snapshot here.](./images/htb-cap2.png)

### Digging Deeper 🔍  
When we input the value `0`, we download a `.pcap` file containing network traffic data.

🖼️ [See the result here.](./images/htb-cap3.png)

---

## 🗄️ **Step 3: Analyzing the PCAP File**

After analyzing the `.pcap` file, we extract FTP credentials! 🎉  
🖼️ [Screenshot of the analysis.](./images/htb-cap4.png)

**Credentials:**  
- **Username:** `nathan`  
- **Password:** `Buck3tH4TF0RM3!`  

📌 *Note: These credentials work for both FTP and SSH!*  

---

## 📂 **Step 4: Logging into the FTP Server**

Using the credentials, we log into the FTP server:  

```bash
ftp [IP]
```

Here, we find the **`user.txt`** file containing the first flag. 🏁  

USER FLAG: 

---

## 🚀 **Step 5: Privilege Escalation**

To escalate privileges, we upload and execute **`linpeas.sh`**. This reveals that Python has the necessary permissions to elevate our privileges. 💡  

🖼️ [LinPEAS output screenshot.](./images/htb-cap5.png)

### Gaining Root Access 👑  
We use Python to execute a simple command and retrieve the **root flag**:

```python -c 'import os; os.setuid(0); os.system("cat /root/root.txt")'```

🖼️ [Root flag screenshot.](./images/htb-cap6.png)

---

### 🏆 **Conclusion**  

With careful reconnaissance and privilege escalation, we retrieved both the user and root flags. 🎉 **Cap** was a fun box with lots of opportunities to practice your enumeration and privilege escalation skills! 💻  

Happy hacking! 💀  
