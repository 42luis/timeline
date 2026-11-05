from os import getenv

from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()


SUPABASE_URL = getenv("SUPABASE_URL")
SUPABASE_KEY = getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be defined in .env"
    )


supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
