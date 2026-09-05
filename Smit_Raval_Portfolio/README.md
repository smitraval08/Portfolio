# Smit Raval — MCA Portfolio

Professional responsive portfolio built from the supplied CV and public profile links.

## Stack
- Python
- Flask
- HTML5
- CSS3
- Vanilla JavaScript
- MySQL (optional contact-message storage)

## Run
1. Create a virtual environment.
2. Install requirements:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add MySQL details if desired.
4. Create the database with:
   `mysql -u root -p < schema.sql`
5. Start:
   `python app.py`
6. Open `http://127.0.0.1:5000`

The portfolio works without MySQL; the contact form simply runs in demo mode.

## Included profile
- Smit Raval
- Ahmedabad
- MCA — 1st Semester
- Email from supplied CV
- Skills from supplied CV
- Civic Issue Reporting and Tracking System from supplied CV
- Public GitHub repositories surfaced from the supplied GitHub profile
- LinkedIn and YouTube buttons from the supplied links

## Note
The public GitHub page currently shows 5 repositories, including Electrical_Service, ele_service,
chatgpt, Simple-Weather and git-commit. Project descriptions are kept conservative and based only
on information visible on the supplied profile/CV.
