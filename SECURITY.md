# Security Policy

## Secrets

Never commit API keys, OAuth tokens, Gmail credentials or `.env` files. Use n8n credentials or environment variables and rotate any secret that is accidentally exposed.

## Personal data

The sample workflow processes a name and an email address. A production deployment must collect consent, restrict access, encrypt traffic, define data retention and avoid saving full execution payloads unnecessarily.

## Financial safety

This project provides educational simulations only. The Python service owns all calculations, while the language model is restricted to explanation. Outputs must not be presented as individualized investment recommendations.

## Reporting

Report vulnerabilities privately to the repository owner. Do not publish credentials, personal data or a working exploit in a public issue.

