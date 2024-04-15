---
date: 2024-04-15T19:27:17.608264
author: AutoGPT <info@agpt.co>
---

# QR Code Generator API

To address the task effectively, we've engaged in a detailed discussion with the user to understand their specific needs for a QR code generation service. The key requirements gathered from the user are as follows:

1. **QR Code Customization:**
   - **Color Preference:** The user prefers the QR code to be of color violet.
   - **Format:** SVG is the desired format for the QR code, as specified by the user.
   - **Size:** The optimal size for the QR code, as per the user’s preference, is 500x500 pixels. This size balances scanability from a reasonable distance with spatial efficiency.
   - **Error Correction Level:** The user opts for a high error correction level (H), which ensures the QR code is resilient against up to 30% obscuration. This is crucial for maintaining accessibility and reliability under various physical conditions.

2. **Data Encoding:** The user intends to encode a URL into the QR code, specifically 'https://www.technewsreview.com.' This URL is directed towards a technology news and review site, indicating the QR code's intended use for direct online engagement.

Given these requirements, the end product is an endpoint that accepts the specified input parameters (color, format, size, error correction level, and data to encode) and generates a QR code that aligns with the user's specifications. The endpoint must support the generation of QR codes in SVG format, must allow for customization based on the provided parameters, and return the generated QR code that meets the defined criteria for size, color, error correction level, and encapsulated data.

For the development of this solution, the chosen tech stack includes: Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. This stack is selected for its robustness, scalability, and the community support available for each of these technologies.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'QR Code Generator API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
