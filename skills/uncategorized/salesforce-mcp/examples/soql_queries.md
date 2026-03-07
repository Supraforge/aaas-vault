# Salesforce SOQL Query Examples

## Basic Queries

### Get All Open Opportunities
```sql
SELECT Id, Name, StageName, Amount, CloseDate, Probability
FROM Opportunity
WHERE IsClosed = false
ORDER BY CloseDate ASC
```

### Get Recent Leads
```sql
SELECT Id, FirstName, LastName, Company, Email, Status, CreatedDate
FROM Lead
WHERE CreatedDate = LAST_N_DAYS:30
ORDER BY CreatedDate DESC
```

### Get Contacts with Account Information
```sql
SELECT Id, FirstName, LastName, Email, Phone, Account.Name, Account.Industry
FROM Contact
WHERE Email != null
ORDER BY LastName
```

## Advanced Analytics

### Pipeline by Stage
```sql
SELECT StageName, COUNT(Id) opportunityCount, SUM(Amount) totalAmount
FROM Opportunity
WHERE IsClosed = false
GROUP BY StageName
ORDER BY totalAmount DESC
```

### Lead Conversion Rate
```sql
SELECT 
  COUNT(Id) totalLeads,
  SUM(CASE WHEN IsConverted = true THEN 1 ELSE 0 END) convertedLeads,
  (SUM(CASE WHEN IsConverted = true THEN 1 ELSE 0 END) / COUNT(Id)) * 100 conversionRate
FROM Lead
WHERE CreatedDate = LAST_N_DAYS:90
```

### Sales Performance by Owner
```sql
SELECT 
  Owner.Name,
  COUNT(Id) totalOpportunities,
  SUM(Amount) totalAmount,
  SUM(CASE WHEN StageName = 'Closed Won' THEN Amount ELSE 0 END) wonAmount,
  (SUM(CASE WHEN StageName = 'Closed Won' THEN 1 ELSE 0 END) / COUNT(Id)) * 100 winRate
FROM Opportunity
WHERE CloseDate = THIS_YEAR
GROUP BY Owner.Name
ORDER BY wonAmount DESC
```

## Data Export Queries

### Complete Contact Export
```sql
SELECT 
  Id, FirstName, LastName, Email, Phone, Title,
  Account.Name, Account.BillingStreet, Account.BillingCity,
  Account.BillingState, Account.BillingPostalCode, Account.BillingCountry,
  MailingStreet, MailingCity, MailingState, MailingPostalCode, MailingCountry,
  CreatedDate, LastModifiedDate
FROM Contact
WHERE Email != null
ORDER BY LastName
```

### Opportunity History
```sql
SELECT 
  Opportunity.Name,
  StageName,
  Amount,
  CloseDate,
  Probability,
  Account.Name,
  Owner.Name,
  CreatedDate,
  LastModifiedDate
FROM Opportunity
WHERE CloseDate = LAST_N_DAYS:365
ORDER BY CloseDate DESC
```
