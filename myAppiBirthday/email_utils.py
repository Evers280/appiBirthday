# myAppiBirthday/email_utils.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import logging


logger = logging.getLogger(__name__)

# Chemin vers le fichier d'identifiants OAuth 2.0
CREDENTIALS_FILE = 'myAppiBirthday/credentials/client_secret.json'  # Mettez à jour ce chemin
TOKEN_FILE = 'myAppiBirthday/credentials/token.pickle'  # Chemin pour stocker le jeton
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    # Charger le jeton d'accès s'il existe
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    
    # Si le jeton n'existe pas ou est invalide, en générer un nouveau
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8000)
        # Sauvegarder le jeton pour une utilisation future
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    
    # Créer un service Gmail
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_confirmation_email(invites, billets):
    subject = "Confirmation de votre inscription à la fête d'anniversaire"
    message_text = f"""
    Bonjour {invites.prenom} {invites.nom},

    Nous sommes ravis de confirmer votre inscription à la fête d'anniversaire !

    Voici vos informations d'inscription :
    - Nom : {invites.nom}
    - Prénom : {invites.prenom}
    - Email : {invites.email}
    - Téléphone : {invites.telephone}

    Voici les détails de votre billet :
    - Numéro de billet : {billets.num_billet}

    Merci de votre participation ! Si vous avez des questions, n'hésitez pas à nous contacter.

    Cordialement,
    L'équipe de la fête d'anniversaire
    """
    
    # Créer le message email
    message = MIMEText(message_text)
    message['to'] = invites.email
    message['from'] = 'eversdmbini@gmail.com'
    message['subject'] = subject
    
    # Encoder le message en base64
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw_message}
    
    try:
        service = get_gmail_service()
        message = (service.users().messages().send(userId='me', body=body).execute())
        logger.info(f"Email de confirmation envoyé à {invites.email}, ID du message : {message['id']}")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'email à {invites.email} : {str(e)}")
        raise
    
