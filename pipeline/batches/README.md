# Department book batches (queued 17 Nov 2026)

100 department subjects (ECE, EEE, Mech, Civil, EIE, Chem, Auto, Aero, BME, Mechatronics, Nanotech, in that order),
split into five batches of about 122 units. Start one batch only when the five DeepSeek lanes are idle and it is
off-peak (outside 06:30-09:30 and 11:30-15:30 IST on weekdays): spread the batch's units over
pipeline/requests-deepseek.txt and -2 … -5 and push. A push to a request file cancels that lane's running job, so
never push while a lane is running. Check the balance first with the "DeepSeek balance" workflow (about $20 a batch).
