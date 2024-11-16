# White Rose || Tryhackme Walkthrough

### Task 1:

By doing subdomain enumeration we found out that the login page for the admin is in ***admin.cyprus.thm*** [add it to your /etc/hosts file]

After Logging in with the given Credentials 'Olivia Cortez:olivi8' we get to see the admin panel, But somehow the phone numbers are not visible.

Looking around the page we found out that there is a '/messages' page.

By doing a slight modification in the url parameter we can get the previous chat

Changing the parameter c in the url to 15 we can see the previos messages

url: ```http://admin.cyprusbank.thm/messages/?c=15```

After Modification Chat will be like

**Cyprus National Bank** - Admin Chat

**DEV TEAM**: Thanks Gayle, can you share your credentials? We need privileged admin account for testing

**Gayle Bev**: Of course! My password is 'p~]P@5!6;rs558:q'

**DEV TEAM**: Alright we are trying to implement chat history, everything should be ready in week or so

**Gayle Bev**: That's nice to hear!

**Gayle Bev**: Developers implemented this new messaging feature that I suggested! What you guys think?

**Greger Ivayla**: Looks really cool!

**Jemmy Laurel**: Hey have you guys seen Mrs. Jacobs recently??

**Olivia Cortez**: No she hasn't been around for a while

**Jemmy Laurel**: Oh, is she OK?

So we Got another Username and Password

Username: Gayle Bev
Password: p~]P@5!6;rs558:q

By logging in with the given credentials again

We got the phone numbers visible

---

Q1 : What's Tyrell Wellick's phone number?
Ans: 842-029-5701

---
