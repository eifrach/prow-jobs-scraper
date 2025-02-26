import os

from prowjobsscraper.equinix_usages import EquinixUsagesScrapeInterval

ES_URL = os.environ["ES_URL"]
ES_USER = os.environ["ES_USER"]
ES_PASSWORD = os.environ["ES_PASSWORD"]
ES_STEP_INDEX = os.environ["ES_STEP_INDEX"]
ES_JOB_INDEX = os.environ["ES_JOB_INDEX"]
ES_USAGE_INDEX = os.environ["ES_USAGE_INDEX"]
JOB_LIST_URL = os.environ["JOB_LIST_URL"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
EQUINIX_PROJECT_ID = os.environ["EQUINIX_PROJECT_ID"]
EQUINIX_PROJECT_TOKEN = os.environ["EQUINIX_PROJECT_TOKEN"]
EQUINIX_USAGES_SCRAPE_INTERVAL = EquinixUsagesScrapeInterval(
    os.environ["EQUINIX_USAGES_SCRAPE_INTERVAL"]
)
