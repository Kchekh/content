### Group-IB Digital Risk Protection  

- This section explains how to configure the **Digital Risk Protection** instance in **Cortex XSOAR**.  

#### Step 1: Open the Group-IB TI Web Interface  
1.1 Go to [https://drp.group-ib.com](https://drp.group-ib.com).  

#### Step 2: Authentication
2.1 In the new interface:  
  - Log in to your account on DRP: [drp.group-ib.com](drp.group-ib.com)
  - Go to the your profile settings [direct link](https://drp.group-ib.com/p/info/api).
  - Click the big blue button **Generate API key**. Then an API key will show up nearby.
  - Don’t forget to save API key during generation.

Success! Now you can use it with HTTP Basic Auth, where login is your email and password is your API token.

#### Step 3: Set Up Connection Details  
3.1 **Server URL:** Use your **DRP web interface URL**.  
3.2 **Username:** The email address used to log in to the web interface.  

#### Step 4: Configure Classifier and Mapper  
4.1 Set the **Classifier** and **Mapper** using the **Group-IB Digital Risk Protection** classifier and mapper.  
Note: Alternatively, you may configure your own setup if needed.  

#### Step 5: Configure Pre-Processing Rules  
5.1 Navigate to **Settings → Integrations → Pre-Processing Rules**. If a rule already exists, open it and verify it performs the following action. Otherwise, create a new rule:  
   - **Condition**: `"gibdrpid" is not empty (General)`.  
   - **Action**: `Run a script`.  
   - **Script**: `GIBDRPIncidentUpdate` – updates existing incidents without reopening those that were previously closed.  

#### Step 6: Whitelist Your Cortex XSOAR IP  
6.1 Contact **Group-IB support** to add your **Cortex XSOAR IP** or the **proxy public IP** used with Cortex to the allowlist.  