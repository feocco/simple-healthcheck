"""
Poll site and send a notification if the site is down.

Use Discord Webhook URL to send a notification to a Discord channel.
"""

import os
import requests
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d ')


def get_docker_configs():
    """Get Docker configs from env variables."""
    logging.info('Getting Docker configs')
    
    healthcheck_interval_sec = os.environ.get('HEALTHCHECK_INTERVAL_SEC') or 300
    discord_webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    healthcheck_url = os.environ.get('HEALTHCHECK_URL')
    service_name = os.environ.get('SERVICE_NAME')
    
    if os.environ.get('VERIFY_SSL').lower() == 'false':
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    return discord_webhook_url, healthcheck_interval_sec, healthcheck_url, service_name


def send_notification(discord_webhook_url):
    webhook = DiscordWebhook(url=discord_webhook_url)
    embed = DiscordEmbed(title='Mealie is down!',
                         description='Mealie is down! Go check it out.', color='03b2f8')
    webhook.add_embed(embed)

    response = webhook.execute()
    
    if response.status_code != 200:
        logging.error(f'Error sending notification. Status code: {response.status_code}')
    else:
        logging.debug(f'Discord response code {response.status_code}')
    logging.info('Notification sent')


def main():
    logging.info('Starting health check service. Polling site every 5 minutes. (300 seconds)')
    
    while True:
        try:
            discord_webhook_url, healthcheck_interval_sec, healthcheck_url, service_name = get_docker_configs()
            logging.info(f"Polling {service_name} service @ {healthcheck_url} every {healthcheck_interval_sec} seconds via {discord_webhook_url}")

            r = requests.get(healthcheck_url, verify=False)
            logging.debug(f'Polling site. Status code: {r.status_code}')
            
            if r.status_code != 200:
                logging.info('Site is down. Sending notification')
                send_notification(discord_webhook_url)
        
        except requests.exceptions.RequestException as e:
            logging.error(f'Error polling site. Error: {e}')
            send_notification(discord_webhook_url)

        time.sleep(int(healthcheck_interval_sec))


if __name__ == "__main__":
    main()
