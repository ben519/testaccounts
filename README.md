# testaccounts

Skeleton app that should implement the following:

Anonymous users (users who are not logged in) should be able to create one or more League instances. These instances should be stored in the user's session. When a user logs in or registers, all leagues in the user's session should get associated to the user via a user id in the database.

Registration should require an email address (unique) and a password. Registering should automatically send an email activation link to confirm the authenticity and ownership of the user's email address

User's should be marked as "active" (or whatever other flag is commonly used) for a 3-day period, at which time, if they have not clicked the activation link in their email, they should be marked as inactive.
